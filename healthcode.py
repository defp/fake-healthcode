import json
from mitmproxy import http

def modify_hz(flow: http.HTTPFlow):
    content = flow.response.content
    body = json.loads(content)
    result = body['result']

    result_json = json.loads(result)
    result_json['healthRecord']['colorCss'] = '#2bac65'
    result_json['healthRecord']['color'] = 'green'
    result_json['descCn'] = ''

    body['result'] = json.dumps(result_json)
    flow.response.text = json.dumps(body)

def modify_hz_scan(flow: http.HTTPFlow):
    content = flow.response.content
    body = json.loads(content)

    data = body['data']
    data['colorCode'] = 'green'
    data['time'] = '24'

    data['specialColorInfo']['colorCss'] = '#2bac65'
    data['specialColorInfo']['level'] = 'green'
    data['specialColorInfo']['orange'] = '1'
    
    flow.response.text = json.dumps(body)

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://healthcode.dingtalk.com/unAuthLwp/queryHealthInfoByAuthCode":
        modify_hz(flow)
        
    # https://szhzjkm.hangzhou.gov.cn:9090/api/v1/healthy/code/zfb/saveAuthInfo
    if "zfb/saveAuthInfo" in flow.request.pretty_url:
        modify_hz_scan(flow)

