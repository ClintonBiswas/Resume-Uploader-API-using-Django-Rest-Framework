from django.contrib import admin
from .models import Profile
# Register your models here.
#admin.site.register(Profile)
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email', 'location', 'dob', 'gender', 'state', 'pimage', 'rdoc',]