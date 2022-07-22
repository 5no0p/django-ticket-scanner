from django.contrib import admin, messages
from django.utils.translation import ngettext

@admin.action(description='Mark selected tickets as valid')
def make_valid(modeladmin, request, queryset):
    updated = queryset.update(validity = True)
    modeladmin.message_user(request, ngettext(
            '%d ticket was successfully marked as valid.',
            '%d tickets were successfully marked as valid.',
            updated,
        ) % updated, messages.SUCCESS)

@admin.action(description='Mark selected tickets as unchecked')
def make_unchecked(modeladmin, request, queryset):
    updated = queryset.update(is_checked = False)
    modeladmin.message_user(request, ngettext(
            '%d ticket was successfully marked as unchecked.',
            '%d tickets were successfully marked as unchecked.',
            updated,
        ) % updated, messages.SUCCESS)