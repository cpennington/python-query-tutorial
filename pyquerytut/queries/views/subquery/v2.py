from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import viewsets
from bridgekeeper import perms
from ...serializers import InstructorSerializer
from ...models import Course, Organization, Instructor


class SubQueryViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        mit = Organization.objects.filter(name="MITx")[:1]
        courses = Course.objects.filter(organizations=mit)
        faculty = Instructor.objects.filter(course__in=courses)

        return faculty

    serializer_class = InstructorSerializer
