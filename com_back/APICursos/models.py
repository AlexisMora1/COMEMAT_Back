from django.db import models

# Create your models here.
class Cursos_Page(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    

class Curso_info(models.Model):
    course_id = models.ForeignKey(Cursos_Page, on_delete=models.CASCADE, related_name='course_id')
    des = models.CharField(max_length=350)
    opinions = models.CharField(max_length=250)
    valuation = models.FloatField()
    count_mod = models.IntegerField()


class Modules(models.Model):
    module_id = models.ForeignKey('Curso_info', on_delete=models.CASCADE)
    url = models.URLField()
