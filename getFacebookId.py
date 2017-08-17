#!/usr/bin/env python
# -*- coding: utf8 -*

import sys
import urllib.request
import json

if __name__ == '__main__':
    # 페이스북 api는 고유이름을 이용하여 접근 불가능하므로
    # graph api를 이용하여 고유이름을 통해 고유의 id를 가지고 와야 한다.
    page_name = "jtbcnews"
    app_id = "111645486170577"
    app_secret = "3e4ed5ae3aa2d856c09285fdaa50d166"
    access_token = app_id + "|" + app_secret

    # https://graph.facebook.com/v2.10/[page_name]/?access+token=[app_id]|[app_secret]
    base = "https://graph.facebook.com/v2.10"
    node = "/" + page_name
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            page_id = data['id']
            print("%s Facebook Numeric ID : %s" % (page_name, page_id))
    except Exception as e:
        print(e)