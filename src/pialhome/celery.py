from celery import Celery
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pialhome.settings")

app = Celery('pialhome')
app.config_from_object(
    'django.conf:settings', 
    namespace='CELERY'
)
app.autodiscover_tasks()