# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lundong.shenhu300_chuangyeban import *
from django.shortcuts import render
from django.http.response import HttpResponse
import json
from lundong.models import Bankuailundong

# Create your views here.
def everyday_change(request):
    save_data()
    return HttpResponse("OK")

def lundong(request):
    return render(request,'lundong.html')

def shenhu300_list(request):
    a = []
    for i in range(0,80):
        a.append(Bankuailundong.objects.get(num=i+1).value)
    return HttpResponse(json.dumps(a),content_type='application/json')