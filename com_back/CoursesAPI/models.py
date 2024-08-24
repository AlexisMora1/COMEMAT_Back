from django.db import models

class Course_List(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    # Otros campos necesarios

class Course_info(models.Model):
    course = models.ForeignKey(Course_List, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)
    modules_count = models.IntegerField()
    description = models.TextField()
    valuation = models.FloatField()
    # Otros campos necesarios

class Modules(models.Model):
    course_info = models.ForeignKey(Course_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_url = models.URLField()