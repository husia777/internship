from django.shortcuts import  redirect

from .forms import MailingForm
from .models import MailSubscribedToTheNewsletter


def email_subscription(request):
    form = MailingForm(request.POST)
    if request.method == "POST" and form.is_valid():
        email = request.POST.get('email')
        MailSubscribedToTheNewsletter.objects.create(email=email)

    return redirect('home')
