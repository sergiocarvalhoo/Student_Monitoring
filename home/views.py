from django.views.generic import TemplateView

from students.models import Student


# Create your views here.


class HomePageView(TemplateView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'home'
