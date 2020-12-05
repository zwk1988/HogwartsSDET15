#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import json

import pytest

# todo:与底层具体的实现框架代码耦合严重，代码冗余，需要用po封装
from 作业.接口自动化.service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['etYL6FEAAAQ6ReAyY_VtpRdF4H753fGQ', 'tag1_new_'],
        ['etYL6FEAAAQ6ReAyY_VtpRdF4H753fGQ', 'tag1-中文_'],
        ['etYL6FEAAAQ6ReAyY_VtpRdF4H753fGQ', 'tag1[]']
    ])
    @pytest.mark.skip
    # 修改标签
    def test_tag_list(self, tag_id, tag_name):
        group_name = 'python15'
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )

        r = self.tag.list()
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert tags != []

    # 创建了一个新的标签组，然后在里面新增3个标签
    @pytest.mark.parametrize("tag_name, order", [
        ['tag_add1', 3],
        ['tag_add2', 2],
        ['tag_add3?', 1]
    ])
    def test_tag_add(self, tag_name, order):
        group_name = 'hogwarts15-SET'
        # tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

        r = self.tag.add(
            group_name=group_name,
            tag_name=tag_name,
            order_num=order
        )

        r = self.tag.list()
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert tags != []

    # 删除标签
    def test_tag_del(self):
        r = self.tag.list()
        # 从新建的标签组里面，取第二个tag_id，传给下面的delete方法进行删除
        tag_id = json.dumps(r.json()['tag_group'][1]['tag'][1]['id'])
        print(tag_id)
        r = self.tag.delete(tag_id)

        # tags = [
        #     tag
        #     for group in r.json()['tag_group'][1] if group['group_name'] == group_name
        #     for tag in group['tag'][0] if ['id'] == tag_id
        # ]
        # assert tags == []
        # group_id = json.dumps(r.json()['tag_group'][1]['group_id'])
