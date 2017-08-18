from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Queries
from .forms import QueriesForm
from googleapiclient.discovery import build

def query_page(request):
    qresults = None
    if request.GET.get('q'):
        question = request.GET.get('q')
        query = Queries.objects.create(query=question)
        query.save()

        service = build("customsearch", "v1",
                        developerKey="AIzaSyBNpq5EBgxwYUMGeTmOfYGr8wOlX8B_EeY")

        res = service.cse().list(
            q=question,
            cx='006354159737151125162:amidb2ooswc',
            searchType='image',
            num=3,
            imgType='clipart',
            fileType='png',
            safe='off'
        ).execute()

        if not 'items' in res:
            images = [{'title': '', 'src': ''}, {'title': '', 'src': ''}, {'title': '', 'src': ''}]
        else:
            images = []
            for item in res['items']:
                images.append({'title': item['title'], 'src': item['link']})

        qresults = images


    return render(request, 'wiki/query.html', {
        'qresults': qresults,
    })

def results_page(request):
    query_form = QueriesForm(request.POST or None, initial={'query': 'football'})

    service = build("customsearch", "v1",
                    developerKey="AIzaSyBNpq5EBgxwYUMGeTmOfYGr8wOlX8B_EeY")

    res = service.cse().list(
        q=query_form['query'],
        cx='006354159737151125162:amidb2ooswc',
        searchType='image',
        num=3,
        imgType='clipart',
        fileType='png',
        safe='off'
    ).execute()

    if not 'items' in res:
        images = [{'title':'', 'src':''}, {'title':'', 'src':''}, {'title': '', 'src': ''}]
    else:
        images = []
        for item in res['items']:
            images.append({'title': item['title'], 'src': item['link']})
    return render(request, 'wiki/results.html', {'qresults': images})