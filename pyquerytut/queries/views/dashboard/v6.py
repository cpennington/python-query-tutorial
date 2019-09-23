from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import viewsets
from ...serializers import DashboardSerializer
from ...models import Course, Organization, Instructor


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related(
        Prefetch(
            "instructors",
            queryset=Instructor.objects.select_related("employer").prefetch_related(
                "course_set", "course_set__instructors", "course_set__organizations"
            ),
        ),
        "organizations",
        "organizations__course_set",
        "organizations__course_set__instructors",
        "organizations__course_set__organizations",
        "organizations__instructor_set",
    ).all()
    serializer_class = DashboardSerializer
