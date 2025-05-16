from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'phone',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'get_groups',
        'get_user_permissions',
    )

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = "Groups"

    def get_user_permissions(self, obj):
        return ", ".join([perm.name for perm in obj.user_permissions.all()])
    get_user_permissions.short_description = "Permissions"