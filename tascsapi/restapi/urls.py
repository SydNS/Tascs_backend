from django.urls import include, path
from rest_framework import routers

from . import views
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register('', TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]