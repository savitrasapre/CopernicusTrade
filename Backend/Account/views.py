from django.http import HttpResponse, Http404, JsonResponse
from .models import User, Token
from .utils.jwt import generate_token
from django.views import View

class AccountView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the Account index.")

class LoginView(View):
    def get(self, request, username: str, password_hash: str):
        try:
            user: User = User.objects.get(username=username, password_hash=password_hash)
            
            if user.id:
                new_token: Token = Token.objects.create(user=user, token=generate_token(user))
                if new_token.id:
                    return JsonResponse({
                        'Message': 'User successfully logged in!',
                        'BearerToken': new_token.token,
                    }, status=200)
                else:
                    raise Http404({
                        'Message': 'Error in creating token!'
                    })
        
        except User.DoesNotExist:
            print("Please enter a valid username and password")
            raise Http404({
                'Message': 'Please enter a valid username and password'
            })
        
class RegisterView(View):
    def post(self, request, username: str, email: str, password_hash: str):
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