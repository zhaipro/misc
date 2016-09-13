'''
http://inside.wot.kongzhong.com/inside/wotinside/signact/signinfo?jsonpcallback=jQuery&useraccount=&login=<base64(<login>)>=&zoneid=1500100
http://inside.wot.kongzhong.com/inside/wotinside/signact/sign?jsonpcallback=jQuery&useraccount=&login=<base64(<login>)>&zoneid=1500100
'''
# coding: utf-8
import base64
import time

import requests


def jsonp(url, **params):
    params['jsonpcallback'] = 'jQuery'
    res = requests.post(url, params)
    def jQuery(obj):    # NOQA
        return obj
    return eval(res.text)


def dbg(fmt, *args):
    msg = fmt % args
    if isinstance(msg, bytes):
        msg = msg.decode('ascii')
    print(msg)


def call(api, login, zoneid=1500100):
    _login = base64.b64encode(login)
    url = b'http://inside.wot.kongzhong.com/inside/wotinside/signact/%b'
    url = url % api
    data = jsonp(url, login=_login, zoneid=zoneid, useraccount='')
    dbg(b"%b('%b', %d) => %r", api, login, zoneid, data)
    return data


def sign(login, zoneid=1500100):
    return call(b'sign', login, zoneid)


def signinfo(login, zoneid=1500100):
    return call(b'signinfo', login, zoneid)


def xxx_sign(login, times, zoneid=1500100):
    for _ in range(times):
        sign(login, zoneid)
        login += b' '
        time.sleep(5)

if __name__ == '__main__':
    # signinfo(b'xxx')
    sign(b'xxx')
    # xxx_sign(b'xxx', 10)
