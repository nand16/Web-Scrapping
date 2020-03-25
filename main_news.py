import urllib.request
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
import pandas as pd
#import time
nltk.download('punkt')

main_news={}
count=0

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"

page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
infile=urllib.request.urlopen(page).read()
soup = BeautifulSoup(infile,'lxml')

section = soup.find("div", {"class": "lBwEZb BL5WZb GndZbb"})

for a in section:
    a1=a.find({'h3':"ipQwMb ekueJc gEATFF RD0gLb"}).text
    
    a3=(a.find({'a':"VDXfz"}).get('href'))
    a3='https://www.news.google.com/'+a3
    
    a4=(a.find({'time':"WW6dff uQIVzc Sksgp"}).get('datetime'))
    
    toi_article = Article(a3, language="en")
    toi_article.download() 
    toi_article.parse() 
    toi_article.nlp() 
    
    a2=toi_article.summary
    
    count+=1
    main_news[count]=[a1,a2,a4,a3]
    
    
    
data=pd.DataFrame.from_dict(main_news,orient='index',columns=['Ttile','Summmary','DateTime',"URL"])
#print(data.head(3))
data.to_csv("main_news.csv")