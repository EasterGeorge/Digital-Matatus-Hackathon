from django.contrib import admin
from .models import Post, Comment ,Resources , Reports, Ushuhuda, Cases

admin.site.register(Post)
admin.site.register(Resources)
admin.site.register(Reports)
admin.site.register(Ushuhuda)
admin.site.register(Cases)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)