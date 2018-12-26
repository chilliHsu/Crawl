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



appID = "jp.co.happyelements.toto"
lang = "zh-tw"
sort = "gplay.sort.HELPFULNESS"
AllReview = []
AllDate = []
AllRate = []

for i in range(1,21):
    page = str(i)
    #page =  "1"
    claim, method = crawl_setting('\"'+appID+'\"','\"'+lang+'\"', sort, page)
    writeNodeJS(claim, method)
    reviews = getReviewsList()

    for r in reviews:
        #print(r['text'])
        AllReview.append(r['text'])
        AllDate.append(r['date'])
        AllRate.append(r['score'])


dict = {"reviews" : AllReview,"Date":AllDate,"Rate":AllRate }
save_df = pd.DataFrame(dict)
save_df.to_csv("./review-data/"+appID+".csv",encoding='utf_8_sig')
        
print("scraper over, We have ",len(AllReview)," reviews")

