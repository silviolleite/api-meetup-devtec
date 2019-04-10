from rest_framework import viewsets, mixins

from meetup import settings
from meetup.api.serializers import SpeakerSerializer, SubjectSerializer, SubscriptionSerializer
from meetup.core.models import Speaker, Subject
from meetup.subscriptions.models import Subscription
from django.core import mail
from django.template.loader import render_to_string


class SampleViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubscriptionViewSet(SampleViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        self._send_mail(
            'Confirmação de inscrição',
            settings.DEFAULT_FROM_EMAIL,
            serializer.data['email'],
            'subscriptions/subscription_email.txt',
            {'name': serializer.data['name'], 'email': serializer.data['email']}
           )

    def _send_mail(self, subject, from_, to, template_name, context):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, [from_, to])
