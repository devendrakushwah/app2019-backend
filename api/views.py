from django.shortcuts import render
from api.models import Coin,Exchange
from django.http import HttpResponse
import json
# Create your views here.

def get_top_coins(request):
    #print(exchange)
    price_convert=Exchange.objects.get(pk='INR').value
    query_set=Coin.objects.order_by('cmc_rank')[:150]
    rsp={}
    for row in query_set:
        id=row.id
        cmc_rank=row.cmc_rank
        symbol=row.symbol
        name=row.name
        price=str(float(str(row.price_usd))*float(str(price_convert)))
        change_day=row.change_day
        rsp[id]={'id':id,'cmc_rank':cmc_rank,'symbol':symbol,'name':name,'price':price,'change_day':change_day}
    rsp_json=(json.dumps(rsp,indent=4))
    return HttpResponse(rsp_json)