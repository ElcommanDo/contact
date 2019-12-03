from django.shortcuts import render, HttpResponseRedirect
from .forms import MessageForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' dear {}  your message sent successfully . we will mail you in reciveing email address '.format(form.cleaned_data['name']))
            print(form.cleaned_data)
            message = 'thank ou for send us your message is recieved successfully and the replay through 24 hours'
            send_mail('thank you for mailing us',message,'adamweldadam@gmail.com',[form.cleaned_data['Email']])
            return HttpResponseRedirect('/') 
    else:
        form = MessageForm()


    return render(request,'support/contact.html',{'form':form})