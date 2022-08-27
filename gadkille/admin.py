from django.contrib import admin
from import_export.admin import ImportExportMixin

from gadkille.models import AboutBackground, AboutUs, BestClick, ContactBackground, ContactDetail, CustomerContact, Destination, DestinationBackground, FeedBack, HomeBackground, SuccessfulTreks, TeamMember, UpcomingTreks

class ExportContact(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'mobile', 'subject', 'message']


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

admin.site.register(ContactBackground)
admin.site.register(ContactDetail)
admin.site.register(CustomerContact,ExportContact)