from django.db import models

# Create your models here.
class Profile(models.Model):

    Mychoices = ((
        ('Dhaka', 'Dhaka'),
        ('Magura', 'Magura'),
        ('Sylhet', 'Sylhet'),
        ('Khulna', 'Khulna'),
    ))
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    state = models.CharField(choices=Mychoices, max_length=50)
    location = models.CharField(max_length=300, blank=True)
    pimage = models.ImageField(upload_to = 'images', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)