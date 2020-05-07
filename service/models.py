from django.db import models


class About(models.Model):
    service = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    reviewer = models.CharField(max_length=500)
    post = models.CharField(max_length=500, default=2)
    review = models.CharField(max_length=500, default=2)
    reviewer_image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.service

class Contact(models.Model):
    description = models.CharField(max_length=900)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email


