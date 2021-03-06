from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose

# Create your models here.

class Hashtag(models.Model):
    content = models.TextField(unique=True)
    # article_cnt = models.IntegerField(default = 1) # 0을 기본 

    def __str__(self):
        return self.content

        
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    hashtags = models.ManyToManyField(Hashtag)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail_detail = ImageSpecField(source='image',
                                     processors=[
                                         #  이미지 회전 방지
                                         Transpose(),
                                         ResizeToFill(670, 500)
                                         ],
                                     format='JPEG',
                                     options={'quality': 100})
    image_thumbnail_index = ImageSpecField(source='image',
                                     processors=[
                                        #  이미지 회전 방지
                                         Transpose(),
                                         ResizeToFill(200, 200)
                                         ],
                                     format='JPEG',
                                     options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
