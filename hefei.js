
// [Script]
// 安康码 = type=http-response,pattern=https://akm.ahzwfw.gov.cn/akm-sj-user/health/detail,requires-body=1,max-size=1048576,debug=1,script-path=https://rules-set.oss-cn-beijing.aliyuncs.com/hefei.js,script-update-interval=300


let obj = JSON.parse($response.body);

obj.data.healthStatus = "0";
obj.data.orgName = "NoCode";
body = JSON.stringify(obj);

$done({body});
