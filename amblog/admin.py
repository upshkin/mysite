from django.contrib import admin
from .models import Blog, Author, Entry


class EntryTabular(admin.TabularInline):  # Можно использовать StackedInline
    model = Entry
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [EntryTabular]


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
