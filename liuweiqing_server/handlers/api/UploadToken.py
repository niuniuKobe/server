#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: UploadToken.py
@date: 16/4/18 下午2:08
"""

import base64
from RequestHandler import RequestHandler
from tornado import gen
import time
import json
import hmac
from hashlib import sha1
import settings
from behaviors import CreatUserAvatar

class UploadToken(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        uid=self.get_argument('uid').encode("utf8")

        aid=yield CreatUserAvatar().Action()
        print aid
        # aid=aid.encode("utf8")
        avatar_id=str(aid).encode('utf8')

        condition="{\"scope\":\"liuweiqing:123123123123\",\"deadline\":%d}"%(1461155867+1000000)
        print condition
        encoded = base64.b64encode(condition)
        has = hmac.new(settings.Qiniu.SECRET_KEY, encoded, sha1)
        encodedSign = base64.b64encode(has.digest())

        upload_token="%s:%s:%s"%(settings.Qiniu.ACCESS_KEY,encodedSign,encoded)
        print upload_token
        self.render({"token":upload_token,'key':'123123123123'})

