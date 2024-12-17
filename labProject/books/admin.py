from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'price', 'edition')
    search_fields = ('title', 'authors')
    list_filter = ('edition',)
