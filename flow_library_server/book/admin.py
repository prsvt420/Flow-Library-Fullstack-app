from django.contrib import admin

from book.models import Book, Author, Genre, Publisher, Tag


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets: tuple = (
        ('Title', {'fields': ['title']}),
        ('Description', {'fields': ['description']}),
        ('Genre', {'fields': ['genre']}),
        ('Author', {'fields': ['author']}),
        ('Publisher', {'fields': ['publisher']}),
        ('ISBN', {'fields': ['isbn']}),
        ('Year', {'fields': ['year']}),
        ('Quantity_pages', {'fields': ['quantity_pages']}),
        ('Image', {'fields': ['image']}),
        ('File', {'fields': ['file']}),
        ('Tags', {'fields': ['tags']}),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display: tuple = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display: tuple = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display: tuple = ('name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display: tuple = ('name',)
