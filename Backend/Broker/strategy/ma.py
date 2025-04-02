from .strategy import IStrategy
from Util.types import EStrategyType
import logging

logging = logging.getLogger(__name__)

class MovingAverage(IStrategy):
    """"
    Moving Average strategy class.
    This class implements the IStrategy interface and provides methods to run a moving average strategy.
    """
    def __init__(self, symbol_name: str):
        self.current_strategy = EStrategyType['MA'].value
        self.current_symbol = symbol_name
        self.market_direction = EStrategyType['NONE'].value
    
    def calculate_average(self) -> dict:
        try:
            symbol_df: dict = self.load_symbol_data()
            if symbol_df is None:
                logging.error(f"Symbol data is not found")
            
            current_sum = 0
            for item in symbol_df:
                closing_price = item["c"]
                current_sum += closing_price
                item["avg"] = current_sum / (len(symbol_df) + 1)
            
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
