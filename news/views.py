from django.shortcuts import render
from .models import Content
from django.core.paginator import Paginator
import urllib.request
import json
from time import sleep

def index(request):
    Content.objects.all().delete()
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    if kw:
        client_id = "bIoP3NHu1eWH4ON1koub"
        client_secret = "ZBYUwa8oaT"
        encText = urllib.parse.quote(kw)
        url = "https://openapi.naver.com/v1/search/news?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            item = json.loads(data)
            for i in item:
               c = Content(title=i['title'], url=i['link'], pub_date=i['pubDate'])
               c.save()
            sleep(5)    
        else:
            print("Error Code:" + rescode)
    content_list = Content.objects.order_by('-pub_date')
    paginator = Paginator(content_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'content_list': page_obj}
    return render(request, 'news/content_list.html', context)