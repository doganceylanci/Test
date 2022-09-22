import requests as r 
from bs4 import BeautifulSoup as bs
import pandas as pd 

# Get the data from the website
citys=list()
benzin=list()
dizel = list()
lpg = list()
url = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari"
params = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
def fiyatlar():
    with r.session() as s:
        page=s.get(url, params=params)
        soup=bs(page.content, "html.parser")
        # Get the data from the table
        citys.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(2) > td:nth-child(1)").text)
        citys.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(3) > td:nth-child(1)").text)
        citys.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(4) > td:nth-child(1)").text)
        citys.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(5) > td:nth-child(1)").text)
        citys.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(29) > td:nth-child(1)").text)
        
        benzin.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(2) > td:nth-child(2)").text.strip())
        benzin.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(3) > td:nth-child(2)").text.strip())
        benzin.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(4) > td:nth-child(2)").text.strip())
        benzin.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(5) > td:nth-child(2)").text.strip())
        benzin.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(29) > td:nth-child(2)").text.strip())
        
        dizel.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(2) > td:nth-child(3)").text.strip())
        dizel.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(3) > td:nth-child(3)").text.strip())
        dizel.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(4) > td:nth-child(3)").text.strip())
        dizel.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(5) > td:nth-child(3)").text.strip())
        dizel.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(29) > td:nth-child(3)").text.strip())

        lpg.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(2) > td:nth-child(5)").text.strip())
        lpg.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(3) > td:nth-child(5)").text.strip())
        lpg.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(4) > td:nth-child(5)").text.strip())
        lpg.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(5) > td:nth-child(5)").text.strip())
        lpg.append(soup.select_one("#fuelPricesTableDesktop > tbody > tr:nth-child(29) > td:nth-child(5)").text.strip())

        df = pd.DataFrame({"Şehir":citys, "Benzin":benzin, "Dizel":dizel, "LPG":lpg})
        print(df)
    
fiyatlar()