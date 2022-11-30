let obj = JSON.parse($response.body);

obj.data.healthStatus = "0";
obj.data.orgName = "NoCode";
body = JSON.stringify(obj);

$done({body});
