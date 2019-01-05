from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

text = "更新後小地圖的跑車顯示根本就是屁 什麼都看不到 排位賽的物資分配不要太誇張 跑了兩三棟房子只有手槍跟配件 藏寶圖也不要開放啦 這遊戲是我要活下去 不是我要開寶箱"

terms = jieba.cut(text,cut_all=False)
#sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True)
for t in terms:
	print(t)

print(Counter(terms))

my_wordcloud = WordCloud(background_color="white",collocations=False, width=2400, height=2400, margin=2)  
my_wordcloud.generate_from_frequencies(frequencies=Counter(terms))
