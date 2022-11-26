# fake-healthcode


## hz

POST https://healthcode.dingtalk.com/unAuthLwp/queryHealthInfoByAuthCode

```javascript
{
  arguments: null,
  errorCode: null,
  errorMsg: null,
  result: '{"reason":"0","zlbLogoSize":30,"modifiedTimes":0,"logoUrl":"//img.alicdn.com/imgextra/i1/O1CN01RTcWEm1mriBsqhQ3Q_!!6000000005008-2-tps-516-516.png","uid":553581839,"descEn":"Tips:According to relevant regulations of epidemic prevention and control regulations and your possible exposure to COVID-19, Your health QR code turns yellow.Starting November 25,3 consecutive days of nucleic acid testing (once a day) , after the sampling turned green, 24 hours of non-detection will be re-assigned to the yellow code. Three days after the nucleic acid results were negative, the green code was automatically transferred.","descCn":"温馨提示：根据疫情防控相关规定和您可能到过相关风险地区或场所，现给您健康码赋黄码，11月25日起，连续3天核酸检测（每天1次），采样后转绿，24小时内未检测的将重新赋黄码。","logoSize":30,"orgReworkModel":{"orgName":"啊app"},"vaccinatedSwitch":true,"name":"李大双","healthRecord":{"colorCss":"#FF9F00","qrCode":"V0ding408fc9e037b13079a1320dcb25e91351","feControlModel":{"tips":"","enTips":""},"stateCouncilBarCode":"7e0bba7d4716a7c704ce4c725d21938b","eHealthCode":"","qrColor":"yellow","extInfo":"{\\"districtCodeFlag\\":true,\\"nucleicData\\":{\\"nucleicDescriptionEn\\":\\"d\\",\\"nucleicDescriptionCn\\":\\"天内\\",\\"countDownDescriptionEn\\":\\"3 Days To Maturity\\",\\"nucleicStatusCn\\":\\"阴性\\",\\"countDownDescriptionCn\\":\\"距离3天到期还剩\\",\\"nucleicStatusEn\\":\\"Neg\\",\\"expireSpecVal\\":\\"168\\",\\"showCompareTime\\":true,\\"lessthenDayNumbersDisplayAsHours\\":2,\\"compareType\\":\\"report\\",\\"checkTime\\":\\"2022-11-25 15:03:42\\",\\"hourValue\\":25.5,\\"nucleicDayEn\\":\\"≤2\\",\\"timeInterval\\":\\"48\\",\\"nucleicDayCn\\":2,\\"countDown\\":166321,\\"compareTime\\":\\"2022-11-25 19:43:06\\",\\"reportTime\\":\\"2022-11-25 19:43:06\\",\\"recentNoNucleicDay\\":3},\\"outProvinceData\\":{\\"flag\\":false}}"},"descCss":"#333333","config":"{\\"travelCardUrl\\":\\"alipays://platformapi/startapp?appId=2019011763060066&page=pages%2Fjourney-webview%2Fjourney-webview\\",\\"travelCardUrlH5\\":\\"https://xc.caict.ac.cn/?code=152&phone={phone}&t={timestamp}&ad=1\\"}"}',
  success: true
}
> JSON.parse(a.result)
{
  reason: '0',
  zlbLogoSize: 30,
  modifiedTimes: 0,
  logoUrl: '//img.alicdn.com/imgextra/i1/O1CN01RTcWEm1mriBsqhQ3Q_!!6000000005008-2-tps-516-516.png',
  uid: 553581839,
  descEn: 'Tips:According to relevant regulations of epidemic prevention and control regulations and your possible exposure to COVID-19, Your health QR code turns yellow.Starting November 25,3 consecutive days of nucleic acid testing (once a day) , after the sampling turned green, 24 hours of non-detection will be re-assigned to the yellow code. Three days after the nucleic acid results were negative, the green code was automatically transferred.',
  descCn: '温馨提示：根据疫情防控相关规定和您可能到过相关风险地区或场所，现给您健康码赋黄码，11月25日起，连续3天核酸检测（每天1次），采样后转绿，24小时内未检测的将重新赋黄码。',
  logoSize: 30,
  orgReworkModel: { orgName: '啊app' },
  vaccinatedSwitch: true,
  name: '李大双',
  healthRecord: {
    colorCss: '#FF9F00',
    qrCode: 'V0ding408fc9e037b13079a1320dcb25e91351',
    feControlModel: { tips: '', enTips: '' },
    stateCouncilBarCode: '7e0bba7d4716a7c704ce4c725d21938b',
    eHealthCode: '',
    qrColor: 'yellow',
    extInfo: '{"districtCodeFlag":true,"nucleicData":{"nucleicDescriptionEn":"d","nucleicDescriptionCn":"天内","countDownDescriptionEn":"3 Days To Maturity","nucleicStatusCn":"阴性","countDownDescriptionCn":"距离3天到期还剩","nucleicStatusEn":"Neg","expireSpecVal":"168","showCompareTime":true,"lessthenDayNumbersDisplayAsHours":2,"compareType":"report","checkTime":"2022-11-25 15:03:42","hourValue":25.5,"nucleicDayEn":"≤2","timeInterval":"48","nucleicDayCn":2,"countDown":166321,"compareTime":"2022-11-25 19:43:06","reportTime":"2022-11-25 19:43:06","recentNoNucleicDay":3},"outProvinceData":{"flag":false}}'
  },
  descCss: '#333333',
  config: '{"travelCardUrl":"alipays://platformapi/startapp?appId=2019011763060066&page=pages%2Fjourney-webview%2Fjourney-webview","travelCardUrlH5":"https://xc.caict.ac.cn/?code=152&phone={phone}&t={timestamp}&ad=1"}'
}
```

