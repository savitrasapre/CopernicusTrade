from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
import yfinance as yf
import pandas as pd
from .task import hello_world

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Account index.")

def trigger_task(request):
    try:
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
        symbol_data = yf.Ticker(symbol_name)
        #Only 8 days of 1m data is allowed at once.
        data_history = symbol_data.history(period="1mo", interval="1d")
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

        return JsonResponse({
                    'Message': 'History successfully retrieved!',
                    'history': json_data,
                }, status=200)

    except Exception as e:
        print(e)
        raise Http404({
                    'Message': 'Error in retrieving data!'
                })