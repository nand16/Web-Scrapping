from newspaper import Article
import nltk
import pandas as pd

nltk.download('punkt')

data=pd.read_csv("main_news.csv",header=None)
#page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
print("Main news :")
for a in range(1,len(data)):
    s=''
    toi_article = Article(data[4][a], language="en")
    toi_article.download() 
    toi_article.parse() 
    toi_article.nlp() 
    if('surge' in toi_article.text):
        x=toi_article.text.index('surge')
        i=x-1
        s='s'
        while(toi_article.text[i]!='.'):
            s=toi_article.text[i]+s
            i-=1
        i=x+1
        while(toi_article.text[i]!='.'):
            s=s+toi_article.text[i]
            i+=1
        s=s+'.'
    elif('acquisitions' in toi_article.text):
        x=toi_article.text.index('acquisitions')
        i=x-1
        s='a'
        while(toi_article.text[i]!='.'):
            s=toi_article.text[i]+s
            i-=1
        i=x+1
        while(toi_article.text[i]!='.'):
            s=s+toi_article.text[i]
            i+=1
        s=s+'.'
    elif('initial public offering' in toi_article.text):
        x=toi_article.text.index('initial public offering')
        i=x-1
        s='i'
        while(toi_article.text[i]!='.'):
            s=toi_article.text[i]+s
            #print(s)
            i-=1
        i=x+1
        while(toi_article.text[i]!='.'):
            s=s+toi_article.text[i]
            i+=1
        s=s+'.'
    elif('IPO' in toi_article.text):
        x=toi_article.text.index('IPO')
        i=x-1
        s='I'
        while(toi_article.text[i]!='.'):
            s=toi_article.text[i]+s
            #print(s)
            i-=1
        i=x+1
        while(toi_article.text[i]!='.'):
            s=s+toi_article.text[i]
            i+=1
        s=s+'.'
    if(len(s)!=0):
        print("From article",a,"-----",s)
        

data=pd.read_csv("sub_news.csv",header=None)
#page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
print("Sub news :")
for a in range(1,len(data)):
    if(data[4][a]!="None"):
        try:
            s=''
            toi_article = Article(data[4][a], language="en")
            toi_article.download() 
            toi_article.parse() 
            toi_article.nlp() 
            if('surge' in toi_article.text):
                x=toi_article.text.index('surge')
                i=x-1
                s='s'
                while(toi_article.text[i]!='.'):
                    s=toi_article.text[i]+s
                    i-=1
                i=x+1
                while(toi_article.text[i]!='.'):
                    s=s+toi_article.text[i]
                    i+=1
                s=s+'.'
            elif('acquisitions' in toi_article.text):
                x=toi_article.text.index('acquisitions')
                i=x-1
                s='a'
                while(toi_article.text[i]!='.'):
                    s=toi_article.text[i]+s
                    i-=1
                i=x+1
                while(toi_article.text[i]!='.'):
                    s=s+toi_article.text[i]
                    i+=1
                s=s+'.'
            elif('initial public offering' in toi_article.text):
                x=toi_article.text.index('initial public offering')
                i=x-1
                s='i'
                while(toi_article.text[i]!='.'):
                    s=toi_article.text[i]+s
                    #print(s)
                    i-=1
                i=x+1
                while(toi_article.text[i]!='.'):
                    s=s+toi_article.text[i]
                    i+=1
                s=s+'.'
            elif('IPO' in toi_article.text):
                x=toi_article.text.index('IPO')
                i=x-1
                s='I'
                while(toi_article.text[i]!='.'):
                    s=toi_article.text[i]+s
                    #print(s)
                    i-=1
                i=x+1
                while(toi_article.text[i]!='.'):
                    s=s+toi_article.text[i]
                    i+=1
                s=s+'.'
            if(len(s)!=0):
                print("From article",a,"-----",s)
        except:
            pass