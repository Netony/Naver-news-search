from django.shortcuts import render
from .models import Content
from django.core.paginator import Paginator
import urllib.request
import json
from django.utils import timezone


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    if kw:
        Content.objects.all().delete()
        client_id = "LYVZkqjtCMSsIoNTSvbo"
        client_secret = "Nd46m_umMZ"
        encText = urllib.parse.quote(kw)
        url = "https://openapi.naver.com/v1/search/news?display=100&query=" + encText
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id",client_id)
        req.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(req)

        response_body = response.read()
        data = response_body.decode('utf-8')
        item = json.loads(data)
        items = item['items']
        for i in items:
            c = Content(title=i['title'], url=i['link'], pub_date=timezone.now())
            c.save()
    content_list = Content.objects.order_by('-pub_date')
    paginator = Paginator(content_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'content_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'news/content_list.html', context)