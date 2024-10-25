from django.contrib import admin

from student.models import Student, Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)