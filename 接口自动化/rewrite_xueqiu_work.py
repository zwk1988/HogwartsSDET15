import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 响应数据拿到转换成json对象
        data = json.loads(flow.response.content)

        name2 = data['data']['items'][1]['quote']['name']
        # 字符串拼接
        data['data']['items'][1]['quote']['name'] = name2 * 2
        data['data']['items'][2]['quote']['name'] = ''
        # 把修改后的内容赋给response原始数据格式
        flow.response.text = json.dumps(data)
