from django.contrib import admin
from .models import *
print("Hola, mundo")
# Register your models here.

@admin.register(Cursos_Page)
class Cursos_Page_Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'image')

@admin.register(Curso_info)
class Curso_info_Admin(admin.ModelAdmin):
    list_display = ('course_id','des', 'opinions', 'valuation', 'count_mod')

@admin.register(Modules)
class Modules_Admin(admin.ModelAdmin):
    list_display = ('module_id', 'url')