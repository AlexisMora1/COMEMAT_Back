from rest_framework import serializers
from .models import Course_List, Course_info, Modules

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_List
        fields = '__all__'

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'

class CourseInfoSerializer(serializers.ModelSerializer):
    modules = ModulesSerializer(many=True, read_only=True, source='modules_set')

    class Meta:
        model = Course_info
        fields = '__all__'
