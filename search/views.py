from django.shortcuts import render
from django.http import HttpResponse
from .models import Promotion

def index(request):
    sample_list = Promotion.objects.all()
    context = {'sample_list': sample_list}
    return render(request, 'search/index.html', context)

def results(request):
    response = str(request.POST['q'])
    results_list = Promotion.objects.filter(sponsored__icontains=str(request.POST['q']))
    context = {'results_list': results_list,
    'response': response}
    return render(request, 'search/results.html', context)

def detail(request, article_id):
    pr = Promotion.objects.get(id=article_id)
    context = {'pr': pr}
    return render(request, 'search/detail.html', context)

import csv
def save_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'

    results_list = Promotion.objects.filter(sponsored__icontains=str(request.POST['q']))
    writer = csv.writer(response)
    writer.writerow(['Site', 'Sponsored', 'Title', 'Date', 'URL'])
    for row in results_list:
        writer.writerow([row.site, row.sponsored, row.title ,row.date, row.url])
    return response
