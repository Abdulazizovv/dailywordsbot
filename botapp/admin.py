from django.contrib import admin
from .models import BotUsers, Word, WordOption, Category, UserWord, UserCategory


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


class WordOptionInline(admin.TabularInline):
    model = WordOption
    extra = 1


class WordAdmin(admin.ModelAdmin):
    inlines = [WordOptionInline]
    list_filter = ('created', 'updated')
    search_fields = ('word', 'meaning')
    date_hierarchy = 'created'
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    list_display_links = ('word',)

    def formatted_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')
    formatted_created.admin_order_field = 'created'
    formatted_created.short_description = 'Created'

    def formatted_updated(self, obj):
        return obj.updated.strftime('%Y-%m-%d %H:%M:%S')
    formatted_updated.admin_order_field = 'updated'
    formatted_updated.short_description = 'Updated'

    list_display = ('id', 'word', 'author', 'category', 'formatted_created', 'formatted_updated')


admin.site.register(Word, WordAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'title', 'description')
    list_filter = ('owner', 'created', 'updated')
    readonly_fields = ('created', 'updated')

    def formatted_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')
    formatted_created.admin_order_field = 'created'
    formatted_created.short_description = 'Created'

    def formatted_updated(self, obj):
        return obj.updated.strftime('%Y-%m-%d %H:%M:%S')
    formatted_updated.admin_order_field = 'updated'
    formatted_updated.short_description = 'Updated'
    list_display = ('owner', 'title', 'description', 'formatted_created', 'formatted_updated')


admin.site.register(Category, CategoryAdmin)