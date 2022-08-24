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
    placesexplored = models.PositiveIntegerField()
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
    image = models.ImageField(upload_to='webapp/images/')
    def __str__(self):
        return self.title

@receiver(post_delete, sender=SuccessfulTreks)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.image.delete()
    except:
        pass

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



# ---------------------------



# class Highlight(models.Model):
#     title = models.CharField(max_length=20)
#     heading = models.CharField(max_length=50)
#     detail = models.TextField()
#     image = models.ImageField(upload_to='webapp/images/')
#     def __str__(self):
#         return self.heading
    

# class AboutUs(models.Model):
#     title = models.CharField(max_length=40)
#     heading = models.CharField(max_length=50)
#     aboutDetail = models.TextField()
#     def __str__(self):
#         return self.title

# class SuccessfulTreksBackground(models.Model):
#     image = models.ImageField(upload_to='webapp/images/')
#     def __str__(self):
#         return "SuccessfulTreksBackground"

# class Vimeo(models.Model):
#     image = models.ImageField(upload_to='webapp/images/')
#     link = models.URLField()
#     def __str__(self):
#         return "Vimeo"  

# class TrendingPost(models.Model):
#     id = models.AutoField(primary_key=True)
#     link = models.URLField()
#     def __str__(self):
#         return "Trending Post"+str(self.id)
    


# class Testimonial(models.Model):
#     std_choices = ((3,3),(4,4))
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=40)
#     designation = models.CharField(max_length=50)
#     star = models.IntegerField(choices=std_choices)
#     feedback = models.CharField(max_length=150)
#     def __str__(self):
#         return self.name  

# class Destination(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=30)
#     location = models.CharField(max_length=50)
#     rate = models.PositiveSmallIntegerField()
#     day = models.PositiveSmallIntegerField()
#     night = models.PositiveSmallIntegerField()
#     image = models.ImageField(upload_to='webapp/images/')
#     def __str__(self):
#         return self.title

# class Vlog(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=40)
#     date = models.DateField()
#     description = models.CharField(max_length=110)
#     link = models.URLField()
#     youtubeID = models.CharField(max_length=50)
#     def __str__(self):
#         return self.title


# class Contact(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(null=True)
#     mobile = models.CharField(max_length=10,null=True)
#     destination = models.CharField(max_length=40)
#     detail = models.TextField(null=True)
#     def __str__(self):
#         return self.destination



# @receiver(post_delete, sender=Destination)
# def post_del_result(sender, instance, *args, **kwargs):
#     try:
#         instance.image.delete()
#     except:
#         pass





# @receiver(post_delete, sender=SuccessfulTreksBackground)
# def post_del_result(sender, instance, *args, **kwargs):
#     try:
#         instance.image.delete()
#     except:
#         pass

# @receiver(post_delete, sender=Vimeo)
# def post_del_result(sender, instance, *args, **kwargs):
#     try:
#         instance.image.delete()
#     except:
#         pass

# @receiver(post_delete, sender=VlogBackground)
# def post_del_result(sender, instance, *args, **kwargs):
#     try:
#         instance.image.delete()
#     except:
#         pass

