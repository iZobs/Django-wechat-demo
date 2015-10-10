# -*- coding: utf-8 -*-
from django.shortcuts import render
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
from django.http.response import HttpResponse, HttpResponseBadRequest
import logging

logger = logging.getLogger('django')

# Create your views here.

WECHAT_TOKEN = 'WECHAT_IZOBS'
AppID = 'wx6109791799898b1d'
AppSecret = '2ac875e10c05d19c32844c7af9145129'

# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)

def Index(request):
    logger.info('get signature,timestamp,nonce')

    if wechat_instance.check_signature(
        signature=request.GET['signature'], timestamp=request.GET['timestamp'], nonce=request.GET['nonce']):
            if request.method == 'GET':
                logger.info('it is get')
                return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")
            elif request.method == 'POST':
                logger.info('it is post')
                response = HttpResponse(responseMsg(request))
                return response
            else:
                logger.info('it is else')
                return None
    else:
        rsp = wechat.response_text('check error')
        return HttpResponse(rsp)

def responseMsg(request):
    wechat_instance.parse_data(request.body)
    # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
    message = wechat_instance.get_message()

    response = None
    if message.type == 'text':
        if message.content == 'wechat':
            response = wechat_instance.response_text(u'^_^')
        else:
            response = wechat_instance.response_text(u'文字')
    elif message.type == 'image':
        response = wechat_instance.response_text(u'图片')
    else:
        response = wechat_instance.response_text(u'未知')
    return response

