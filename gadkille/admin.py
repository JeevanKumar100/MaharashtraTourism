from django.contrib import admin

from gadkille.models import BestClick, FeedBack, HomeBackground, SuccessfulTreks, UpcomingTreks

# Register your models here.
admin.site.register(HomeBackground)
admin.site.register(UpcomingTreks)
admin.site.register(BestClick)
admin.site.register(SuccessfulTreks)
admin.site.register(FeedBack)
