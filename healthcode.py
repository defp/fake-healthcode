import json
import pprint
from mitmproxy import http

def modify_hz(flow: http.HTTPFlow):
    content = flow.response.content
    body = json.loads(content)
    result = body['result']

    result_json = json.loads(result)
    result_json['healthRecord']['colorCss'] = '#2bac65'
    result_json['healthRecord']['qrColor'] = 'green'
    result_json['descCn'] = ''

    ext_info = result_json['healthcode']['extInfo']
    ext_info_json = json.loads(ext_info)
    if 'outProvinceData' in ext_info_json:
        del ext_info_json['outProvinceData']
    ext_info = json.dumps(ext_info_json)
    result_json['healthcode']['extInfo'] = ext_info

    pprint.pprint(result_json)
    body['result'] = json.dumps(result_json)
    flow.response.text = json.dumps(body)

def modify_hz_scan(flow: http.HTTPFlow):
    content = flow.response.content
    body = json.loads(content)

    data = body['data']
    data['colorCode'] = 'green'
    data['qrCode'] = "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"

    data['specialColorInfo']['colorCss'] = '#2bac65'
    data['specialColorInfo']['level'] = 'green'

    data['travelInfo'] = '1'
    
    flow.response.text = json.dumps(body)

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://healthcode.dingtalk.com/unAuthLwp/queryHealthInfoByAuthCode":
        modify_hz(flow)
        
    # https://szhzjkm.hangzhou.gov.cn:9090/api/v1/healthy/code/zfb/saveAuthInfo
    if "zfb/saveAuthInfo" in flow.request.pretty_url:
        modify_hz_scan(flow)



# TODO disable  reportInfoAndLocationToPolice
# PSOT https://healthcode.dingtalk.com/unAuthLwp/reportInfoAndLocationToPolice
