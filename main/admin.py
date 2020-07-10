from django.contrib import admin
from .models import Book, Genre, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "tagline", "genre", "id")
    # readonly_fields = ("title",)
    filter_horizontal = ["authors"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


admin.site.site_title = "ReadMe"
admin.site.site_header = "ReadMe"
