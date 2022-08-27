from django.shortcuts import render

from gadkille.models import AboutBackground, AboutUs, BestClick, FeedBack, HomeBackground, SuccessfulTreks, TeamMember, UpcomingTreks


# Create your views here.
def index(request):
    homebackground = HomeBackground.objects.all().last()
    bestclick = BestClick.objects.all().last()
    successfultreks = SuccessfulTreks.objects.all()
    upcomingtreks = UpcomingTreks.objects.all()
    feedbacks = FeedBack.objects.all()

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
    return render(request,'destination.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')