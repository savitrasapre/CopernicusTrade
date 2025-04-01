from Util.types import StrategyType

class Strategy():

    def __init__(self, strategy_name=StrategyType(2).name):
        """Initialize strategy with MA"""
        self.current_strategy = strategy_name

    def run_strategy(self):
        """Run the default strategy on the bars that are in the database"""

        #run_strategy_logic(with_loaded_data)
    
