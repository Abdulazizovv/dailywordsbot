from django.contrib import admin
from .models import BotUsers


class BotUsersAdmin(admin.ModelAdmin):
    list_filter = ('created', 'updated')
    search_fields = ('usr_id', 'username', 'first_name', 'last_name')
    date_hierarchy = 'created'
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    list_display_links = ('user_id', 'first_name')

    def formatted_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')
    formatted_created.admin_order_field = 'created'
    formatted_created.short_description = 'Created'

    def formatted_updated(self, obj):
        return obj.updated.strftime('%Y-%m-%d %H:%M:%S')
    formatted_updated.admin_order_field = 'updated'
    formatted_updated.short_description = 'Updated'

    list_display = ('id', 'user_id', 'username', 'first_name', 'last_name', 'formatted_created', 'formatted_updated')


admin.site.register(BotUsers, BotUsersAdmin)
