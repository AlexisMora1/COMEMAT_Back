from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course_List, Course_List, Modules
from .serializers import CourseListSerializer, CourseInfoSerializer, ModulesSerializer

class CourseListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course_List.objects.all()
    serializer_class = CourseListSerializer

class CourseInfoViewSet(viewsets.ViewSet):
    #   Configuring GET method
    def retrieve(self, request, pk=None):
        try:
            Course_List_1 = Course_List.objects.get(course_id=pk)
            serializer = CourseInfoSerializer(Course_List_1)
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
    
    # Configuring POST method
    def create(self, request):
        # Extracting data from request
        course_list_data = request.data.get('page_data')
        course_info_data = request.data.get('course_info')
        modules_data = request.data.get('course_modules')

        # Parsing course_list data with serializer and saving into db
        course_list_serializer = CourseListSerializer(data=course_list_data)
        course_list_serializer.is_valid(raise_exception=True)
        course = course_list_serializer.save()

        # Doing the same for course_info table
        course_info_data['course'] = course.id
        course_info_serializer = CourseInfoSerializer(data = course_info_data)
        course_info_serializer.is_valid(raise_exception=True)
        course_info = course_info_serializer.save()

        # Now lets save modules information
        for module in modules_data:
            module['course_info'] = course_info.id
            module_serializer = ModulesSerializer(data = module)
            module_serializer.is_valid(raise_exception=True)
            final_module = module_serializer.save()

        return Response(course_list_serializer.data, status= 201)



