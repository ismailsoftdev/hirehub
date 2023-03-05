from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __save__(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).__save__(*args, **kwargs)

    def __str__(self):
        return self.user.username
