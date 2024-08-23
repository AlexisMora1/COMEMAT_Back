from rest_framework import serializers
from .models import *

class CursoPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos_Page
        fields = '__all__'

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules

class CursoInfoSerializer(serializers.ModelSerializer):
    modules = ModulesSerializer(many=True)
    class Meta: 
        model = Curso_info
        fields = '__all__'
    
    def create(self, validated_data):
        modules_data = validated_data.pop('modules')
        course_info = Curso_info.objects.create(**validated_data)
        for module_data in modules_data:
            Modules.objects.create(course_info=course_info, **module_data)
        return course_info
