from django.contrib import admin
from .models import Post

admin.site.site_title = "Blog"

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "body", "author", "create_date")
    list_display_links = ("title",)
    search_fields = ("title",)
    ordering = ("author", "title")
    list_filter = ("author",)
    date_hierarchy = "create_date"

admin.site.register(Post, PostAdmin)