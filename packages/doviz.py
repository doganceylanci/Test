import requests as r 
from bs4 import BeautifulSoup as bs
import pandas as pd
from lxml import etree
# Get the data from the website
cins=str(input("döviz cinsini girin (dolar/euro): ")).lower().capitalize()
url =f"https://www.bloomberght.com/doviz/{cins.lower()}"
params = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
def fiyatOgren():
    with r.session() as s:
        page = s.get(url, params=params)
        soup = bs(page.content, "html.parser")
        dom = etree.HTML(str(soup))
        fiyat = dom.xpath("/html/body/div[3]/section/div/div/div[1]/div[2]/div[1]/h1/span[1]")[0].text
        degisim = dom.xpath("/html/body/div[3]/section/div/div/div[1]/div[2]/div[1]/h1/span[2]")[0].text
        tarih = dom.xpath("/html/body/div[3]/section/div/div/div[1]/div[2]/div[1]/h1/span[3]")[0].text
        df = pd.DataFrame({"Cins":cins ,"Fiyat":fiyat, "Degisim":degisim, "Tarih":tarih}, index=[0])
        print(df)
fiyatOgren()