from django.urls import path
from .views import (
    UserListView,
    CourseListCreateView,
    CourseDetailView,
    EnrollmentListView,
    EnrollView,
    UnenrollView,
    CourseStudentsView,
     UserCoursesView,
)

urlpatterns = [
    path('users/', UserListView.as_view()),

    path('courses/', CourseListCreateView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),
    path('courses/<int:course_id>/students/', CourseStudentsView.as_view()),

    path('enrollments/', EnrollmentListView.as_view()),
    path('enroll/', EnrollView.as_view()),
    path('unenroll/', UnenrollView.as_view()),
    
    
    
    path('users/<int:user_id>/courses/', UserCoursesView.as_view()),
]
