import yfinance as yf
from celery import shared_task
from ..Broker.models import SymbolData
import logging

logger = logging.getLogger(__name__)

@shared_task
def get_chart_bars():
    try:
        print("-- Getting chart bars --")
        symbols = "AAPL"
        symbol_data = yf.Ticker(symbols)
        data_history = symbol_data.history(period="1mo", interval="1d")
        json_data = [
            {'x': index.strftime('%Y-%m-%d'), 'o': row['Open'], 'h': row['High'], 'l': row['Low'], 'c': row['Close']}
            for index, row in data_history.iterrows()
        ]
        if json_data:
            SymbolData.objects.update_or_create(
                symbol_name=symbols,
                defaults={'market_data': json_data, 'broker_name': 'yf', 'symbol_name': symbols}
            )
        else:
            logger.warning("Yfinance data not retrieved")
    except Exception as e:
        logger.error(f"Error fetching chart bars: {e}")