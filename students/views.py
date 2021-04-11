from django.views.generic import ListView
from students.models import Student


# Create your views here.


class HomePageView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'
