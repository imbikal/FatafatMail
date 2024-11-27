from celery import shared_task
from .models import TempEmail
from django.utils.timezone import now
from datetime import timedelta

@shared_task
def delete_expired_emails():
    # Delete TempEmail objects that are older than 10 minutes
    TempEmail.objects.filter(created_at__lt=now() - timedelta(minutes=10)).delete()

