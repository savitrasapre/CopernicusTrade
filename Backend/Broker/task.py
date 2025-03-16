from celery import shared_task
from datetime import datetime

@shared_task
def hello_world():
    return "Hello World!"


@shared_task
def periodic_print():
    print("PERIODIC TASK - ", datetime.now())
