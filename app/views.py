
from rest_framework import generics, viewsets

from .models import Student, Course, Mentor
from .serializers import StudentSerializer, MentorSerializer, CourseSerializer
from .my_generics import ListMixinAPI, CreateMixinAPI, UpdateMixinAPI, RetrieveMixinAPI, DeleteMixinAPI, MyAPIView


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MentorViewSet(ListMixinAPI, CreateMixinAPI,
                    UpdateMixinAPI, RetrieveMixinAPI,
                    DeleteMixinAPI, viewsets.ViewSetMixin, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
