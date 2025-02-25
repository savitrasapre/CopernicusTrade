from django.http import HttpResponse, Http404, JsonResponse
from .models import User
from django.dispatch import Signal

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Account index.")

def login(request, username, password_hash):
    return HttpResponse("Hello, this will be on user login")

def register(request, username, email, password_hash):
    try:
        #check if request is valid or not.
        new_user, created = User.objects.get_or_create(
            username=username, 
            password_hash=password_hash, 
            email=email
        )
        # block till token is created / saved.
        if created:
            Signal.send(sender=new_user)
            return JsonResponse({
                'Message': 'User successfully created!' 
            })
        else:
            return JsonResponse({
                'Message': 'Error in saving user'
            })
        
    except User.DoesNotExist:
        raise Http404("Hello, this is user signup exception")
    
def echo(request, echo_str):
    return HttpResponse("Echo response! %s" % echo_str)