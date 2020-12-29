import ssl
import requests
import json
import tkinter as tk
import urllib.request as req
import bs4
from crawlerView import *

ssl._create_default_https_context = ssl._create_unverified_context


class WooliesSpecial:
    def __init__(self):
        self.src = "https://www.woolworths.com.au/apis/ui/browse/category"
        self.root = tk.Tk()
        self.view = MainScreen(self.root, self)
        self.root.geometry("1200x800")
        self.root.title("Woolies Special")
        self.root.mainloop()

    def getSpecialCategory(self):
        self.special_list = ["Half Price", "Meats", "Fruits and Veggies"]
        return self.special_list

    def getHalfPrice(self):
        self.page_num = 1
        self.product_name = []
        self.product_price = []
        self.product_info = []
        while self.page_num > 0:

            self.payload = {"categoryId": "specialsgroup.3631",
                            "pageNumber": self.page_num,
                            "pageSize": 36,
                            "sortType": "TraderRelevance",
                            "url": "/shop/browse/specials/half-price",
                            "location": "/shop/browse/specials/half-price",
                            "formatObject": "{\"name\":\"Half Price\"}",
                            "isSpecial": "true",
                            "isBundle": "false",
                            "isMobile": "false",
                            "filters": "[]",
                            "token": ""}
            self.res = requests.post(self.src, data=self.payload)

            self.data = json.loads(self.res.text)

            self.posts = self.data['Bundles']
            if not self.posts:
                break

            for product in self.posts:
                self.product_name.append(product['Name'])
                for price in product['Products']:
                    self.product_price.append(price['Price'])
            self.product_info.append(self.product_name)
            self.product_info.append(self.product_price)
            self.page_num += 1
        return self.product_info

    def getMSDSpecial(self):
        self.page_num = 1
        self.product_name = []
        self.product_price = []
        self.product_info = []
        while self.page_num > 0:

            self.payload = {"categoryId": "1_D5A2236_SPECIALS",
                            "pageNumber": self.page_num,
                            "pageSize": 36,
                            "sortType": "TraderRelevance",
                            "url": "/shop/browse/meat-seafood-deli/meat-seafood-deli-specials",
                            "location": "/shop/browse/meat-seafood-deli/meat-seafood-deli-specials",
                            "formatObject": "{\"name\":\"Meat, Seafood & Deli Specials\"}",
                            "isSpecial": "true",
                            "isBundle": "false",
                            "isMobile": "false",
                            "filters": "[]",
                            "token": ""}
            self.res = requests.post(self.src, data=self.payload)

            self.data = json.loads(self.res.text)

            self.posts = self.data['Bundles']
            if not self.posts:
                break

            for product in self.posts:
                self.product_name.append(product['Name'])
                for price in product['Products']:
                    self.product_price.append(price['Price'])
            self.product_info.append(self.product_name)
            self.product_info.append(self.product_price)
            self.page_num += 1
        return self.product_info

    def getVegAndFruitsSpecial(self):
        self.page_num = 1
        self.product_name = []
        self.product_price = []
        self.product_info = []
        while self.page_num > 0:

            self.payload = {"categoryId": "1-E5BEE36E_SPECIALS",
                            "pageNumber": self.page_num,
                            "pageSize": 36,
                            "sortType": "TraderRelevance",
                            "url": "/shop/browse/fruit-veg/fruit-veg-specials",
                            "location": "/shop/browse/fruit-veg/fruit-veg-specials",
                            "formatObject": "{\"name\":\"Fruit & Veg Specials\"}",
                            "isSpecial": "true",
                            "isBundle": "false",
                            "isMobile": "false",
                            "filters": "[]",
                            "token": ""}
            self.res = requests.post(self.src, data=self.payload)

            self.data = json.loads(self.res.text)

            self.posts = self.data['Bundles']
            if not self.posts:
                break

            for product in self.posts:
                self.product_name.append(product['Name'])
                for price in product['Products']:
                    self.product_price.append(price['Price'])
            self.product_info.append(self.product_name)
            self.product_info.append(self.product_price)
            self.page_num += 1
        return self.product_info


if __name__ == "__main__":
    # getHalfPrice(src)
    # getMeatSpecial(src)
    WooliesSpecial()
