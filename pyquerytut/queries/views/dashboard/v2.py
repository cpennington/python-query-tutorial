from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ...serializers import DashboardSerializer
from ...models import Course, Organization, Instructor


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related("instructors", "organizations").all()
    serializer_class = DashboardSerializer
