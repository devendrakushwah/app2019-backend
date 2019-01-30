from django.http import HttpResponse
from django.template import  loader
import json
import requests
from api.api_keys import *
from api.models import Coin,Exchange,News

# Create your views here.

def maintain(request):
    html=loader.get_template('maintain/maintain.html')
    return HttpResponse(html.render({'data':'','success':False},request))

def update_coins(request):
    Coin.objects.all().delete()
    rsp=requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD&CMC_PRO_API_KEY='+cmc_api)
    data = json.loads(rsp.text)
    for i in data['data']:
        id = i['id']
        cmc_rank = i['cmc_rank']
        symbol = i['symbol']
        name = i['name']
        price_usd = i['quote']['USD']['price']
        total_supply = i['total_supply']
        max_supply = i['max_supply']
        circulating_supply = i['circulating_supply']
        change_hour = i['quote']['USD']['percent_change_1h']
        change_day = i['quote']['USD']['percent_change_24h']
        change_week = i['quote']['USD']['percent_change_7d']
        instance = Coin(id=id, cmc_rank=cmc_rank, symbol=symbol, name=name, price_usd=price_usd,
                        total_supply=total_supply, max_supply=max_supply, circulating_supply=circulating_supply,
                        change_hour=change_hour, change_day=change_day, change_week=change_week)
        instance.save()
    html = loader.get_template('maintain/maintain.html')
    return HttpResponse(html.render({'data': 'Coins', 'success': True}, request))

def update_exchange(request):
    Exchange.objects.all().delete()
    rsp = requests.get('http://apilayer.net/api/live?access_key='+cl_api)
    data = json.loads(rsp.text)
    for i in data['quotes'].keys():
        name = i[3:]
        value = data['quotes'][i]
        instance = Exchange(name=name, value=value)
        instance.save()
    html = loader.get_template('maintain/maintain.html')
    return HttpResponse(html.render({'data': 'Exchanges', 'success': True}, request))

def update_news(request):
    News.objects.all().delete()
    rsp = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key='+ccmp_api)
    data = json.loads(rsp.text)
    j = 0
    for i in data['Data']:
        j += 1
        if (j > 20):
            break
        title = i['title']
        image = i['imageurl']
        url = i['url']
        date = i['published_on']
        source = i['source_info']['name']
        instance = News(title=title, image=image, url=url, date=date, source=source)
        instance.save()
        #print(j)
    html = loader.get_template('maintain/maintain.html')
    return HttpResponse(html.render({'data': 'News', 'success': True}, request))