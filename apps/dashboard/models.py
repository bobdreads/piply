from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    # Usando TextChoices para melhor legibilidade e suporte a tradução nativa do Django
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
    symbol = models.CharField(max_length=50)  # Ex: EURUSD, BTCUSDT
    side = models.CharField(max_length=4, choices=Side.choices)

    # Valores financeiros
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
    # Opcional: Vincular a um trade específico ou estratégia
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

# --- Detalhamento de Operações (Normalização) ---


class TradeEntry(models.Model):
    trade = models.ForeignKey(
        Trade, related_name='entries', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    entry_date = models.DateTimeField(default=timezone.now)


class TradeExit(models.Model):
    """Unifica Stop, Target e Manual Close para simplificar a arquitetura"""
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
