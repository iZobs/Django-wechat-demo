from django.shortcuts import render
from django.http import HttpResponse
from wechat_sdk import WechatBasic
# Create your views here.


def Index(request):
    token = 'WECHAT_IZOBS'
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat = WechatBasic(token=token)

    if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        return HttpResponse(request.GET.get('echostr'))

