from django.contrib import admin
from .models import Comment, Like


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'date_time_of_publication', 'to_photo')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_photo')
