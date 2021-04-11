from django.urls import path

from .views import (
    HomePageView,
    ListStudentsView,
    DetailStudentView,
    CreateStudentView,
    UpdateStudentView,
    DeleteStudentView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ifpb/students/', ListStudentsView.as_view(), name='list_students'),
    path('ifpb/student/<int:pk>/', DetailStudentView.as_view(), name='detail_student'),
    path('ifpb/student/new/student/', CreateStudentView.as_view(), name='add_student'),
    path('ifpb/<int:pk>/update/', UpdateStudentView.as_view(), name='update_student'),
    path('ifpb/<int:pk>/delete/', DeleteStudentView.as_view(), name='delete_student'),
]
