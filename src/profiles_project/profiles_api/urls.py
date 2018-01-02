from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
#First param: name of api, Second param: name of viewset to assign to router,
#Third param: base_name
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')
#Do not need base class paramater for model viewset
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name = 'login')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    #Allows router to create url for us
    url(r'', include(router.urls))
]
