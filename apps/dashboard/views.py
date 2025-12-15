from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum

from .models import (
    Portfolio, Strategy, Trade, JournalNote, Tag,
    TaxReport, Ticket, PortfolioTransaction
)
from .serializers import (
    PortfolioSerializer, StrategySerializer, TradeSerializer,
    JournalNoteSerializer, TagSerializer, TaxReportSerializer,
    TicketSerializer, TransactionSerializer
)

# --- ViewSets Padrão (CRUD) ---


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_transaction(self, request, pk=None):
        """Endpoint para Depósito/Saque dentro do Portfolio"""
        portfolio = self.get_object()
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(portfolio=portfolio)
            # Aqui você poderia adicionar lógica para atualizar o saldo do portfolio
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StrategyViewSet(viewsets.ModelViewSet):
    serializer_class = StrategySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Strategy.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trade.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JournalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = JournalNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalNote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --- Funcionalidades Especiais do PDF ---


class TaxReportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Visualização dos relatórios de imposto gerados automaticamente.
    Permite apenas marcar como pago.
    """
    serializer_class = TaxReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TaxReport.objects.filter(user=self.request.user).order_by('-month')

    @action(detail=True, methods=['patch'])
    def mark_paid(self, request, pk=None):
        report = self.get_object()
        report.is_paid = True
        report.save()
        return Response({'status': 'paid'})


class TicketViewSet(viewsets.ModelViewSet):
    """Sistema de Suporte"""
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --- Utilitários (Calculadora Forex) ---


class ForexCalcView(APIView):
    """
    Endpoint para calcular risco/retorno de Forex (Sem salvar no banco).
    Recebe: entry_price, stop_loss, risk_amount
    Retorna: position_size (lotes)
    """
    permission_classes = [permissions.AllowAny]  # Pode ser pública ou não

    def post(self, request):
        try:
            entry = float(request.data.get('entry_price'))
            stop = float(request.data.get('stop_loss'))
            # Dinheiro que aceita perder (ex: $100)
            risk = float(request.data.get('risk_amount'))

            if entry == stop:
                return Response({'error': 'Entry e Stop não podem ser iguais'}, status=400)

            # Cálculo básico de pips (simplificado para pares USD padrão)
            pip_value = 0.0001  # Para maioria dos pares (exceto JPY)
            stop_pips = abs(entry - stop) / pip_value

            # Valor por pip por lote standard ($10/pip no EURUSD)
            # Fórmula: Risco / (Stop_Pips * Valor_Pip_Standard)
            # Simplificando: Lotes = Risco / Distancia_Preço / 100000 (aprox)

            distance = abs(entry - stop)
            position_size = risk / distance

            return Response({
                'risk_amount': risk,
                'stop_distance_price': distance,
                'suggested_units': position_size,  # Unidades da moeda base
                'suggested_lots': position_size / 100000  # Lotes Standard
            })
        except (TypeError, ValueError):
            return Response({'error': 'Dados inválidos'}, status=400)
