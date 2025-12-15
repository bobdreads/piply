from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from .utils import get_ptax

User = get_user_model()

# --- Auxiliares ---


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name

# --- Principais ---


class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='portfolios')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='BRL')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} ({self.currency})"


class Strategy(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='strategies')
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self): return self.name


class Trade(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Em Aberto'
        CLOSED = 'CLOSED', 'Fechado'

    class Side(models.TextChoices):
        BUY = 'BUY', 'Compra'
        SELL = 'SELL', 'Venda'

    class AssetType(models.TextChoices):
        BR_STOCK = 'BR_STOCK', 'Ações BR (Swing)'
        BR_DAYTRADE = 'BR_DAYTRADE', 'Day Trade (Índice/Dólar/Ação)'
        BR_FII = 'BR_FII', 'Fundos Imobiliários (FII)'
        BR_ETF = 'BR_ETF', 'ETF Brasileiro'
        US_STOCK = 'US_STOCK', 'Stocks/REITs/ETFs EUA'
        CFD = 'CFD', 'CFD (Forex/Índices/Commodities)'
        CRYPTO = 'CRYPTO', 'Criptomoedas'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trades')
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='trades')
    strategy = models.ForeignKey(
        Strategy, on_delete=models.SET_NULL, null=True, blank=True)

    symbol = models.CharField(max_length=50)
    asset_type = models.CharField(
        max_length=20, choices=AssetType.choices, default=AssetType.BR_STOCK)
    side = models.CharField(max_length=4, choices=Side.choices)

    # Valores
    quantity = models.DecimalField(max_digits=15, decimal_places=5, default=1)
    entry_price = models.DecimalField(
        max_digits=15, decimal_places=5, default=0)
    exit_price = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, null=True, blank=True)

    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_result = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)

    total_sale_value = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, editable=False)

    # exchange_rate com blank=True para não travar o formulário
    exchange_rate = models.DecimalField(
        max_digits=10, decimal_places=4, default=1.0000, blank=True)

    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.OPEN)

    # Data editável agora!
    created_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == self.Status.CLOSED and not self.closed_at:
            self.closed_at = timezone.now()

        # Robô de PTAX
        if self.status == self.Status.CLOSED and self.asset_type in [self.AssetType.US_STOCK, self.AssetType.CFD, self.AssetType.CRYPTO]:
            if self.exchange_rate == Decimal('1.0000'):
                rate = get_ptax(self.closed_at)
                if rate:
                    self.exchange_rate = Decimal(str(rate))

        if self.exit_price and self.quantity:
            self.total_sale_value = self.exit_price * self.quantity * self.exchange_rate

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.symbol} ({self.get_status_display()})"

# --- Relatório Fiscal ---


class TaxReport(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tax_reports')
    month = models.DateField()

    sales_volume_br_swing = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    result_br_daytrade = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    result_br_swing = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    result_br_fii = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    tax_due_br = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)

    result_offshore = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    tax_provision_offshore = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)

    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'month')

    def __str__(self):
        return f"Relatório {self.month.strftime('%m/%Y')}"

# --- Outros ---


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)


class JournalNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class TradeEntry(models.Model):
    trade = models.ForeignKey(
        Trade, related_name='entries', on_delete=models.CASCADE)
    # Campos opcionais caso use o modelo simplificado
    price = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True)
    quantity = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True)


class TradeExit(models.Model):
    trade = models.ForeignKey(
        Trade, related_name='exits', on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True)
    quantity = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True)


class PortfolioTransaction(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=15, decimal_places=2)

# --- SIGNAL ---


@receiver(post_save, sender=Trade)
def recalculate_tax(sender, instance, **kwargs):
    if instance.status != Trade.Status.CLOSED:
        return

    ref_date = instance.closed_at or instance.created_at
    month_start = ref_date.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0)

    report, _ = TaxReport.objects.get_or_create(
        user=instance.user, month=month_start)

    trades = Trade.objects.filter(
        user=instance.user,
        closed_at__year=month_start.year,
        closed_at__month=month_start.month,
        status=Trade.Status.CLOSED
    )

    vol_br_swing = Decimal(0)
    res_br_dt = Decimal(0)
    res_br_sw = Decimal(0)
    res_br_fii = Decimal(0)
    res_offshore = Decimal(0)

    for t in trades:
        val_brl = t.net_result * t.exchange_rate
        if t.asset_type == Trade.AssetType.BR_DAYTRADE:
            res_br_dt += val_brl
        elif t.asset_type == Trade.AssetType.BR_STOCK:
            res_br_sw += val_brl
            vol_br_swing += t.total_sale_value
        elif t.asset_type == Trade.AssetType.BR_FII:
            res_br_fii += val_brl
        elif t.asset_type in [Trade.AssetType.US_STOCK, Trade.AssetType.CFD, Trade.AssetType.CRYPTO]:
            res_offshore += val_brl

    tax_br_sw = Decimal(0)
    if vol_br_swing > 20000 and res_br_sw > 0:
        tax_br_sw = res_br_sw * Decimal('0.15')

    tax_br_dt = res_br_dt * Decimal('0.20') if res_br_dt > 0 else Decimal(0)
    tax_br_fii = res_br_fii * Decimal('0.20') if res_br_fii > 0 else Decimal(0)
    tax_offshore = res_offshore * \
        Decimal('0.15') if res_offshore > 0 else Decimal(0)

    report.sales_volume_br_swing = vol_br_swing
    report.result_br_daytrade = res_br_dt
    report.result_br_swing = res_br_sw
    report.result_br_fii = res_br_fii
    report.result_offshore = res_offshore
    report.tax_due_br = tax_br_sw + tax_br_dt + tax_br_fii
    report.tax_provision_offshore = tax_offshore

    report.save()
