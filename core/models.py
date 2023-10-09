from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from core.helpers import getUniqueId

# Create your models here.



class MainPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(verbose_name="Main Image", blank=True, null=True, upload_to='pages/img', help_text="Image size should be 922x731 px")
    body = RichTextUploadingField(blank=True, null=True)
    vid_file = models.FileField(upload_to='blog/videos', blank=True, null=True, help_text="Upload Video File")
    youtube_video_id = models.CharField(blank=True, null=True, max_length=20, help_text="Youtube Video ID e.g L0I7i_lE5zA. Not Complete Url")
    extra_info = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    on_navigation = models.BooleanField(default=False)

    class Meta: 
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Pages'
        ordering = ["-title", ]

    def get_video_link(self):
        if self.youtube_video_id:
            return "https://www.youtube.com/embed/{}".format(self.youtube_video_id)
        elif self.vid_file:
            return self.vid_file.url
        else:
            return None
    def __str__(self):
        return self.title


class HomePageSlider(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)    
    
    class Meta: 
        verbose_name = 'Home Page Slider'
        verbose_name_plural = 'Home Page Sliders'
        ordering = ["-updated", ]

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    slider = models.ForeignKey(HomePageSlider, on_delete=models.CASCADE, related_name='sliders')
    file = models.ImageField(upload_to='sliders/img', help_text="Image size is 1900px width and 1267px height")
    header = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    button = models.CharField(max_length=50, blank=True, null=True)
    button_url = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    class Meta: 
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'
        ordering = ["-updated", ]
    def __str__(self):
        return self.slider.title
 
class Partner(models.Model):
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='partners', help_text='Image size is 340x145 px')
    website = models.CharField(max_length=200, blank=True, null=True, help_text="Start with http:// or https://")
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)

    def __str__(self):
        return self.title

class SiteInformation(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    info = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)

    class Meta: 
        verbose_name = 'Site Information'
        verbose_name_plural = 'Site Informations'
        ordering = ["-updated", ]

    def __str__(self):
        return self.title