from django.contrib import admin
from .models import *

@admin.register(Course_List)
class Course_List_Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'image')

@admin.register(Course_info)
class Course_info_Admin(admin.ModelAdmin):
    list_display = ('course_id','des', 'opinions', 'valuation', 'count_mod')

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ('module_id', 'url')