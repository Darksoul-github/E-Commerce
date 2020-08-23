from django.shortcuts import render
from Nav2.settings import *
from django.core.mail import send_mail
from subscribe.forms import *

# Create your views here.
def email(request):
    form=EmailForm()
    if request.method=='POST':
        form=EmailForm(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(form['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':form})
