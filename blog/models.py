from asyncio.windows_events import NULL
from calendar import c
from distutils.command.upload import upload
import email
from django.db import models
from users.models import BlogUser
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    uname = models.ForeignKey(BlogUser,default=1, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.tag.slug, self.slug)

        

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

