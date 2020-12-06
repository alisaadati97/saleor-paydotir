from django.shortcuts import render
from django.http import HttpResponse

import requests
from .models import Paydotir

# Create your views here.
def verify(request):
    
    token = request.GET['token']
    
    url = 'https://pay.ir/pg/verify'
    #TODO : check for if multiple transactions exits
    
    data = {
            'api':'test',
            'token': token
    }
    
    req = requests.post(url,data=data)
    req = req.json()
    message = req["message"]
    transId = req["transId"]
    
    paydotir = Paydotir.objects.get(token=token)
    
    if message == 'OK':
        paydotir.token = token
        paydotir.transid = transId
        paydotir.save()
        

    return HttpResponse('succesful')