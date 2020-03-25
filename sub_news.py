import urllib.request
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
import pandas as pd
#import time
nltk.download('punkt')

sub_news={}
count=0

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"

page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
infile=urllib.request.urlopen(page).read()
soup = BeautifulSoup(infile,'lxml')

sect = soup.find("div", {"class": "lBwEZb BL5WZb GndZbb"})

for j in sect:
    try:
        a=j.find({'div':"SbNwzf"})    
        b1=a.find({'h4':"ipQwMb ekueJc gEATFF RD0gLb"}).text
        b2=(a.find({'span':"xBbh9"}).text)
        b3=(a.find({'a':"VDXfz"}).get('href'))
        b3='https://www.news.google.com/'+b3
        b4=(a.find({'time':"WW6dff uQIVzc Sksgp"}).get('datetime'))
    except:
        b1=b2=b3=b4='None'
    count+=1
    sub_news[count]=[b1,b2,b4,b3]
    print(sub_news[count])
    
data=pd.DataFrame.from_dict(sub_news,orient='index',columns=['Ttile','Summmary','DateTime',"URL"])
#print(data.head(3))
data.to_csv("sub_news.csv")