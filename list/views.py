from django.shortcuts import render
from django.http import HttpResponse
from search.models import Promotion

def index(request):
    site_list = Promotion.objects.values_list('site', flat=True).distinct()
    context = {'site_list': site_list}
    return render(request, 'list/index.html', context)


def table(request, site_name):
    results_list = Promotion.objects.filter(site=site_name)
    context = {'results_list': results_list,
    'site_name':site_name}
    return render(request, 'list/table.html', context)

def detail(request, site_name, article_id):
    pr = Promotion.objects.get(id=article_id)
    context = {'pr': pr}
    return render(request, 'list/detail.html', context)

import csv
def save_csv(request, site_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'
    results_list = Promotion.objects.filter(site=str(request.POST['q']))
    writer = csv.writer(response)
    writer.writerow(['Site', 'Sponsored', 'Title', 'Date', 'URL'])
    for row in results_list:
        writer.writerow([row.site, row.sponsored, row.title ,row.date, row.url])
    return response
