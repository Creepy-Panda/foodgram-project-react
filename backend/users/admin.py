from django.contrib import admin

from .models import Follow, CustomUser


admin.site.register(Follow)
admin.site.register(CustomUser)
