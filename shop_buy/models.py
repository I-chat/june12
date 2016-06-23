from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


# Create your models here.
@python_2_unicode_compatible
class Product_Info(models.Model):
    product_name = models.CharField('Product Name', max_length=50)
    product_desc = models.CharField('Product Description', max_length=250)
    product_image = models.ImageField('Product Image', upload_to='images/%Y/%m/%d/')
    product_price = models.DecimalField('Product Price', max_digits=8, decimal_places=2)
    pub_date = models.DateTimeField('date published', default = timezone.now)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return "/shop_buy/%i/" % self.id


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=140)  
    male = 'M'
    female = 'F'
    gender_choices = (
        (male, 'Male'),
        (female, 'Female'),
    )
    gender = models.CharField(max_length=2, choices=gender_choices)
    profile_picture = models.ImageField('Profile Image', upload_to='images/profile')

    def __str__(self):
        return 'Profile of user: %s' % self.user.username

		
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])