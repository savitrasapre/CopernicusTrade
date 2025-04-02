"""
IStrategy interface
Interface to apply for all strategies.
"""

from Util.types import EMarketDirection
from abc import ABC, abstractmethod
from ..models import SymbolData
import logging

logging = logging.getLogger(__name__)

class IStrategy(ABC):
    """Since interface is not a default type in python, we use abstract base classes"""

    """Initialize strategy with MA"""
    current_strategy: str
    current_symbol: str
    market_direction: EMarketDirection

    def __init__(self) -> None:
        """Initialize market direction to NONE for start."""
        self.market_direction = EMarketDirection['NONE'].value
        super().__init__()

    def load_symbol_data(self) -> dict:
        """"
        - TODO:
        - Add broker_name as another filter to the query.
        """
        try:
            dataframe: SymbolData = SymbolData.objects.get(symbol_name=self.current_symbol)
            logging.info(f"Loaded symbol data for {self.current_symbol} from the database.")
            return dataframe.market_data
        except SymbolData.DoesNotExist:
            logging.error(f"Symbol data not founr for {self.current_symbol}")
            raise ValueError(f"Symbol data for {self.current_symbol} not found in the database.")

    @abstractmethod
    def run_strategy_logic():
        pass    #implement strategy logic in subclass