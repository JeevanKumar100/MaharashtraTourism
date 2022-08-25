from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here. 

class HomeBackground(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=150)
    link = models.URLField()
    image = models.ImageField(upload_to='gadkille/images/')
    def __str__(self):
        return self.heading

@receiver(post_delete, sender=HomeBackground)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass


class UpcomingTreks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    rate = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    night = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gadkille/images/')
    def __str__(self):
        return self.title

@receiver(post_delete, sender=UpcomingTreks)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass
    

class BestClick(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    successfultours = models.PositiveIntegerField()
    happytourist = models.PositiveIntegerField()
    placeexplored = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gadkille/images/')

@receiver(post_delete, sender=BestClick)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass


class SuccessfulTreks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    trekcount = models.IntegerField()
    image = models.ImageField(upload_to='gadkille/images/')
    def __str__(self):
        return self.title

@receiver(post_delete, sender=SuccessfulTreks)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass


class FeedBack(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class AboutBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/')

@receiver(post_delete, sender=AboutBackground)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass

    
class DestinationBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/')
    
@receiver(post_delete, sender=DestinationBackground)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass


class ContactBackground(models.Model):
    image = models.ImageField(upload_to='gadkille/images/')

@receiver(post_delete, sender=ContactBackground)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass



