from django.shortcuts import render
from django.template import loader

# Create your views here.
from .models import Account

def index(request):
    latest_account_list = Account.objects.order_by('-create_date')[:5]
    template = loader.get_template('seller/index.html')
    context = {
        'latest_account_list': latest_account_list,
    }
    return render(request, 'seller/index.html', context)