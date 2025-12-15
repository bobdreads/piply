from rest_framework import serializers
from .models import (
    Portfolio, Strategy, Trade, JournalNote, Tag,
    TradeEntry, TradeExit, PortfolioTransaction,
    TaxReport, Ticket
)

# --- Auxiliares ---


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# --- Transações & Detalhes ---


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTransaction
        fields = '__all__'


class TradeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeEntry
        fields = ['id', 'price', 'quantity', 'entry_date']


class TradeExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeExit
        fields = ['id', 'price', 'quantity', 'exit_type', 'exit_date']

# --- Principais ---


class PortfolioSerializer(serializers.ModelSerializer):
    # Mostra o saldo calculado se quiser, ou usa o do model
    class Meta:
        model = Portfolio
        fields = '__all__'
        read_only_fields = ('user',)


class StrategySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='tags', write_only=True, many=True
    )

    class Meta:
        model = Strategy
        fields = '__all__'
        read_only_fields = ('user',)


class TradeSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display', read_only=True)
    entries = TradeEntrySerializer(many=True, read_only=True)
    exits = TradeExitSerializer(many=True, read_only=True)

    # Para exibir o nome da estratégia e portfolio na leitura
    strategy_name = serializers.CharField(
        source='strategy.name', read_only=True)
    portfolio_name = serializers.CharField(
        source='portfolio.name', read_only=True)

    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'net_result')


class JournalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalNote
        fields = '__all__'
        read_only_fields = ('user', 'created_at')

# --- Especiais (PDF FinBoard 2.0) ---


class TaxReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'tax_due', 'net_profit',
                            'total_fees', 'total_gross_profit', 'total_losses')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at', 'status')
