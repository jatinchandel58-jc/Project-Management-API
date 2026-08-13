from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkspaceViewSet, CreateMemberView,  GetMemberView


router = DefaultRouter()

router.register(
    "workspace",
    WorkspaceViewSet,
    basename="workspace"
)


urlpatterns = [
    path("", include(router.urls)),
    path("create/member/", CreateMemberView.as_view()),
    path("workspace/<int:workspace_id>/member/", CreateMemberView.as_view()),
    path("workspace/<int:workspace_id>/member/<int:member_id>/", GetMemberView.as_view())
]