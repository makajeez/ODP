from django.urls import re_path
# , include

from .views import contactView, subscriberView

# from django.contrib.auth import views as auth_views

urlpatterns = [
	re_path(r'contact/$', contactView,  name='contact'),
	re_path(r'subscribe/$', subscriberView, name='add-subscriber'), 
]
 
