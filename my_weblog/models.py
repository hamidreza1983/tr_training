from django.db import models
   


class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name

class cheap_package(models.Model):
    city = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.city

class luxary_package(models.Model):
    city = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.city

class camping_package(models.Model):
    city = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.city

class newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


    