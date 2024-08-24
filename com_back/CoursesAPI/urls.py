from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CourseListViewSet, CourseInfoViewSet

router = DefaultRouter()
router.register(r'courses', CourseListViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('courses/newcourse', CourseInfoViewSet.as_view({'post':'create'})),
    path('courses/<int:pk>/info', CourseInfoViewSet.as_view({'get': 'retrieve'})),
    path('courses/<int:pk>/', include([
        path('', CourseInfoViewSet.as_view({'get': 'retrieve'})),
        path('module=<int:module_id>', CourseInfoViewSet.as_view({'get': 'module'})),
    ])),
]
