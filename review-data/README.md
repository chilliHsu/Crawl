# reviews-data
下載資料 : git clone "網址"

如要更新資料 : git pull 

#跑datacut.py 什麼都沒有出現是正常的。因為我的設計是當有新的評論csv檔出現，才會將檔案存入csvfile列表中，才會跑(不想一直重新跑所有的)。所以如果要嘗試了話，把jiebaword隨便刪一個xls檔，應該就會跑你刪的那個檔，重新生成一個新的xls檔。

#評論檔案csv 存在review-data資料夾中，也就是跟datacut.py同一層中

-------------------

jeiba下來的資料都放在jiebaword裡面，裡面包括 positive,negative 的字，跟出現頻率 這裡的positive是指給予rate=5顆星的人的評論、negative是指給予rate=1顆星的評論。 此外，出現頻率已排序完成
jeiba的code叫做datacut.py 

----------------------
文字雲 
http://stacepsho.blogspot.com/2018/06/word-cloud-in-python.html

https://blog.csdn.net/wireless_com/article/details/60571394
(但我還沒寫，懶)

-------------------
jieba : 關於繁體中文、idf 相關參考資料 (idf 還沒用)
https://coderwall.com/p/38wtgw/jieba

https://github.com/tomlinNTUB/Python-in-5-days

停用詞: stopWords.txt ,此外，另外新增"遊戲" 這個字為停用詞
