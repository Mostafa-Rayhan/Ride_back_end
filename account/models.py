from django.db import models
from django.contrib.auth.models import AbstractUser
# from PIL import Image

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_rider = models.BooleanField('Is rider', default=False)
    is_driver = models.BooleanField('Is driver', default=False)


class Review(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.CharField(User, max_length=50)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Help(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250, null=True, blank=True)

    # def __str__(self):
    #     return self.user.username


# my_choices = (
#     ('one', 'Bike'),
#     ('two', 'Car'),
#     ('three', 'CNG'),
# )

class profileForm(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # userName = models.CharField(max_length=50, null=True, blank=True)
    # # lastName = models.CharField(max_length=50, null=True, blank=True)
    # email = models.EmailField(max_length=50, null=True, blank=True)
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=100, null=True, blank=True)
    licence = models.IntegerField()
    nidNo = models.IntegerField()
    plateNo = models.IntegerField(max_length=40, null=True)
    vehicle = models.CharField(max_length=40, null=True)
    # vehicle = models.CharField(max_length=40, null=True, choices=my_choices)

    # photo = models.ImageField(upload_to="images/", blank=True)
    # added_on = models.DateTimeField(auto_now_add=True, null=True)
    # update_on = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return f'{self.user.username} Profile'

