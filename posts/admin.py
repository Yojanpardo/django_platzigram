from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'title',
        'photo',
    )
    list_display_links = (
        'user',
        'pk',
    )
    list_editable = ('title',)
    search_fields = (
        'post__title',
        'post__user',
    )
    fieldsets = (
        ('Post',{
                'fields':(('user','title','photo','description',),),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        }),
    )
    readonly_fields = ('created','modified',)
