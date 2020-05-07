from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title




class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.project


