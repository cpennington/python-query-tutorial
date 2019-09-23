from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ..serializers import (
    UserSerializer,
    GroupSerializer,
    CourseSerializer,
    OrganizationSerializer,
    InstructorSerializer,
    DashboardSerializer,
)
from ..models import Course, Organization, Instructor


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Organizations to be viewed or edited.
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instructors to be viewed or edited.
    """

    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = DashboardSerializer
