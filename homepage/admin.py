from django.contrib import admin

from homepage.models import Bookmark, Folder

admin.site.register(Folder)


@admin.register(Bookmark)
class BookmarkInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'timestamp')
