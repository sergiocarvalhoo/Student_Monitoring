from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student


# Create your views here.


class ListStudentsView(ListView):
    model = Student
    template_name = 'list_students.html'
    context_object_name = 'students'


class DetailStudentView(DetailView):
    model = Student
    template_name = 'detail_student.html'
    context_object_name = 'student'


class CreateStudentView(CreateView):
    model = Student
    template_name = 'add_student.html'
    fields = ['name', 'registration', 'course', 'situation']


class UpdateStudentView(UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = ['registration', 'course', 'situation']


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('list_students')
