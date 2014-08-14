from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'body', 'owner', 'moderator', 'status',
        'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'body', 'owner__username', 'moderator__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Story', {
            'fields': ('title', 'body', 'status')
        }),
        ('Auth', {
            'classes': ('collapse',),
            'fields': ('owner', 'moderator')
        }),
        ('Change History', {
            'classes': ('collapse',),
            'fields': ('updated_at', 'created_at')
        })
    ]

admin.site.register(Task, TaskAdmin)
