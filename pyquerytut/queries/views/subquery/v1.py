from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import viewsets
from bridgekeeper import perms
from ...serializers import InstructorSerializer
from ...models import Course, Organization, Instructor


class SubQueryViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        mit = Organization.objects.get(name="MITx")
        courses = Course.objects.filter(organizations__id=mit.id)
        faculty = Instructor.objects.filter(
            course__id__in=[course.id for course in courses]
        )

        return faculty

    serializer_class = InstructorSerializer
