from django.contrib import admin

@admin.action(description='Mark selected tickets as valid')
def make_valid(modeladmin, request, queryset):
    queryset.update(validity = True)
