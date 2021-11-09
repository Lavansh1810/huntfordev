from django.contrib import admin
from .models import Messsage, Profile, Skill
# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Messsage)