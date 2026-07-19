import requests
from bs4 import BeautifulSoup 

url ="https://www.meesho.com/search?q=kurti"

headers ={
    "User-Agent": "Mozilla/5.0",
    "Accept-Language" : "en-IN,en;q=0.9"
}

response = requests.get(url,headers=headers)

if response.status_code!=200 : 
      print("Fialed to fetch page !")
      exit()
      
soup=BeautifulSoup(resposne.text,"lxml")

product_names =soup.find_all("p")
prices =soup.find ("h5")

print("Meesho Product: \n")

for name, price in zip(product_names[:10],price [:10]):
     product_name = name.tetx.strip()
     product_price = price.text.strip()
     
     
     if "₹" in product_price :
               print(f"Product:{product_name}")
               print(f"Price:{product_price}")
               print("-"*50)
    
