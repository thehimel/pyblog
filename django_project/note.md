About
---------------
Editor: VS Code
Theme: Dainty Andromeda


Admin
-----
Make migration before logging in the admin panel for the first time.

# To control models from admin page, we need to register models in the app/admin.py
from blog.models import Post
admin.site.register(Post)


Models
------
DateTimeField
-------------
Suppose in a Post model we have a field named date_posted.
if we use, date_posted = models.DateTimeField(auto_now=True),
it will take the current time and will get updated when we update the post.

if we use, date_posted = models.DateTimeField(auto_now_add=True),
it will take the current time but date can never be changed.

-> Best option:
from django.utils import timezone

class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)

# Notice, use didn't use parenthesis after timezone.now.
By this we are not executing timezone.now function at this point,
instead, we are just passing the funtion as default value.


Interactive Console
-------------------
# We can import and use django objects with shell.
python manage.py shell

from blog.models import Post
from django.contrib.auth.models import User

User.objects.all()  # Returns QuerySet with all users
User.objects.first()  # Returns the first user
User.objects.filter(username='john')  # Returns QuerySet with all users after filtering
User.objects.filter(username='john').first()  # Returns the first user after filtering

user = User.objects.filter(username='john').first()  # Saving the result in a variable
user.id  # Returns the id of the user, i.e. 1
user.pk  # Returns the primary key of the user, i.e. 1

user = User.objects.get(id=1)  # Returns the user with that id.

# date_posted field is not required to be declared as it will be saved automatically.
post_1 = Post(title='Blog 1', content='1st Post Content', author=user)
post_1.save()  # Commit the post to the database
Post.objects.all()  # Returns QuerySet with all the posts.

# author_id can also be used instead of author while creating the post
post_2 = Post(title='Blog 1', content='1st Post Content', author_id=user.id)
post_1.save()
Post.objects.all()

post = Post.objects.first()  # Returns the first post
post.content  # Returns the content of the selected post
post.date_posted()  # Returns the DateTime object
post.author  # Returns the user object
post.author.email  # Returns the email of that author

user.post_set.all()  # Returns QuerySet with all posts created by this user
Syntax: user.modelName_set.all()

# Create a post directly using post_set
# External .save() is not required as it will commit automatically.
user.post_set.create(title='Blog 3', content='3rd Blog Content')


User and Profile in shell
-------------------------
# Run this in the shell after creating a profile
from django.contrib.auth.models import User
user = User.objects.filter(username='john').first()
user  # Returns the user object
user.profile  # Returns the profile object of the user
user.profile.image  # Returns the image object of the user profile
user.profile.image.width  # Returns the width(int)
user.profile.image.url  # Returns the url(str) of the image.



Signals
-------
A signal is used when we need to do something after a particular action.
To perform a signal we need a sender, receiver, and the signal itself.
Few developers include the signal section in the models.py but django
documentation suggests to keep the signals in the app_name/signals.py
to let the import work perfectly.

Example: Create a profile after a user is created.
Note: You must import the signals in the ready method of the AppConfig
located in app_name/apps.py

-> django_project/users/signals.py
-> Syntax: project_root/app_name/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


-> Exmplanation:
In create_profile, sender=User, signal=post_save, receiver=create_profile.
When a User is created a post_save signal is sent to the receiver
create_profile. post_save passes User instance and created=True to
create_profile. Upon getting the signal, it creates a profile.
On the same way save_profile receiver is used to save the profile of the
User instance.


Migration
---------
See the SQL code that a migration file executes in the backend
------------------------------------------------------------------
Example: python manage.py sqlmigrate blog 001
Syntax: python manage.py sqlmigrate app_name migration_file_number


views.py
--------
Flash Messages
--------------
In form view we can define flash messages to be shown on the user's end.
from django.contrib import messages

-> Types of Messages:
messages.info
messages.success
messages.warning
messages.error
messages.debug

Example:
-> Backend code in views.py
if form.is_valid():
    messages.success(request, f'Account created for {username}!')

-> Frontend code in the html file:
Django flash messages and Bootstrap alert has similaries.
i.e. alert-info, alert-success, alert-warning
message.tags will be replaced with given info/success/warning/error/debug etc.

{% if messages %}
    {% for message in messages %}
        <div class='alert alert-{{ message.tags }}'>
            {{ message }}
        </div>
    {% endfor %}
{% endif %}


Routing
-------
In urls.py, we use a trailing slash after every route in the urlpatters, to avoid confusion.
urlpatterns = [
    path('about/', views.about, name='blog-about'),
]

Serving files uploaded by a user during development
---------------------------------------------------
During development, user-uploaded media files from MEDIA_ROOT can be served
using django.views.static.serve() view. See django documentation for more details.
For production, don't use this approach. Read 'Deploying static files'.


Template Inheritance
--------------------
In file.html during template inheritance, end a block by {% endblock block_name %} to avoid confusion.
You can also use just {% endblock %}, but mentioning the name will help while ending multiple blocks.


Template
--------
If you print the DateTimeField object in the template, you'll see the default formatting.
But we can use custome filtering as mentioned in https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
Example: {{ post.date_posted|date:"F d, Y" }}
This prints like January 01, 2020


Hard Reload of Browser
----------------------
In Windows, Ctrl + F5
In Mac, Cmd + Shift + R


External Apps
-------------
crispy forms
------------
This is used to style Django forms with Bootstrap. By default CRISPY_TEMPLATE_PACK = 'boostrap2'
pip install django-crispy-forms
conda install -c conda-forge django-crispy-forms

-> settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    ...
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

-> Frontend code in the base.html file:
{% extends 'blog/base.html' %}
{% load crispy_forms_tags %}

Note: use {{ form|crispy }} to apply crispy filter.
{{ form.as_p }} is not required since styling is controlled by crispy_forms.
