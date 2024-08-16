from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/saludar', Course_List_DB.as_view())
]