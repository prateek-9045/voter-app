from django.contrib import admin
from .models import VoterDetails, ExtendedData, AppDownload, Assembly, CustomerDetails, Election

# Register your models here.
admin.site.register(VoterDetails)
admin.site.register(ExtendedData)
admin.site.register(AppDownload)
admin.site.register(Assembly)
admin.site.register(CustomerDetails)
admin.site.register(Election)

