from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Tag, Post

class TagSitemap(Sitemap):
    def items(self):
        return Tag.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects

    def lastmod(self, obj):
        return obj.created_at