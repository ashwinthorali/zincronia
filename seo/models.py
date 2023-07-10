from django.db import models

# Create your models here.
class AboutPage(models.Model):
    description = models.CharField(max_length = 900)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://website.com/")
    
    why_choose_us_img = models.ImageField(upload_to="Page Data", blank=True, null=True)
    why_choose_us_img_1 = models.ImageField(upload_to="Page Data", blank=True, null=True)
    
    
    def __str__(self):
        return self.title


class Team(models.Model):   
    image  = models.ImageField(upload_to="SEO")
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    fb = models.CharField(max_length = 156)
    insta = models.CharField(max_length = 156)
    twitter = models.CharField(max_length = 156)
    youtube = models.CharField(max_length = 156)

    def __str__(self):
        return self.name

class Testimonials(models.Model):   
    image  = models.ImageField(upload_to="SEO")
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    review = models.TextField()
 
    def __str__(self):
        return self.name
   
    
    
    
    
    
     