from django.contrib import admin
from .models import Post, PostCategory

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at", "updated_at")
    list_filter = ("author", "status", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]


admin.site.register(PostCategory)
