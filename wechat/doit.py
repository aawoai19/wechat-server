#coding=utf-8

from wechat_sdk import *
import re

token = 'mahhhraspberrypi'

def do_it(request):
    wechat = WechatBasic(token=token)
    if wechat.check_signature(signature=request.REQUEST.GET('signature', ''),
                              timestamp=request.REQUEST.GET('timestamp', ''),
                              nonce=request.REQUEST.GET('nonce', '')):
        if request.method == 'GET':
            rsp = request.REQUEST.get('echostr', '')
        else:
            wechat.parse_data(request.body)
            message = wechat.get_message()
            if message.type == 'text':
                data = message.content
                if u'二八轮动'in data is True:
                    rsp = wechat.response_news([{
                        'title': u'第一条新闻标题',
                        'description': u'第一条新闻描述，这条新闻没有预览图',
                        'url': u'http://www.google.com.hk/',
                    }, {
                        'title': u'第二条新闻标题, 这条新闻无描述',
                        'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                        'url': u'http://www.github.com/',
                    }, {
                        'title': u'第三条新闻标题',
                        'description': u'第三条新闻描述',
                        'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                        'url': u'http://www.v2ex.com/',
                    }])
            else:
                rsp = wechat.response_text(u'消息类型: {}'.format(message.type))
    else:
        rsp = wechat.response_text('check error')