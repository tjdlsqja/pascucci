from wordcloud import WordCloud
from konlpy.tag import Okt

script.to_csv('word.txt', encoding = 'cp949')
text = open('word.txt', encoding = 'cp949').read()

def token_konlpy(text):
	okt=Okt()
	return [word for word in okt.nouns(text) if len(word)>1]

 wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=400, height=400, scale=2.0, max_font_size=250).generate(text)

plt.figure(figsize = (40,40))
plt.imshow(wc)
plt.axis('off')
 plt.show()
