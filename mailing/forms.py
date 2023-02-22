from django import forms

from .models import MailSubscribedToTheNewsletter


class MailingForm(forms.ModelForm):
    class Meta:
        model = MailSubscribedToTheNewsletter
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'field'})
        }




