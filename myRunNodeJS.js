var gplay = require('google-play-scraper');
gplay.reviews({appId: "com.netease.g78na.tw", lang: "zh-tw", sort: gplay.sort.HELPFULNESS, page: 20}).then(console.log, console.log);