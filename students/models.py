from django.db import models
from django.urls import reverse

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    registration = models.IntegerField()
    campus = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    situation = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('detail_student', args=[str(self.id)])

    def __str__(self):
        return self.name[:40]
