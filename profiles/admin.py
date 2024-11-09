from django.contrib import admin
from .models import profile,project
from django.contrib.auth.admin import UserAdmin
from .forms import profileChangeForm,profileCreationForm

# Register your models here.

class profileAdmin(UserAdmin):
    add_form = profileCreationForm
    form = profileChangeForm
    model = profile
    list_display = ("email","is_active")
    list_filter = ("email","is_active")
    fieldsets = (
        (None,{"fields": ("email","password",)}),
        ("Permissions", {"fields": ("is_staff","is_superuser","is_active","groups","user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields" : (
                "email","password1","password2","is_staff","is_active",
                "groups","user_permissions",
            )}
        )
        )


search_fields = ("email")
ordering= ("email")

admin.site.register(profile,profileAdmin)
admin.site.register(project)