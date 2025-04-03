from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.MRI_list, name='MRIList'),
    path('create/', views.MRI_create, name='MRICreate'),
]