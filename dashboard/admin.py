from django.contrib import admin
from .models import UserProfile, Address

class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ( 'user', 'name', 'dob', 'active')
    search_fields = ['user__username', 'gender', 'phone_number']

    class Meta:
    	model = UserProfile

    def name(self, obj):
    	return str(obj.user.first_name)+" "+ str(obj.user.last_name)

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'state',
        'country',
        'zip_code',
        'default'
    ]
    list_filter = ['default', 'state', 'country']
    search_fields = ['user__user__username', 'street_address', 'state', 'zip_code']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(Address, AddressAdmin)