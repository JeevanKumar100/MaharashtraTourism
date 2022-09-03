from pyexpat import model
from unicodedata import name
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete,pre_save

from django.core.exceptions import ValidationError


# Create your models here. 

#Class to validate the file size
class ValidateSize():
    def validate_1MB(fieldfile_obj):
            filesize = fieldfile_obj.file.size
            megabyte_limit = 1.0
            if filesize > megabyte_limit*1024*1024:
                raise ValidationError("Max file size is %s MB" % str(megabyte_limit))
    def validate_2MB(fieldfile_obj):
            filesize = fieldfile_obj.file.size
            megabyte_limit = 2.0
            if filesize > megabyte_limit*1024*1024:
                raise ValidationError("Max file size is %s MB" % str(megabyte_limit))
    def validate_3MB(fieldfile_obj):
            filesize = fieldfile_obj.file.size
            megabyte_limit = 3.0
            if filesize > megabyte_limit*1024*1024:
                raise ValidationError("Max file size is %s MB" % str(megabyte_limit))

class HomeBackground(models.Model):
    heading = models.CharField(max_length=150)
    subheading = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_3MB])
    def __str__(self):
        return self.heading
    class Meta: 
        verbose_name = "Home Background"
        verbose_name_plural = "Home Background"


class UpcomingTreks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rate = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    night = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    file = models.FileField(upload_to='gadkille/files/',validators=[ValidateSize.validate_2MB])
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name = "Upcoming Trek"
        verbose_name_plural = "Upcoming Treks"
    

class BestClick(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    successfultours = models.PositiveIntegerField()
    happytourist = models.PositiveIntegerField()
    placeexplored = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    def __str__(self):
        return self.title


class SuccessfulTreks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    trekcount = models.IntegerField()
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name = "Successful Trek"
        verbose_name_plural = "Successful Treks"


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"


class AboutBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_3MB])

    
class AboutUs(models.Model):
    heading = models.CharField(max_length=200)
    detail = models.TextField()
    def __str__(self):
        return self.heading
    class Meta: 
        verbose_name = "About US"
        verbose_name_plural = "About US"


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField()
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_1MB])
    def __str__(self):
        return self.name


class DestinationBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_3MB])  


class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rate = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    night = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    def __str__(self):
        return self.title


class GalleryBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_3MB])


class TrekPhoto(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    location = models.CharField(max_length=30)
    def __str__(self):
        return self.location
    class Meta: 
        verbose_name = "TrekPhoto"
        verbose_name_plural = "TrekPhotos"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_2MB])
    location = models.CharField(max_length=30)
    def __str__(self):
        return self.location
    class Meta: 
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class ContactBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/',validators=[ValidateSize.validate_3MB])


class CustomerContact(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.PositiveBigIntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customer Contact"




##------- Handler configurations for models ----------

def model_pre_delete_handler(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
        instance.file.delete()
    except:
        pass

def model_pre_save_handler(sender,instance,*args,**kwargs):
    try:
        available_object = sender.objects.get(id=instance.id)
        if available_object.image != instance.image:
            available_object.image.delete()
        if available_object.file != instance.file:
            available_object.file.delete()
    except:
        pass

MODELS_TO_BE_PRE_DELETE_HANDLED = [HomeBackground, UpcomingTreks, BestClick, SuccessfulTreks, AboutBackground, TeamMember, DestinationBackground, Destination, GalleryBackground, TrekPhoto, Gallery, ContactBackground]

for model in MODELS_TO_BE_PRE_DELETE_HANDLED:
    pre_delete.connect(model_pre_delete_handler, sender=model)
    pre_save.connect(model_pre_save_handler,sender=model)