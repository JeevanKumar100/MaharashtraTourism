from django.shortcuts import render

from gadkille.models import BestClick, FeedBack, HomeBackground, SuccessfulTreks, UpcomingTreks


# Create your views here.
def index(request):
    homebackground = HomeBackground.objects.all().first()
    bestclick = BestClick.objects.all()
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
    return render(request,'about.html')

def destination(request):
    return render(request,'destination.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')