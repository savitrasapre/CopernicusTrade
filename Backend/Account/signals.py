from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Token
from .utils.jwt import generate_token

#@receiver(post_save, sender=User)
def user_post_create(sender, instance, created, **kwargs):
    if created:
        try:
            #generate JWT and save in Token database
            token_h256 = generate_token(instance)
            print("Token created %s" % token_h256)
            token_entry, token_created = Token.objects.get_or_create(user=instance, token=token_h256)
            print("sender id is %s" % token_entry.created_at)
        except Exception as e:
            print("Error in creating token %s" % e)