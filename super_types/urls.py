from django.urls import path
from . import views

urlpatterns= [
    path('', views.supertype_list),
    path('', views.supertype_detail)
]