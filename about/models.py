from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length = 50)
    blood = models.CharField(max_length = 50)
    address = models.CharField(max_length = 254)
    about = models.CharField(max_length = 500)
    image = models.FileField(upload_to='images/')
     
    
    def __str__(self):
        return self.name




