from enum import Enum

class EStrategyType(Enum):
    RSI = "rsi"
    MA = "ma"
    #MACD = 2


class EMarketDirection(Enum):
    LONG = "long"
    SHORT = "short"
    NONE = "none"

class EUpdateType(Enum):
    CHART = "chart"