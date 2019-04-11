from rest_framework import routers


from meetup.api.views import SpeakerViewSet, SubjectViewSet, SubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'palestrantes', SpeakerViewSet)
router.register(r'temas', SubjectViewSet)
router.register(r'inscricoes', SubscriptionViewSet)
