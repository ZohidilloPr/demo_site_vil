
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm

Users = get_user_model()
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = Users

    list_display = [ 'username', 'full_name','joined_date']
    list_filter = ('full_name', 'phone_number', 'username',)

    fieldsets = (
        (None, {
            "fields": (
                'full_name', 'username', 'password',
            ),
        }),
        ('Permisssions',{
            "fields":(
                'is_active','staff', 'superuser', 'data_viewer',
            )
        })
    )
    readonly_fields = ['joined_date']
    add_fieldsets = (
        (None, {
            "classes":("wide", ),
            "fields": ["username", "password", "password2", "is_active", "superuser", "staff", "data_viewer"]
        })
    )

    search_fields = ("username", "full_name", "phone_number", "staff", "superuser", "data_viewer")
    ordering = ["-joined_date"]

admin.site.register(Users, CustomUserAdmin)
