from .strategy import IStrategy
from Util.types import EStrategyType, EMarketDirection
import logging

logging = logging.getLogger(__name__)

class MovingAverage(IStrategy):
    """"
    Moving Average strategy class.
    This class implements the IStrategy interface and provides methods to run a moving average strategy.
    """
    def __init__(self, symbol_name: str):
        try:
            self.current_strategy = EStrategyType.MA.value
            self.current_symbol = symbol_name
            self.market_direction = EMarketDirection.NONE.value
        except Exception as e:
            logging.error(f"Error initializing MovingAverage strategy: {e}")
            raise e
    
    def calculate_average(self):
        try:
            symbol_df = self.load_symbol_data()
            if symbol_df is None:
                logging.error(f"Symbol data is not found")
            
            current_sum = 0
            for idx, item in enumerate(symbol_df, start=1):
                closing_price = item[2] # Assuming the closing price is at index 2
                current_sum += closing_price
                item.append(current_sum / idx)
            
            #return new dict with avg price
            return symbol_df
        except Exception as e:
            logging.error(f"Error in calculating average: {e}")
            raise e
            

    def run_strategy_logic(self):
        try:
            #Load the list of cumulative average price
            chart_data_with_avg_price = self.calculate_average()
            logging.info(f"Chart data with average price for {self.current_symbol} retrieved successfully!")
            #returning the dictionary with average price for now.
            return chart_data_with_avg_price
        except Exception as e:
            logging.error(f"Error in running strategy logic: {e}")
            raise e
