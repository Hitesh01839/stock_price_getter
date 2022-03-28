import requests
from bs4 import BeautifulSoup

company_name = input("Which company stock do you want to check? ")

url = f"https://markets.businessinsider.com/searchresults?_search={company_name}"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

company_table = doc.find(class_="table__tbody")

the_table = company_table.find(class_="table__td")
company_link = the_table.a

attributes = company_link['href']

url = f"https://markets.businessinsider.com{attributes}"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
price_section = doc.find(class_="price-section-with-button")
price = doc.find(class_="price-section__current-value").string
print(f"The stock value currently is ${price}")
