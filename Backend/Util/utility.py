import logging
from CopernicusFE.utility_tasks import send_telegram_message
from Broker.models import SymbolData

logger = logging.getLogger(__name__)

class Utility():
    def __init__(self):
        pass

    @staticmethod
    def fetch_historical_symbol_data(self, symbol: str):
        """
        Fetches data for a given symbol from yfinance and saves it in the database.
        """
        try:
            import yfinance as yf
            print(f"Fetching data for {symbol}")
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
            logger.exception("yfinance not found")
        except Exception as e:
            logger.exception(f"Error fetching data for {symbol}: {e}")