from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
#Do not need base class paramater for model viewset
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name = 'login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    #Allows router to create url for us
    url(r'', include(router.urls))
]
