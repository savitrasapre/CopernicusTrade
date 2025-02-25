import jwt
from django.conf import settings


def generate_token(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'username': user.username,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    print(token)
    return token