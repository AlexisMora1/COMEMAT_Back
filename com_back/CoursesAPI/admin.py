from django.contrib import admin
from .models import *

@admin.register(Course_List)
class Course_List_Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'image')

@admin.register(Course_info)
class Course_info_Admin(admin.ModelAdmin):
    list_display = ('course','description', 'valuation', 'modules_count', 'created_by')

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ('course_info', 'video_url', 'name')