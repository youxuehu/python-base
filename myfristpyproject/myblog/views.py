from django.shortcuts import render

from django.http import HttpResponse

import logging

logger = logging.getLogger('django')


def index(request):
    logger.info("一个萌萌的请求过来了。。。。")
    logger.info("一个更萌的请求过来了。。。。")
    logger.info("这是app01里面的index视图函数")
    return HttpResponse("OK")
