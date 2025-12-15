from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PortfolioViewSet, StrategyViewSet, TradeViewSet,
    JournalNoteViewSet, TaxReportViewSet, TicketViewSet,
    ForexCalcView
)

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')
router.register(r'strategies', StrategyViewSet, basename='strategy')
router.register(r'trades', TradeViewSet, basename='trade')
router.register(r'journal', JournalNoteViewSet, basename='journal')
router.register(r'tax-reports', TaxReportViewSet, basename='tax-report')
router.register(r'support-tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
    path('tools/forex-calc/', ForexCalcView.as_view(), name='forex-calc'),
]
