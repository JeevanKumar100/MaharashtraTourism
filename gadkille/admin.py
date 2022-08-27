from django.contrib import admin

from gadkille.models import AboutBackground, AboutUs, BestClick, Destination, DestinationBackground, FeedBack, HomeBackground, SuccessfulTreks, TeamMember, UpcomingTreks

# Register your models here.
admin.site.register(HomeBackground)
admin.site.register(UpcomingTreks)
admin.site.register(BestClick)
admin.site.register(SuccessfulTreks)
admin.site.register(FeedBack)

admin.site.register(AboutBackground)
admin.site.register(AboutUs)
admin.site.register(TeamMember)

admin.site.register(DestinationBackground)
admin.site.register(Destination)