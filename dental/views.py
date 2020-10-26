from django.shortcuts import render
from django.core.mail import  send_mail


def home(request):

    return render(request, "dental/home.html", {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, # message
            message_email, #from email
            ['sh.danishyar@gmail.com'], # to email
            fail_silently=False
        )
        context = {
            'message_name': message_name
        }
        return render(request, "dental/contact.html", context)
    else:
        return render(request, "dental/contact.html", {})

    