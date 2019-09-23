from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import viewsets
from bridgekeeper import perms
from ...serializers import DashboardSerializer
from ...models import Course, Organization, Instructor


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        courses = Course.objects.prefetch_related(
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

        return perms["queries.view_course"].filter(self.request.user, courses)

    serializer_class = DashboardSerializer
