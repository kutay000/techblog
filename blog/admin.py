from django.contrib import admin
from .models import Post, Comment


# 📄 POST ADMIN
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')
    list_filter = ('author',)


# 💬 COMMENT ADMIN
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('author',)