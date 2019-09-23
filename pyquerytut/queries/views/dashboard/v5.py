from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ...serializers import DashboardSerializer
from ...models import Course, Organization, Instructor


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related(
        "instructors",
        "instructors__course_set",
        "instructors__course_set__instructors",
        "instructors__course_set__organizations",
        "instructors__employer",
        "organizations",
        "organizations__course_set",
        "organizations__course_set__instructors",
        "organizations__course_set__organizations",
    ).all()
    serializer_class = DashboardSerializer
