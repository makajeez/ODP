from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference', 'gateway', 'timestamp', 'status', 'paid']
    search_fields = ['transaction_id', 'uid', 'reference', 'status', 'timestamp', 'email', 'fullname']
    list_filter  = ['status', 'paid',  'timestamp', 'user', 'gateway',]
    list_display_links = ['user', 'reference', 'gateway', 'paid']



# Register your models here.
admin.site.register(Donation, DonationAdmin)