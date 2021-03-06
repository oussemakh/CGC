from django.shortcuts import render,redirect
from .forms import contactform
from django.core.mail import send_mail
from .models import Contact
from django.conf import  settings 

# Create your views here.
def ContactView(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            subject = 'CSC'
            message = 'Thank you for sending a message we well replay so soon'
            email_from = settings.EMAIL_HOST_USER
            recipient = [form.cleaned_data['email']]
            send_mail(subject,message,email_from,recipient)
            
          
        return redirect('home')


    else:
        form = contactform()
    return render(request, 'contact.html', {'form':form})