from celery import shared_task
from CopernicusFE.celery import app
from datetime import datetime

@shared_task
def hello_world():
    return "Hello World!"


@app.task
def periodic_print():
    print("PERIODIC TASK - ", datetime.now())
