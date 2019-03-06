from django import forms
from meetup.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'email']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.title()
