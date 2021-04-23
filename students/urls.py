from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import never_cache

from .views import (
    ListStudentsView,
    DetailStudentView,
    CreateStudentView,
    UpdateStudentView,
    DeleteStudentView,
)

urlpatterns = [
    path('ifpb/students/', never_cache(login_required(ListStudentsView.as_view())), name='list_students'),
    path('ifpb/student/<int:pk>/', never_cache(login_required(DetailStudentView.as_view())), name='detail_student'),
    path('ifpb/student/new/student/', login_required(CreateStudentView.as_view()), name='add_student'),
    path('ifpb/<int:pk>/update/', never_cache(login_required(UpdateStudentView.as_view())), name='update_student'),
    path('ifpb/<int:pk>/delete/', never_cache(login_required(DeleteStudentView.as_view())), name='delete_student'),
]
