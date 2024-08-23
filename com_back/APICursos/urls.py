from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'courses',CursosPageViewSet)

urlpatterns = [
    # path('v1/saludar', Course_List_DB.as_view())
    path('',include(router.urls)),
    path('courses/<int:course_id>/info/',CursoInfoViewSet.as_view({'get':'list','post':'create'})),
    path('courses/info/<int:pk>/', CursoInfoViewSet.as_view({'get': 'list'})),
]