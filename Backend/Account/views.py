from django.http import HttpResponse, Http404, JsonResponse
from .models import User, Token
from .utils.jwt import generate_token

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
        #Should block after creating / getting user
        token_h256: str = generate_token(new_user)
        print("Token created %s" % token_h256)
        if created:
            token_entry: Token = Token.objects.create(user=new_user, token=token_h256)
        else:
            token_entry: Token = Token.objects.get(user=new_user, token=token_h256)
        print("token created at %s" % token_entry.created_at)
        
        if created:
            return JsonResponse({
                'Message': 'User successfully created!',
                'BearerToken': token_entry.token,
            }, status=200)
        else:
            return JsonResponse({
                'Message': 'User already exists!',
                'BearerToken': token_entry.token,
            }, status=200)
        
    except Token.DoesNotExist:
        raise Http404("Hello, this is user signup exception")
    
def echo(request, echo_str):
    return HttpResponse("Echo response! %s" % echo_str)