from django.db import models

class TempEmail(models.Model):
    address = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class EmailMessage(models.Model):
    temp_email = models.ForeignKey(TempEmail, related_name='emailmessages', on_delete=models.CASCADE)
    sender = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender}, Subject: {self.subject}"
