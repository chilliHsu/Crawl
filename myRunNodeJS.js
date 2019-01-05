var gplay = require('google-play-scraper');
gplay.reviews({appId: "com.bigbull.tdsgtw", lang: "zh-tw", sort: gplay.sort.HELPFULNESS, page: 1}).then(console.log, console.log);