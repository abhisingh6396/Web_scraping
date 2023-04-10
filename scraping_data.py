# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 01:53:49 2023

@author: singh
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as rq
from bs4 import BeautifulSoup as bs

Product_name = []
Price = []
Description = []
Review = []

for i in range (1,4):
    
    
    url = "https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+under+10000%7CMobiles&requestId=5ae9623d-a8ef-4f3d-8eb6-c9cba9b94a22&page="+str(i)
    
    r = rq.get(url)
    soup = bs(r.text , "lxml")
    
    
    box_page = soup.find("div",class_="_1YokD2 _3Mn1Gg")
    name =box_page.find_all("div",class_="_4rR01T")
    
    
    ##print(name)
    for i in name:
        name=i.text
        Product_name.append(name)
        
    ##print(Product_name) 
    print(len(Product_name))
    
    prices = box_page.find_all("div",class_="_30jeq3 _1_WHN1") 
    
    for i in prices:
        prices=i.text
        Price.append(prices)
        
    ##print(Price) 
    print(len(Price))
    
    
    description = box_page.find_all("div",class_="fMghEO") 
    
    for i in description:
        description=i.text
        Description.append(description)
        
   ## print(Description)
    print(len(Description))
    
    
    review = box_page.find_all("div",class_="_3LWZlK") 
    
    for i in review:
        review=i.text
        Review.append(review)
        
    ##print(Review)
    print(len(Review))

data_frame= pd.DataFrame({"Product Name": Product_name,"Prices":Price,"Description":Description,"Reviews":Review})
#print(data_frame)

data_frame.to_csv("F:/flipkart_electronics_scrap.csv")
   



                       




