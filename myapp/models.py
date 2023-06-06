from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Category (models.Model):
    cat = models.CharField(max_length=255)
    def __str__(self):
        return self.cat

class cartoon(models.Model):
    card_title=models.CharField(max_length=50)
    image=CloudinaryField('image')
    description=models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Release_Year=models.CharField(max_length=55,blank=True, null=True)
    text1=models.CharField(max_length=1000,blank=True, null=True)
    download_url = models.CharField(max_length=300,blank=True, null=True)
    download_url1 = models.CharField(max_length=300,blank=True, null=True)
    download_url2 = models.CharField(max_length=300,blank=True, null=True)
    download_url3= models.CharField(max_length=300,blank=True, null=True)
    download=models.CharField(max_length=600,blank=True, null=True)
    download1=models.CharField(max_length=600,blank=True, null=True)
    download2=models.CharField(max_length=600,blank=True, null=True)
    download3=models.CharField(max_length=600,blank=True, null=True)
    text=models.CharField(max_length=600,blank=True, null=True)
    
    uploaded_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.uploaded_on)
    
    
    image1=CloudinaryField('image',blank=True, null=True)
    image2=CloudinaryField('image',blank=True, null=True)
    image3=CloudinaryField('image',blank=True, null=True)
    image4=CloudinaryField('image',blank=True, null=True)
    image5=CloudinaryField('image',blank=True, null=True)
    image6=CloudinaryField('image',blank=True, null=True)
    
    def __str__(self):
        return self.card_title
    
    
class contact(models.Model):
    username=models.CharField(max_length=55)
    subject=models.CharField(max_length=1000)
    email=models.EmailField(max_length=55)
    city=models.CharField(max_length=55)
    number=models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    