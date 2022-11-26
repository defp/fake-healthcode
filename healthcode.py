import json

from mitmproxy import http
from urllib.parse import urlparse, parse_qs

def modify_hz(flow: http.HTTPFlow):
    content = flow.response.content
    body = json.loads(content)
    result = body['result']

    result_json = json.loads(result)
    result_json['healthRecord']['colorCss'] = '#2bac65'
    result_json['healthRecord']['color'] = 'green'

    body['result'] = json.dumps(result_json)
    flow.response.text = json.dumps(body)


def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://healthcode.dingtalk.com/unAuthLwp/queryHealthInfoByAuthCode":
        modify_hz(flow)
        
