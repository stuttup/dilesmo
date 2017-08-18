from django.shortcuts import render, redirect
from django.http import HttpResponse

from wiki.models import Item
from wiki.forms import QueryForm
from googleapiclient.discovery import build

def query_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(title=request.POST['query'])
    #     return redirect('/query/')

    return render(request, 'wiki/query.html')


def results_page(request):
    query_form = QueryForm(request.POST or None, initial={'query': 'football'})

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