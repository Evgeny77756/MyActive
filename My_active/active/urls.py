from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('action_list/', views.action_list, name='stock'),
    path('registration/', views.registration, name='registrations'),
]

