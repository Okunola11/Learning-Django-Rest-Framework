from rest_framework import permissions

# This is to override DjangoModelPermissions to include the view('GET') method as it was excluded.
# Go to the class definition, copy out perms_map and paste
# Add permission to the 'GET' method


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],  # Permission added
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # Extra layer of custom permissions that can be done

    # def has_permission(self, request, view):
    #     if not request.user.username == 'Waasi':
    #         return False
    #     if not request.user.is_staff:  # checking IsAdmin in views will do the same as this
    #         return False
    #     return super().has_permission(request, view)

#####################################################################################################
################## This is a flawed method which does not do the permissions effectively #############
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         # format to check permissions - 'app_name.action_model_name
    #         if user.has_perm('products.add_product'):
    #             return True
    #         if user.has_perm('products.view_product'):
    #             return True
    #         if user.has_perm('products.change_product'):
    #             return True
    #         if user.has_perm('products.delete_product'):
    #             return True
    #         return False
    #     return False
