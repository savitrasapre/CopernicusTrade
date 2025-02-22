from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Account index.")

def login(request, username, password_hash):
    return HttpResponse("Hello, this will be on user login")

def register(request, username, email, password_hash):
    return HttpResponse("Hello, this is user signup and account creation")

def echo(request, echo_str):
    return HttpResponse("Echo response! %s" % echo_str)