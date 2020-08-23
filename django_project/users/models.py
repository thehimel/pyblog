from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Adding new fields to the user with a OneToOne relation.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Overriding the save method and resizing image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
