from rest_framework.routers import DefaultRouter

from .viewsets import TopHeadlineViewSet

app_name = 'api'
router = DefaultRouter()
router.register(r'top_headlines', TopHeadlineViewSet)

urlpatterns = router.urls
