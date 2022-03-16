from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from shutil import which
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import time

url="https://www.checkatrade.com/blog/?s="
chrome_path = which("chromedriver")
driver=webdriver.Chrome(executable_path=chrome_path)
driver.minimize_window()
driver.get(url)

x=0
for i in range(0,7):
    y=x+500
    driver.execute_script(f"window.scrollTo({x},{y});")
    x=y

while True:
    try:
        loadmore=driver.find_element_by_xpath("//a[@class='inline-block px-8 py-3 text-sm font-semibold leading-tight text-center text-white bg-catRed-500 rounded-lg btn font-os hover:bgcatred-700']")
        loadmore.click()
        time.sleep(1)
        print('load more found')
    except:
        print('Cant find load more')
        break

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
response=etree.HTML(str(soup))

df=pd.DataFrame({'title':[],
                 'link':[],
                 'tag':[],
                 'text':[]})
df.to_csv('result.csv',index=False)

titlee=[]
for i in response.xpath("//div[@class='flex-1']"):
    text='x'
    link=i.xpath(".//a[1]/@href")
    title=i.xpath(".//a[1]/h4/text()")
    tag='Tag Not Found'
    tagb=i.xpath(".//../div[1]/*/text()")
    if tagb!=[]:
        letter=''
        for j in tagb:
            letter+=j+', '
        letter=letter[:-2]
        tag=letter
    df = pd.DataFrame({'title': [title[0]],
                       'link': [link[0]],
                       'tag': [tag],
                       'text':[text]})
    df.to_csv('result.csv',index=False,mode='a',header=False)
    titlee+=[title[0]]
print(len(titlee))
