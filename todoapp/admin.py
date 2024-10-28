from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    # Optional: Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('completed',),
            'classes': ('collapse',)
        }),
    )
