from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import (
    Portfolio, Strategy, Trade, JournalNote, Tag,
    TradeEntry, TradeExit, PortfolioTransaction,
    TaxReport, Ticket
)

# --- Inlines (Opcionais para trades parciais) ---


class TradeEntryInline(TabularInline):
    model = TradeEntry
    extra = 0
    tab = True


class TradeExitInline(TabularInline):
    model = TradeExit
    extra = 0
    tab = True


class TransactionInline(TabularInline):
    model = PortfolioTransaction
    extra = 0
    tab = True

# --- Admins ---


@admin.register(Trade)
class TradeAdmin(ModelAdmin):
    # Lista organizada
    list_display = ('symbol', 'status', 'side', 'asset_type',
                    'entry_price', 'net_result', 'created_at')
    list_filter = ('status', 'asset_type', 'portfolio')
    search_fields = ('symbol',)
    inlines = [TradeEntryInline, TradeExitInline]

    # SEÇÕES ORGANIZADAS COMO PEDIDO
    fieldsets = (
        # Aba 1: O Básico (Igual antes)
        ('Configuração do Trade', {
            'fields': ('user', 'portfolio', 'strategy', 'symbol', 'asset_type', 'side')
        }),

        # Aba 2: Preços e Datas (Agora com Data Editável!)
        ('Execução', {
            'fields': ('quantity', 'entry_price', 'exit_price', 'created_at', 'closed_at', 'status')
        }),

        # Aba 3: Resultado Financeiro
        ('Financeiro', {
            'fields': ('fees', 'net_result')
        }),

        # Aba 4: Fiscal & Sistema (A "Quarta Aba" isolada)
        ('Dados Fiscais (Automático)', {
            'classes': ('collapse',),  # Começa fechado para não poluir
            'description': 'A PTAX é buscada automaticamente no Banco Central ao fechar trades internacionais.',
            'fields': ('exchange_rate', 'total_sale_value')
        }),
    )

    # Impede edição manual acidental da PTAX, mas mostra o valor
    # Se quiser editar na mão em caso de erro, remova 'exchange_rate' daqui.
    readonly_fields = ('total_sale_value',)


@admin.register(TaxReport)
class TaxReportAdmin(ModelAdmin):
    list_display = ('__str__', 'tax_due_br',
                    'tax_provision_offshore', 'is_paid')
    list_filter = ('month', 'is_paid')


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ('name', 'user', 'balance')
    inlines = [TransactionInline]


@admin.register(Strategy)
class StrategyAdmin(ModelAdmin):
    filter_horizontal = ('tags',)


@admin.register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = ('subject', 'status')


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass


@admin.register(JournalNote)
class JournalNoteAdmin(ModelAdmin):
    pass
