from bs4 import BeautifulSoup
import requests

def get_data():
    """
    :return: list[tuple] -> [(fuel, price)...]
    """
    url = "https://www.micm.gob.do/direcciones/combustibles"

    r = requests.get(url)#hmtl content

    soup = BeautifulSoup(r.content, "html.parser")

    fuels_and_prices = []#Prices and fuels

    #Traverse the list that contain fuels and price and adding to fuels_and_prices list
    for cost in list(soup.find_all("tr"))[1:]:
        cost_str = cost.getText()#cost to string
        middle = cost_str.index("RD")#For divide the fuel of the price in the string
        fuel = cost_str[:middle]#Fuel string
        price = cost_str[middle:]#Price string
        fuel_and_price = (fuel, price)#Tuple with fuel and price
        fuels_and_prices.append(fuel_and_price)
        

    return fuels_and_prices
