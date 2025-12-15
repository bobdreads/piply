from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline  # <--- Importação do Unfold
from .models import (
    Portfolio, Strategy, Trade, JournalNote, Tag,
    TradeEntry, TradeExit, PortfolioTransaction,
    TaxReport, Ticket
)

# --- Inlines (Tabelas dentro de tabelas) ---
# Usamos TabularInline do Unfold para ficar bonito


class TradeEntryInline(TabularInline):
    model = TradeEntry
    extra = 0
    tab = True  # Estilo em abas


class TradeExitInline(TabularInline):
    model = TradeExit
    extra = 0
    tab = True


class TransactionInline(TabularInline):
    model = PortfolioTransaction
    extra = 0
    tab = True

# --- Admins Principais (Herdam de ModelAdmin do Unfold) ---


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ('name', 'user', 'balance', 'currency', 'created_at')
    search_fields = ('name', 'user__username')
    inlines = [TransactionInline]


@admin.register(Strategy)
class StrategyAdmin(ModelAdmin):
    list_display = ('name', 'user')
    filter_horizontal = ('tags',)


@admin.register(Trade)
class TradeAdmin(ModelAdmin):
    list_display = ('id', 'symbol', 'side', 'status',
                    'net_result', 'user', 'created_at')
    list_filter = ('status', 'side', 'created_at')
    search_fields = ('symbol', 'user__username')
    inlines = [TradeEntryInline, TradeExitInline]

    fieldsets = (
        ('Identificação', {
            'fields': ('user', 'portfolio', 'strategy', 'symbol')
        }),
        ('Detalhes da Operação', {
            'fields': ('side', 'status')
        }),
        ('Resultado', {
            'fields': ('fees', 'net_result'),
            # 'classes': ('collapse',) # No Unfold o collapse é diferente, melhor deixar visível por enquanto
        }),
    )


@admin.register(TaxReport)
class TaxReportAdmin(ModelAdmin):
    list_display = ('__str__', 'net_profit', 'tax_due', 'is_paid')
    list_filter = ('is_paid', 'month')
    list_editable = ('is_paid',)


@admin.register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = ('id', 'subject', 'user', 'status', 'created_at')
    list_filter = ('status',)

# --- Registros Simples ---
# Para registros simples sem customização, pode usar o decorator direto ou criar classe


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass


@admin.register(JournalNote)
class JournalNoteAdmin(ModelAdmin):
    list_display = ('__str__', 'user', 'created_at')
