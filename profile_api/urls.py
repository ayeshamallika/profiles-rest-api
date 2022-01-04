from django.urls import path

from profile_api import views

urlpatterns = [
    path('hello-view/',views.HellopApiView.as_view()),
]
