from rest_framework import generics
from django.contrib.auth.models import User
from .models import Course, Enrollment
from .serializers import UserSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer



class EnrollView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')

        if not user_id or not course_id:
            return Response(
                {"error": "user_id and course_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Enrollment.objects.filter(user_id=user_id, course_id=course_id).exists():
            return Response(
                {"error": "User already enrolled"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Enrollment.objects.create(user_id=user_id, course_id=course_id)

        return Response(
            {"message": "Enrollment successful"},
            status=status.HTTP_201_CREATED
        )


class UnenrollView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')

        enrollment = Enrollment.objects.filter(
            user_id=user_id,
            course_id=course_id
        ).first()

        if not enrollment:
            return Response(
                {"error": "Enrollment not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        enrollment.delete()

        return Response(
            {"message": "Unenrollment successful"},
            status=status.HTTP_200_OK
        )
        
        
        
class UserCoursesView(APIView):
    def get(self, request, user_id):
        enrollments = Enrollment.objects.filter(user_id=user_id)
        courses = [enrollment.course for enrollment in enrollments]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    
class CourseStudentsView(APIView):
    def get(self, request, course_id):
        enrollments = Enrollment.objects.filter(course_id=course_id)
        users = [enrollment.user for enrollment in enrollments]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

