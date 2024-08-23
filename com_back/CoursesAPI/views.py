from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course_List, Course_List, Modules
from .serializers import CourseListSerializer, CourseInfoSerializer, ModulesSerializer

class CourseListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course_List.objects.all()
    serializer_class = CourseListSerializer

class CourseInfoViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        try:
            Course_List = Course_List.objects.get(course_id=pk)
            serializer = CourseInfoSerializer(Course_List)
            return Response(serializer.data)
        except Course_List.DoesNotExist:
            return Response(status=404)

    @action(detail=True, url_path='module=(?P<module_id>[^/.]+)')
    def module(self, request, pk=None, module_id=None):
        try:
            module = Modules.objects.get(id=module_id, course_info__course_id=pk)
            serializer = ModulesSerializer(module)
            return Response(serializer.data)
        except Modules.DoesNotExist:
            return Response(status=404)
