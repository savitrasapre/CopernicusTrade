from celery import shared_task
from .models import SymbolData
import logging
import time
from Util.utility import Utility

logger = logging.getLogger(__name__)

@shared_task
def hello_world():
    return "Hello World!"

@shared_task
def symbol_data_count():
    logger.debug("Count is --",SymbolData.objects.count())

@shared_task
def get_chart_bars():
    """
    TODO:
    - Default string for symbols should come from the database.
    - Formatting for telegram message should be allowed in send_telegram_message function
    """
    try:
        from .models import DefaultSecurity
        from threading import Thread

        print("-- Getting chart bars --")
        threads = []
        symbols = DefaultSecurity.objects.values_list('symbol_name', flat=True)
        logger.info(f"Symbols: {symbols}")

        for symbol in symbols:
            Utility.fetch_historical_symbol_data(symbol)
            time.sleep(5)

    except Exception as e:
        logger.error(f"Error fetching chart bars: {e}")