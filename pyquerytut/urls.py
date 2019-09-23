from django.urls import include, path
from rest_framework import routers
from pyquerytut.queries import views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r"users", views.raw.UserViewSet)
router.register(r"groups", views.raw.GroupViewSet)
router.register(r"courses", views.raw.CourseViewSet)
router.register(r"organizations", views.raw.OrganizationViewSet)
router.register(r"instructors", views.raw.InstructorViewSet)
router.register(r"dashboard/v1", views.dashboard.v1.DashboardViewSet)
router.register(r"dashboard/v2", views.dashboard.v2.DashboardViewSet)
router.register(r"dashboard/v3", views.dashboard.v3.DashboardViewSet)
router.register(r"dashboard/v4", views.dashboard.v4.DashboardViewSet)
router.register(r"dashboard/v5", views.dashboard.v5.DashboardViewSet)
router.register(r"dashboard/v6", views.dashboard.v6.DashboardViewSet)
router.register(
    r"dashboard/v7", views.dashboard.v7.DashboardViewSet, basename="dashboardv7"
)
router.register(
    r"dashboard/v8", views.dashboard.v8.DashboardViewSet, basename="dashboardv8"
)
router.register(
    r"dashboard/v9", views.dashboard.v9.DashboardViewSet, basename="dashboardv9"
)
router.register(
    r"subquery/v1", views.subquery.v1.SubQueryViewSet, basename="subqueryv1"
)
router.register(
    r"subquery/v2", views.subquery.v2.SubQueryViewSet, basename="subqueryv2"
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

