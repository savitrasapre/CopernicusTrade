from django.http import JsonResponse, Http404
import yfinance as yf
from .task import hello_world
from Util.types import EUpdateType, EStrategyType
import logging

logging = logging.getLogger(__name__)

# Create your views here.
def index(request):
    try:
        print("In task")
        result = hello_world.delay()
        return JsonResponse({
            'Message': 'Triggered Task',
            'MessageID': result.id
        })
    except Exception as e:
        print(e)
        raise Http404({
            'Message': 'Error in triggering task!',
            'Error': e
        })

def update(request, symbol_name: str, strategy_type: str, update_type: EUpdateType):
    try:
        """
        TODO:
        - Fetch from database
        """
        if update_type == EUpdateType.CHART.value:
            if strategy_type == EStrategyType.MA.value:
                from .strategy.ma import MovingAverage
                strategy = MovingAverage(symbol_name)
                chart_data = strategy.run_strategy_logic()
                logging.info(f"Chart data for {symbol_name} retrieved successfully!")
                return JsonResponse({
                    'Message': 'Chart data successfully retrieved!',
                    'chart_data': chart_data,
                }, status=200)

    except Exception as e:
        logging.error(f"Error in retrieving data: {e}")
        raise Http404({
                    'Message': 'Error in retrieving data!'
                })