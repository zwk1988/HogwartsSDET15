#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import requests


class Tag:
    # token=None
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwaa1128934e3c0615'
        corpsecret = 'F4HJXIzrwB3RWkz8OJrwX93Ix-XqgH6sEYtsHygwCSc'
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        print('获取token')
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    def add(self, group_name, tag_name, order_num):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?',
                          params={"access_token": self.token},
                          json={
                              'group_name': group_name,
                              # 'order': 3,
                              'tag': [{
                                  "name": tag_name,
                                  "order": order_num
                              }]
                          }

                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
            params={"access_token": self.token},
            json={
                'tag_id': []
            }
        )

        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id='', tag_name=''):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?',
                          params={"access_token": self.token},
                          json={
                              'id': id,
                              'name': tag_name
                          }

                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_id):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?',
                          params={"access_token": self.token},
                          json={
                              "tag_id": [tag_id]

                          }
                          )

        print(json.dumps(r.json(), indent=2))
        return r
