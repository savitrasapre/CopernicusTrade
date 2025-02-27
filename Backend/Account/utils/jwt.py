import jwt
from datetime import datetime
from django.conf import settings


def generate_token(user):
    payload = {
        #'iat': datetime.now(),
        #'exp': datetime.now() + settings.JWT_EXPIRATION_DELTA,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    print(token)
    return token