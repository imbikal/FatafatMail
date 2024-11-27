import random
import string
from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from .models import TempEmail, EmailMessage

def generate_email(request):
    try:
        while True:
            # Generate a random temporary email address
            random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@fatafatmail.com"
            temp_email, created = TempEmail.objects.get_or_create(address=random_email)
            if created:
                break
    except IntegrityError:
        return render(request, "emailapp/error.html", {"message": "Could not generate a unique email. Please try again."})

    # Now, pass the email object along with its ID to the template
    return render(request, "emailapp/home.html", {"email": temp_email})

def view_inbox(request, email_id):
    # Get the TempEmail object
    temp_email = get_object_or_404(TempEmail, id=email_id)
    
    # Fetch the related email messages (you can customize based on your relationship model)
    emails = temp_email.emailmessages.all()
    
    return render(request, 'emailapp/inbox.html', {'emails': emails, 'email': temp_email})

def delete_email(request, email_id):
    # Get the email to delete
    email = get_object_or_404(EmailMessage, id=email_id)
    email.delete()
    
    return redirect('view_inbox', email_id=email.temp_email.id)  # Redirect back to the inbox
