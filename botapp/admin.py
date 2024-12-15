from django.contrib import admin
from .models import BotUsers, Category, Word, UserWord, UserCategory, WordOption


@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'username', 'phone_number', 'created', 'updated')
    search_fields = ('first_name', 'last_name', 'username', 'phone_number', 'user_id')
    list_filter = ('created', 'updated')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'created', 'updated')
    search_fields = ('title', 'description', 'owner__first_name', 'owner__last_name')
    list_filter = ('is_public', 'created', 'updated')


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'author', 'category', 'created', 'updated')
    search_fields = ('word', 'meaning', 'description', 'author__first_name', 'category__title')
    list_filter = ('created', 'updated')
    autocomplete_fields = ('author', 'category')


@admin.register(UserWord)
class UserWordAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'is_favorite', 'is_learned', 'created', 'updated')
    search_fields = ('user__first_name', 'word__word')
    list_filter = ('is_favorite', 'is_learned', 'created', 'updated')


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_favorite', 'is_learned', 'created', 'updated')
    search_fields = ('user__first_name', 'category__title')
    list_filter = ('is_favorite', 'is_learned', 'created', 'updated')
    filter_horizontal = ('category',)


@admin.register(WordOption)
class WordOptionAdmin(admin.ModelAdmin):
    list_display = ('word', 'option', 'is_correct', 'created', 'updated')
    search_fields = ('word__word', 'option')
    list_filter = ('is_correct', 'created', 'updated')
