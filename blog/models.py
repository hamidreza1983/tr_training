from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class category(models.Model):
    name = models.CharField(max_length=255)

    def  __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to = 'blog', default= 'default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(category)
    counted_viwes = models.IntegerField(default = 0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:

        ordering = ['-created_date']
    def __str__(self):
        return self.title

    def snipets(self):
        return self.content[:10] + '...'
    
    def titleedit(self):
        return self.title.upper()


class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:

        ordering = ['-created_date']
    def __str__(self):
        return self.name