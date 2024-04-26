from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerysetMixin():
    user_field = 'user'
    # this makes sure to set it to 'True' in all views you want to allow to view all queryset
    allow_staff_view = False

    def get_queryset(self):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        queryset = super().get_queryset()
        if self.allow_staff_view and user.is_staff:
            return queryset
        return queryset.filter(**lookup_data)
