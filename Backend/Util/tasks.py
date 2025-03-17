import yfinance as yf
from celery import shared_task
from ..Broker.models import SymbolData

@shared_task
def get_chart_bars(period: str, interval: str):
    """
    For multiple symbols, use whitespaced strings like so "AAPL GOOGL META"
    TODO:
    - Add symbol list to be fetched at the same time from a default list in db.
    - Data from different brokers can be fetched from.
    """
    try:
        print("-- Getting chart bars --")
        #Get default symbol list from db
        symbols: str = "AAPL"
        symbol_data: yf.Ticker = yf.Ticker(symbols)
        #Only 8 days of 1m data is allowed at once. period="1mo" interval="1d"
        data_history = symbol_data.history(period=period, interval=interval)
        json_data = [
            {
                'x': index.strftime('%Y-%m-%d'),
                'o': row['Open'],
                'h': row['High'],
                'l': row['Low'],
                'c': row['Close']
            }
            for index, row in data_history.iterrows()
        ]
        #put json_data in the SymbolData table.
        if json_data:
            SymbolData.objects.update_or_create(
                symbol_name=symbols,
                defaults={
                    'market_data' : json_data,
                    'broker_name' : 'yf',
                    'symbol_name' : symbols
                }
            )
        else:
            print("Yfinance data not retrieved")

    except Exception as e:
        print(e)