var gplay = require('google-play-scraper');
gplay.reviews({appId: "jp.co.happyelements.toto", lang: "zh-tw", sort: gplay.sort.HELPFULNESS, page: 20}).then(console.log, console.log);