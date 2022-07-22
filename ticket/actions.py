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

@admin.action(description='Mark selected tickets have a number')
def make_number(modeladmin, request, queryset):
    for q in queryset:
        if q.number == None:
            try:
                q.number=int(q.name)
                q.save()
            except Exception:
                pass
    # modeladmin.message_user(request, ngettext(
    #         '%d ticket was successfullya get a number.',
    #         '%d tickets were successfullya get a number.',
    #         ) % messages.SUCCESS)