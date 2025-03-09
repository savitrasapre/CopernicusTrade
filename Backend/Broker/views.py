from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Account index.")

def update(request, symbol_name, update_type):
    # try:
        
    # except: