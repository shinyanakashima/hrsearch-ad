from django.shortcuts import render
# Create your views here.
from search.models import Promotion


from django.http import HttpResponse

def index(request):
    number_of_sites = len(Promotion.objects.values_list('site', flat=True).distinct())
    number_of_articles =  len(Promotion.objects.all())
    context = {"number_of_sites":number_of_sites,"number_of_articles":number_of_articles}
    return render(request, 'top/index.html', context)
