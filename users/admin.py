from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','website','phone_number','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website','picture')
    search_fields = ('user__email','user__first_name','user__phonenumber')
    list_filter = ('created','modified')
