from django.contrib import admin
from .models import (
    Portfolio, Strategy, Trade, JournalNote, Tag,
    TradeEntry, TradeExit, PortfolioTransaction,
    TaxReport, Ticket
)

# --- Configurações de Inlines (Para editar tudo na mesma tela) ---


class TradeEntryInline(admin.TabularInline):
    model = TradeEntry
    extra = 1


class TradeExitInline(admin.TabularInline):
    model = TradeExit
    extra = 0


class TransactionInline(admin.TabularInline):
    model = PortfolioTransaction
    extra = 0

# --- Admins Principais ---


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'balance', 'currency', 'created_at')
    search_fields = ('name', 'user__username')
    inlines = [TransactionInline]


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    filter_horizontal = ('tags',)  # Facilita a seleção de muitas tags


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'side', 'status',
                    'net_result', 'user', 'created_at')
    list_filter = ('status', 'side', 'created_at')
    search_fields = ('symbol', 'user__username')
    # Permite adicionar entradas/saídas dentro do Trade
    inlines = [TradeEntryInline, TradeExitInline]

    # Organiza os campos em seções
    fieldsets = (
        ('Identificação', {
            'fields': ('user', 'portfolio', 'strategy', 'symbol')
        }),
        ('Detalhes da Operação', {
            'fields': ('side', 'status')
        }),
        ('Resultado', {
            'fields': ('fees', 'net_result'),
            'classes': ('collapse',)  # Esconde por padrão para não poluir
        }),
    )


@admin.register(TaxReport)
class TaxReportAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'net_profit', 'tax_due', 'is_paid')
    list_filter = ('is_paid', 'month')
    list_editable = ('is_paid',)  # Permite marcar como pago direto na lista


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'user', 'status', 'created_at')
    list_filter = ('status',)


# --- Registros Simples ---
admin.site.register(Tag)
admin.site.register(JournalNote)
# admin.site.register(TradeEntry) # Não precisa registrar solto se já está no inline do Trade
# admin.site.register(TradeExit)
