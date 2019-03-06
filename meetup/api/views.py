from rest_framework import viewsets, mixins

from meetup.api.serializers import SpeakerSerializer, SubjectSerializer, SubscriptionSerializer
from meetup.core.models import Speaker, Subject
from meetup.subscriptions.models import Subscription


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
