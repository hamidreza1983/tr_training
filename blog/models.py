from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=255)

    def  __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to = 'blog', default= 'default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
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
