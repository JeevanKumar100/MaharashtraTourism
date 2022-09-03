from multiprocessing import context
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from gadkille.models import AboutBackground, AboutUs, BestClick, ContactBackground, CustomerContact, Destination, DestinationBackground, Feedback, Gallery, GalleryBackground, HomeBackground, SuccessfulTreks, TeamMember, TrekPhoto, UpcomingTreks


# Create your views here.
def index(request):
    homebackground = HomeBackground.objects.all().last()
    bestclick = BestClick.objects.all().last()
    successfultreks = SuccessfulTreks.objects.all()
    upcomingtreks = UpcomingTreks.objects.all()
    feedbacks = Feedback.objects.all()

    context = {
        'homebackground':homebackground,
        'bestclick':bestclick,
        'successfultreks':successfultreks,
        'upcomingtreks':upcomingtreks,
        'feedbacks':feedbacks,
                
    }
    
    return render(request, 'index.html',context)

def about(request):
    aboutbackground = AboutBackground.objects.all().last()
    aboutus = AboutUs.objects.all().last()
    members = TeamMember.objects.all()

    context = {
        'aboutbackground' : aboutbackground,
        'aboutus' : aboutus,
        'members' : members,
    }

    return render(request,'about.html',context)

def destination(request):
    destinationbackground = DestinationBackground.objects.all().last()
    destinations = Destination.objects.all()

    context = {
        'destinationbackground' : destinationbackground,
        'destinations' : destinations,
    }

    return render(request,'destination.html',context)

def gallery(request):
    gallerybackground = GalleryBackground.objects.all().last()
    photos = TrekPhoto.objects.all()

    context = {
        'gallerybackground' : gallerybackground,
        'photos' : photos,
    }

    return render(request,'gallery.html',context)

def gallery1(request):
    photos = Gallery.objects.all().order_by('?')

    context = {
        'photos' : photos,
    }

    return render(request,'gallery1.html',context)

def contact(request):
    contactbackground = ContactBackground.objects.all().last()

    context = {
        'contactbackground' : contactbackground,
    }

    return render(request,'contact.html',context)


def savecontact(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        
        try :
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            contact = CustomerContact.objects.create(name=name,mobile=mobile,subject=subject,message=message)
            contact.save()
            
            messages.success(request,"Thank you "+ name +" for connecting with us..")
            return HttpResponseRedirect("/contact/#contact_message")
        except :
            messages.error(request,"Something went wrong, please check your details again")
            return HttpResponseRedirect("/contact/#contact_message")