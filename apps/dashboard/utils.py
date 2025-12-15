import requests
from datetime import timedelta
from django.utils import timezone


def get_ptax(date_obj):
    """
    Busca a PTAX de Venda do Banco Central para a data informada.
    Se for fim de semana ou feriado, recua dia a dia até achar (máx 5 dias).
    Retorna um Decimal ou None.
    """
    if not date_obj:
        return None

    # Garante que é um objeto date (remove horas se houver)
    if isinstance(date_obj, str):
        return None  # Deveria ser datetime ou date

    current_date = date_obj
    attempts = 0

    while attempts < 5:
        # Formato exigido pela API do BCB: 'MM-DD-YYYY'
        date_str = current_date.strftime("'%m-%d-%Y'")

        url = (
            f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            f"CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao={date_str}"
            f"&$top=1&$format=json&select=cotacaoVenda"
        )

        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                data = response.json()
                if data.get('value') and len(data['value']) > 0:
                    return data['value'][0]['cotacaoVenda']

            # Se não achou (feriado/fds), volta 1 dia
            current_date = current_date - timedelta(days=1)
            attempts += 1

        except Exception as e:
            print(f"Erro ao buscar PTAX: {e}")
            return None

    return None
