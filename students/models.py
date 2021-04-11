from django.db import models
from django.urls import reverse

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    registration = models.IntegerField()
    course = models.CharField(max_length=30)
    situation = models.CharField(max_length=30)

    # def get_absolute_url(self):
    #     return reverse('list_student', args=[str(self.id)])

    def __str__(self):
        return self.name[:40]
