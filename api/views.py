from api.models import Coin,Exchange,Image,News
from django.http import HttpResponse
import json
# Create your views here.

def get_top_coins(request):
    #print(exchange)
    exchange=request.GET.get('exchange','')
    price_convert=Exchange.objects.get(pk=exchange).value
    query_set=Coin.objects.order_by('cmc_rank')[:150]
    image_set=Image.objects.all()
    rsp={}
    for row in query_set:
        id=row.id
        cmc_rank=row.cmc_rank
        symbol=row.symbol
        name=row.name
        price=str(float(str(row.price_usd))*float(str(price_convert)))
        change_day=row.change_day
        image_url=''
        try:
            image_url=image_set.get(symbol__exact=symbol).url
        except:
            image_url='None'
        rsp[id]={'id':id,'cmc_rank':cmc_rank,'symbol':symbol,'name':name,'price':price,'change_day':change_day,'image_url':image_url}
    rsp_json=(json.dumps(rsp,indent=4))
    return HttpResponse(rsp_json)

def get_details(request):
    id=request.GET.get('id','')
    exchange=request.GET.get('exchange','')
    price_convert = Exchange.objects.get(pk=exchange).value
    query_set = Coin.objects.get(id=id)
    image_set = Image.objects.all()
    rsp = {}
    image_url = ''
    id=query_set.id
    cmc_rank=query_set.cmc_rank
    symbol=query_set.symbol
    name=query_set.name
    price_usd=query_set.price_usd
    total_supply=query_set.total_supply
    max_supply=query_set.max_supply
    circulating_supply=query_set.circulating_supply
    change_hour=query_set.change_hour
    change_day=query_set.change_day
    change_week=query_set.change_week

    try:
        image_url = image_set.get(symbol__exact=symbol).url
    except:
        image_url = 'None'

    price=float(price_usd)*float(price_convert)

    rsp['id'] = id
    rsp['cmc_rank'] = cmc_rank
    rsp['symbol'] = symbol
    rsp['name'] = name
    rsp['price'] = price
    rsp['exchange']=exchange
    rsp['total_supply'] = total_supply
    rsp['max_supply'] = max_supply
    rsp['circulating_supply']=circulating_supply
    rsp['change_hour']=change_hour
    rsp['change_day']=change_day
    rsp['change_week']=change_week
    rsp['image_url']=image_url

    rsp_json = (json.dumps(rsp, indent=4))
    return HttpResponse(rsp_json)

def search_coins(request):
    rsp={}
    string=request.GET.get('q','')
    query_set=Coin.objects.filter(name__contains=string)
    for row in query_set:
        rsp[row.name]={'id':row.id,'symbol':row.symbol}
    rsp_json = (json.dumps(rsp, indent=4))
    return HttpResponse(rsp_json)

def get_news(request):
    query_set=News.objects.all()
    rsp={}
    i=1
    for row in query_set:
        rsp[i]={'title':row.title,'image':row.image,'url':row.url,'date':row.date,'source':row.source}
        i+=1
    rsp_json = (json.dumps(rsp, indent=4))
    return HttpResponse(rsp_json)