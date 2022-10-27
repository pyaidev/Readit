from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=221)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='articles/')
    context = models.TextField()
    tags = models.ManyToManyField(Tags)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f'http://127.0.0.1:8000/{self.image.url}'
        return f"https://sfsfs.uz/{self.image.url}"




