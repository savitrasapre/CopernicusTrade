from celery import shared_task
from .models import SymbolData
import logging
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
        from .models import DefaultSecurities
        from multiprocessing import Process

        print("-- Getting chart bars --")
        processes = []
        symbols = DefaultSecurities.objects.values_list('symbol_name', flat=True)

        for symbol in symbols:
            process = Process(target=Utility.fetch_historical_symbol_data, args=(symbol))
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
    except Exception as e:
        logger.error(f"Error fetching chart bars: {e}")