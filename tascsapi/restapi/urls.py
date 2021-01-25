from django.urls import include, path
from rest_framework import routers

from . import views
from .views import TaskViewSet, LoginView

router = routers.DefaultRouter()
router.register('tascs', TaskViewSet)
router.register('registration', views.UserCreate)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name="login"),
]
