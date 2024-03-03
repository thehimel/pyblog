from django.contrib import admin
from blog.models import Post

# Register models to control them in the admin portal.
admin.site.register(Post)
