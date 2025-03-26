from celery import shared_task
from datetime import datetime
from .models import SymbolData
from CopernicusFE.utility_tasks import send_telegram_message
import logging

logger = logging.getLogger(__name__)

@shared_task
def hello_world():
    return "Hello World!"

@shared_task
def periodic_print():
    print("PERIODIC TASK - ", datetime.now())
    send_telegram_message("Hello World!")

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
        import yfinance as yf
        from .models import DefaultSymbols
        print("-- Getting chart bars --")
        #symbols = "AAPL"
        symbols = DefaultSymbols.objects.values_list('symbol_name', flat=True)

        for symbol in symbols:
            symbol_data = yf.Ticker(symbol)
            data_history = symbol_data.history(period="1mo", interval="1d")
            json_data = [
                {'x': index.strftime('%Y-%m-%d'), 'o': row['Open'], 'h': row['High'], 'l': row['Low'], 'c': row['Close']}
                for index, row in data_history.iterrows()
            ]
            if json_data:
                logger.info("-- Inserting in the database --")
                SymbolData.objects.update_or_create(
                    symbol_name=symbol,
                    defaults={'market_data': json_data, 'broker_name': 'yf', 'symbol_name': symbol}
                )
                send_telegram_message("Data fetched for " + symbol)
            else:
                logger.warning("Yfinance data not retrieved")
    except ImportError:
        logger.error("Yfinance not installed.")
    except Exception as e:
        logger.error(f"Error fetching chart bars: {e}")



        """
        from multiprocessing import Process
from celery import shared_task
import yfinance as yf

def fetch_symbol_data(symbol):
    try:
        print(f"Fetching data for {symbol}")
        symbol_data = yf.Ticker(symbol)
        data_history = symbol_data.history(period="1mo", interval="1d")
        # Process and store data (similar to your current logic)
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

@shared_task
def get_chart_bars_with_multiprocessing():
    symbols = ["AAPL", "GOOG", "MSFT"]  # Example list of symbols
    processes = []

    for symbol in symbols:
        process = Process(target=fetch_symbol_data, args=(symbol,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to complete
        """