from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

User = get_user_model()

# --- Modelos Auxiliares ---


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# --- Modelos Principais ---


class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='portfolios')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='BRL')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Strategy(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='strategies')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Trade(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Em Aberto'
        CLOSED_TARGET = 'CLOSED_TARGET', 'Fechado no Alvo'
        CLOSED_STOP = 'CLOSED_STOP', 'Fechado no Stop'
        CLOSED_MANUAL = 'CLOSED_MANUAL', 'Fechado Manualmente'

    class Side(models.TextChoices):
        BUY = 'BUY', 'Compra'
        SELL = 'SELL', 'Venda'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trades')
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='trades')

    # --- CORREÇÃO: Campo Strategy Adicionado ---
    strategy = models.ForeignKey(
        Strategy, on_delete=models.SET_NULL, null=True, blank=True, related_name='trades')

    symbol = models.CharField(max_length=50)
    side = models.CharField(max_length=4, choices=Side.choices)

    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_result = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)

    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} {self.symbol} - {self.get_status_display()}"


class JournalNote(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='journal_notes')
    trade = models.ForeignKey(
        Trade, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
    strategy = models.ForeignKey(
        Strategy, on_delete=models.SET_NULL, null=True, blank=True)

    notes = models.TextField()
    confidence_level = models.IntegerField(
        default=5, help_text="Nível de confiança de 1 a 10")
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota de {self.user.username} em {self.created_at.strftime('%d/%m/%Y')}"

# --- Detalhamento de Operações ---


class TradeEntry(models.Model):
    trade = models.ForeignKey(
        Trade, related_name='entries', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    entry_date = models.DateTimeField(default=timezone.now)


class TradeExit(models.Model):
    class ExitType(models.TextChoices):
        STOP_LOSS = 'SL', 'Stop Loss'
        TAKE_PROFIT = 'TP', 'Take Profit'
        MANUAL = 'MANUAL', 'Fechamento Manual'

    trade = models.ForeignKey(
        Trade, related_name='exits', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    exit_type = models.CharField(
        max_length=10, choices=ExitType.choices, default=ExitType.MANUAL)
    exit_date = models.DateTimeField(default=timezone.now)


class PortfolioTransaction(models.Model):
    class Type(models.TextChoices):
        DEPOSIT = 'DEPOSIT', 'Depósito'
        WITHDRAWAL = 'WITHDRAWAL', 'Saque'

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=Type.choices)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

# --- MÓDULOS ESPECIAIS ---


class TaxReport(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tax_reports')
    month = models.DateField(help_text="Primeiro dia do mês de referência")

    total_gross_profit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    total_losses = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    total_fees = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    net_profit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)

    tax_due = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'month')

    def __str__(self):
        return f"DARF {self.month.strftime('%m/%Y')} - {self.user.username}"


class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Aberto'
        IN_PROGRESS = 'IN_PROGRESS', 'Em Andamento'
        CLOSED = 'CLOSED', 'Fechado'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tickets')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject}"

# --- SIGNALS ---


@receiver(post_save, sender=Trade)
def update_tax_report(sender, instance, created, **kwargs):
    if instance.status in [Trade.Status.CLOSED_TARGET, Trade.Status.CLOSED_STOP, Trade.Status.CLOSED_MANUAL]:
        report_month = instance.created_at.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0)

        report, _ = TaxReport.objects.get_or_create(
            user=instance.user,
            month=report_month
        )

        trades_in_month = Trade.objects.filter(
            user=instance.user,
            created_at__year=report_month.year,
            created_at__month=report_month.month,
            status__in=[Trade.Status.CLOSED_TARGET,
                        Trade.Status.CLOSED_STOP, Trade.Status.CLOSED_MANUAL]
        )

        aggregates = trades_in_month.aggregate(
            sum_result=Sum('net_result'),
            sum_fees=Sum('fees')
        )

        total_net = aggregates['sum_result'] or 0
        total_fees = aggregates['sum_fees'] or 0

        report.net_profit = total_net
        report.total_fees = total_fees

        if total_net > 0:
            report.tax_due = total_net * 0.15
        else:
            report.tax_due = 0

        report.save()
