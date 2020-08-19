from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# User is the bult-in model provided by django
# User-Post has one-to-many relationship.
# One user can have multiple posts.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
