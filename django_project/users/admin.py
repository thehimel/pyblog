from django.contrib import admin
from .models import Profile

# Register Profile model to access it in the django admin panel.
admin.site.register(Profile)
