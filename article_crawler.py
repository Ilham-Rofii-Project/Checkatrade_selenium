from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from bs4 import BeautifulSoup
from lxml import etree
import time
import pandas as pd

data=pd.read_csv('result.csv')
link = data.link


chrome_path = which("chromedriver")
driver=webdriver.Chrome(executable_path=chrome_path)
driver.minimize_window()
count=0
link2=link[0:3]
# texttt=[]

for ilink in link:
    try:
        print(ilink)
        driver.get(ilink)
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        response=etree.HTML(str(soup))
        title=response.xpath("//h1/text()")
        urlt=response.xpath("//div[@class='container px-4 py-10 mx-auto']/descendant-or-self::node()/a/text()")
        text_link=[]
        for i in urlt:
            if i.strip() !='':
                text_link+=[i.strip()]
        urlt=response.xpath("//div[@class='container px-4 py-10 mx-auto']/descendant::node()/text()")
        text=''
        if type(title)==type(text_link):
            text+=title[0].strip()+'\n\n'
        else:
            text+=title.strip()+'\n\n'
        for i in urlt:
            exists = False
            for j in text_link:
                if i == j:
                    exists = True
            if exists == True:
                text = text[:-1]
                text += ' ' + i + ' '
            else:
                if i.strip()!='':
                    text += i + '\n'
        text=text+'\n'
#         text2=''
#         countt=0
#         for i in text.split('\n'):
#             if countt <1 or countt>12:
#                 text2+=i+'\n'
#             countt+=1
#         text=text2

        # texttt=''
        # texttt+=[text]
        data.text[count]=text
        # df = pd.DataFrame({'text': [text]})
        # df.to_csv('result.csv',index=False,mode='a',header=False)
        count+=1
        print(f'sudah selesai {count} artikel')
#         if count==3:
#             break
# TODO : hapus hasil result.csv
    except:
        text='Article Not Found'
        data.text[count]=text
        count+=1
        print(f'artikel {count} tidak selesai')
#         if count==3:
#             break
        continue
data.to_csv('result.csv',index=False)
data.to_excel('result.xlsx',index=False)
# print(data)
