from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-veiwset')

urlpatterns = [
    path('hello-view/',views.HellopApiView.as_view()),
    path('', include(router.urls))

]
