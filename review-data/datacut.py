import jieba
import pandas as pd
import os
import re

#獲得該app的評論、日期、跟分數
def getData(name):
	df = pd.read_csv(name+'.csv')

	reviews = df['reviews']
	scores = df['Score']
	dates = df['Date']

	return reviews,scores,dates

def save_excel(words,count,label,writer):
	dict = {"word list " : words,"frequency":count} #save relevant data into dataframe
	save_df = pd.DataFrame(dict)
	save_df = save_df.sort_values(by='frequency',ascending=False)
	save_df.to_excel(writer,label) #將csv檔存在review-data資料夾中

def getAllFile():

	path='./'
	files = os.listdir(path)
	csvfile = []

	alreadyfiles = os.listdir('./jiebaword/')

	for file in files:
		if file[-4:] == '.csv':
			# print(file[:-4])
			if file[:-4]+'.xls' not in alreadyfiles:
				print(file)
				csvfile.append(file[:-4])
	
	# 這只是測試用
	# csvfile = ['com.playrix.homescapes']
	
	return csvfile

def getStopWord():
	stopWords=[]
	with open('./stopword/stopWords.txt', 'r', encoding='UTF-8') as file:
		for data in file.readlines():
			data = data.strip()
			stopWords.append(data)
	return stopWords

def main():
	jieba.set_dictionary('./dictionary/dict.txt.big.txt') #繁體中文

	gamefiles = getAllFile()
	stopWords = getStopWord()

	for game in gamefiles:
		positiveW = []
		positiveCount = []
		negativeW = []
		negativeCount = []
		name = game
		print(game)
		reviews,scores,dates = getData(name)
		# print(reviews)

		for index in range(len(scores)):
			reviews[index] = re.sub(r'[^\u4e00-\u9fa5]',' ',str(reviews[index]))
			#print(reviews[index])
			seg_list = jieba.cut(reviews[index])
			if scores[index] == 5:
				for word in seg_list:
					#print(i)
					if word not in stopWords and len(word)>1:
						if word not in positiveW :
							positiveW.append(word)
							positiveCount.append(1)
						else:
							pos = positiveW.index(word)
							positiveCount[pos]+=1
			elif scores[index] == 1:
				for word in seg_list:
					if word not in stopWords and len(word)>1:
						if word not in negativeW :
							negativeW.append(word)
							negativeCount.append(1)
						else: 
							pos = negativeW.index(word)
							negativeCount[pos]+=1

		# 這裡就是可以叫出第一款game的文字雲的地方0w0
		WordCloud(positiveCount, positiveW,name+'_positive')
		WordCloud(negativeCount, negativeW,name+'_negative')

		writer = pd.ExcelWriter('./jiebaword/'+name+'.xls')
		save_excel(positiveW,positiveCount,"positive",writer)
		save_excel(negativeW,negativeCount,"negative",writer)
		writer.save()
		print(name,"ok!!")

def WordCloud(word_counts, words,sensitive):
	# print(words)
	import matplotlib.pyplot as plt 
	from wordcloud import WordCloud 

	# 參考曼軒的，my_wordcloud.generate()的input必須是一整個string
	cloud_term = " "
	for i in words:
		cloud_term = cloud_term + i + " "
		#print(cloud_term)

	# 微軟正黑體
	font = r'msjh.ttc'
	my_wordcloud = WordCloud(background_color="white", font_path=font, collocations=False, width=2400, height=2400, margin=2)  
	word_dic={}
	for num in range(len(words)):
		word_dic[words[num]] = word_counts[num]
	
	#print(dict)
	my_wordcloud.generate_from_frequencies(frequencies=word_dic)

	plt.imshow(my_wordcloud)
	plt.axis("off")
	#plt.show()
	if 'positive' in sensitive:
		plt.savefig('./wordcloud/positive/'+sensitive+'.png')
	elif 'negative' in sensitive:
		plt.savefig('./wordcloud/negative/'+sensitive+'.png')

if __name__ == '__main__':
    main()
