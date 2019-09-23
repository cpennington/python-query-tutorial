from django.contrib.auth.models import User, Group
from .models import Course, Organization, Instructor
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["url", "name", "instructors", "organizations"]
        depth = 1


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["url", "name", "course_set", "instructor_set"]
        depth = 1


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ["url", "name", "employer", "course_set"]
        depth = 1


class DashboardSerializer(serializers.ModelSerializer):
    instructors = InstructorSerializer(many=True, read_only=True)
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["url", "name", "instructors", "organizations"]
