from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Token
from .utils.jwt import generate_token

@receiver(post_save, sender=User)
def user_post_create(sender, instance, created, **kwargs):
    if created:
        try:
            #generate JWT and save in Token database
            create_token_entry = generate_token(instance)
            print("Token created %s" % create_token_entry)
            Token.objects.get_or_create(user_id=sender, token='token') 

            print("sender id is %s %s" % sender.id, create_token_entry.token)
        except Exception as e:
            print("Error in creating token %s" % e)
