import requests as r 
from bs4 import BeautifulSoup as bs
import pandas as pd

# Get the data from the website
cins=str(input("döviz cinsini girin (dolar/euro): ")).lower().capitalize()
url =f"https://www.bloomberght.com/doviz/{cins.lower()}"
params = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
with r.session() as s:
    page = s.get(url, params=params)
    soup = bs(page.content, "html.parser")
    fiyat = soup.find("span", {"class":"LastPrice upGreen"}).text
    degisim = soup.find("span", {"class":"bulk PercentChange"}).text
    tarih = soup.find("span", {"class":"date"}).text
    df = pd.DataFrame({"Cins":cins ,"Fiyat":fiyat, "Degisim":degisim, "Tarih        Saat":tarih}, index=[1])
    print(df)