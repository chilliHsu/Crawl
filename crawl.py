from Naked.toolshed.shell import execute_js, muterun_js 
import sys
import json
import demjson
import pandas as pd

def crawl_setting(app_id, language, sortby, pageNum):
    claim = "var gplay = require('google-play-scraper');"
    method = "gplay.reviews({"+ \
                "appId: "+app_id+", " + \
                "lang: "+language+", " + \
                "sort: "+sortby+", " + \
                "page: "+pageNum + \
            "}).then(console.log, console.log);"
    return(claim, method)

def writeNodeJS(claim, method):
    with open('myRunNodeJS.js', 'w') as the_file:
        the_file.write(claim+'\n')
        the_file.write(method)

def getReviewsList():
    response = muterun_js('myRunNodeJS.js')
   
    if response.exitcode == 0:
        result = response.stdout
        #print(result)
    else:
        print('Error')
    return(demjson.decode(result))

appID_List = ['com.miHoYo.bh3tw']

"""
'com.nsplay.bbs.android','jp.konami.duellinks','com.elive.hunter.gp','com.foyo.WJZJ','com.linecorp.LGWPMT','com.gmail.app.nakayama7.hensaiHan','com.nexon.dynastywarriors','com.herogame.gplay.streetballtw','com.a.one.ss','com.bigbull.tdsgtw'
'com.miHoYo.bh3tw','com.icantw.wings','com.garena.game.kgtw','com.linecorp.LGFARM','com.enjoygame.jwstw','com.wepie.snakeoff','com.gamedreamer.rgdsjtw','com.nintendo.zara','com.linecorp.LGBB2','com.garena.game.botw'
"""

for appID in appID_List:
    #appID = "com.nsplay.bbs.android"
    lang = "zh-tw"
    sort = "gplay.sort.HELPFULNESS"
    AllReview = []
    AllDate = []
    AllScore = []

    for i in range(1,21):
        page = str(i)
        #print(page)
        claim, method = crawl_setting('\"'+appID+'\"','\"'+lang+'\"', sort, page)
        writeNodeJS(claim, method)
        reviews = getReviewsList()
        #print(len(reviews))

        for r in reviews:
            #print(r['text'])
            AllReview.append(r['text'])
            AllDate.append(r['date'])
            AllScore.append(r['score'])


    dict = {"reviews" : AllReview,"Date":AllDate,"Score":AllScore } #save relevant data into dataframe
    save_df = pd.DataFrame(dict)
    save_df['Date'] = pd.to_datetime(save_df['Date'])
    save_df.sort_values(by='Date', inplace=True)
    if len(AllReview) == 800 :
        save_df.to_csv("./review-data/TOP10/"+appID+".csv",encoding='utf_8_sig') #將csv檔存在review-data資料夾中
        print("scraper over, We have ",appID," reviews")
    else:
        print(appID," We only have ", len(AllReview)," reviews")

