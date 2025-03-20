from django.http import JsonResponse, Http404
import yfinance as yf
from .task import hello_world

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
            'Message': 'Error in triggering task!'
        })

def update(request, symbol_name, update_type):
    try:
        """
        TODO:
        - Fetch from database
        """

        return JsonResponse({
                    'Message': 'Historical data successfully retrieved!',
                    #'history': json_data,
                }, status=200)

    except Exception as e:
        print(e)
        raise Http404({
                    'Message': 'Error in retrieving data!'
                })