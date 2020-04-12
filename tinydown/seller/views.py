from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
import json
from django.http import JsonResponse
# Create your views here.
from .models import Account, Seller

def index(request):
    latest_account_list = Account.objects.order_by('-create_date')[:5]
    template = loader.get_template('seller/index.html')
    context = {
        'latest_account_list': latest_account_list,
    }
    return render(request, 'seller/index.html', context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body) #取得数据
        seller_name = data['username']
        seller_password = data['password']
        searchArray = Seller.objects.get_or_create(seller_name=seller_name, seller_password=seller_password) #尝试创建用户
        print(searchArray)
        print(data)
        if searchArray[1] == True:
            return JsonResponse({'result': 200, 'msg':'注册成功'})
        else:
            return JsonResponse({'result': 200, 'msg':'已有重复用户名'})