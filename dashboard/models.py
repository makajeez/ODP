from django.db import models
from django_countries.fields import CountryField
from core.helpers import getUniqueId
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics', help_text="User Profile Picture")
    address = models.ForeignKey('dashboard.Address', blank=True, null=True, on_delete=models.SET_NULL)
    bio = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    gender = models.CharField(default="Others", blank=True, null=True, max_length=6, help_text="Gender", choices=GENDER)
    dob = models.DateField(blank=True, null=True,help_text='Date of Birth')
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"
        ordering = ["-reg_date",]

    def __str__(self):
        return self.user.username



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

class Address(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(multiple=False)
    zip_code = models.CharField(max_length=100)
    default = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.user.user.username} - {self.street_address[:10]}' # self.user.user.username
