import time
from celery import shared_task

@shared_task
def send_emails():
    for x in range(100):
        print(x)
        time.sleep(1)