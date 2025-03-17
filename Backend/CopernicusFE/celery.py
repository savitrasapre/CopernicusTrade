from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CopernicusFE.settings')

# Create Celery app instance
app = Celery('CopernicusFE')

# Load task-related settings from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and register tasks
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-three-hours': {
        'task': 'Util.symbol.Util.get_chart_bars',
        'schedule': crontab(minute="*/5"), #crontab(minute=0, hour='*/3')
        'args': ("1mo","1d")
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
