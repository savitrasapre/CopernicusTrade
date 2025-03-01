import jwt
from datetime import datetime, timedelta
from Account.models import User
from django.conf import settings


def generate_token(user: User):
    payload = {
        "sub": str(user.id),
        'iat': datetime.now().timestamp(),
        'exp': datetime.timestamp(datetime.now() + timedelta(days=settings.JWT_EXPIRATION_DELTA)),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token