from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'website',
        'phone_number',
        'picture'
    )
    list_display_links = ('pk','user')
    list_editable = (
        'phone_number',
        'website',
        'picture'
    )
    search_fields = (
        'user__email',
        'user__first_name',
        'user__phone_number'
    )
    list_filter = ('created','modified')
    fieldsets=(
        ('Profile',{
            'fields': (('user','picture'),),
        }),
        ('Info',{
            'fields': (('website','phone_number','bio'),),
        }),
        ('Metadata',{
            'fields': (('created','modified'),),
        }),
    )
    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
