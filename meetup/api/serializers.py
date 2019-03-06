from rest_framework import serializers

from meetup.core.models import Speaker, Subject
from meetup.subscriptions.models import Subscription


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = (
            'id',
            'name',
            'slug',
            'photo',
            'website',
            'twitter',
            'facebook',
            'instagram',
            'description'
        )


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
            'slug',
            'title',
            'subtitle',
            'description',
            'icon'
        )


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'name',
            'email'
        )
