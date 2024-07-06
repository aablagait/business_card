from django.urls import path

from . import views


app_name = 'me'

urlpatterns = [
    path('', views.NewMe.as_view(), name='newme')
]