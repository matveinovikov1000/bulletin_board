from django.contrib import admin

from advertisements.models import Announcement, Review


@admin.register(Announcement)
class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "created_at",
    )


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ad",
        "author",
        "created_at",
    )
