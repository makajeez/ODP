from django.views.generic import ListView, DetailView, View
from .helpers_sub import Egg, getSiteMedia
from .models import MainPage, HomePageSlider
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse, render
from blog.models import Post
from gallery.models import GalleryImage


# Create your views here.
class HomeView(View):
    # model = Item
    # paginate_by = 12
    template_name = "core/home.html"
    def get(self, *args, **kwargs):
        context = {}
        context['posts'] = Post.objects.all().filter(publish=True).order_by('-pub_time')[:6]
        context['slider'] = HomePageSlider.objects.filter(active=True).first()
        context['site_media'] = GalleryImage.objects.all().order_by('-updated')[:2]
        # context['partners'] = Partner.objects.all().order_by('-updated')
        return render(self.request, template_name='core/home.html', context=context)


class MainPageDetailView(DetailView):
    template_name = "core/pages.html" #.format(themeVersion() )
    model = MainPage
    query_pk_and_slug = True
    context_object_name = 'page'
    # context = {}
    def get_context_data(self, *args, **kwargs):  
        try:            
            context = super(MainPageDetailView, self).get_context_data(*args, **kwargs)
            print('Found')
            return context
        except MainPage.DoesNotExist:
            context['page'] =  Egg
            #TODO: send mail on error
            print('Not Found')
            return context
        return context

def contactView(request):
    next_url = reverse('audience:contact')
    return HttpResponseRedirect(next_url)
