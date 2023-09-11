from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, BookReview, Profile, Feedback


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # išjungia papildomas tuščias eilutes įvedimui
    readonly_fields = ('id',)
    can_delete = False


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    list_editable = ('due_back', 'status')
    search_fields = ('id', 'book__title')

    fieldsets = (
        ('General', {'fields': ('id', 'book')}),
        ('Availability', {'fields': ('status', 'due_back', 'reader')}),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Profile)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Feedback)
