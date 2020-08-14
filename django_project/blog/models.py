from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# User is the bult-in model provided by django
# User-Post has one-to-many relationship.
# One user can have multiple posts.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
