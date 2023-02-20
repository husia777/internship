from django import forms
from mailing.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class: field newsletter-section__email-field'})
        }
