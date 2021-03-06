from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_description = models.CharField(max_length=250)
    image_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=50)
    post_content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image_url = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.title

    def content_truncate(self):
        return self.post_content[:250]