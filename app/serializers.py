from rest_framework import serializers

from .models import Course, Student, Mentor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Mentor


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Course
