import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from datetime import date
from tqdm import tqdm
import time

def extract_last_page_number():
    url = "https://unique.com.mm/collections/mobile-phone"

    data = requests.get(url)

    #extract web code html,css,js,etc.
    web_data = data.text
    #print(web_data)

    #clear extracted web data
    bsObj = BeautifulSoup(web_data, "html5lib")
    page_final = bsObj.find("div", class_="pagination__nav")
    page_number_final = bsObj.find_all("a", class_="pagination__nav-item link")
    final_number = page_number_final[-1]
    page_num = int(final_number.text)
    print(page_num)
    return page_num
    
def extract_product_name(tag):
    """Extract Product Name"""
    name_tag = tag.find("a", class_="product-item__title text--strong link")
    name_tag = name_tag.text
    return name_tag
def extract_product_price(tag):
    """Extract Product Price"""
    price_tag = tag.find("span", class_="price")
    price_tag = price_tag.text
    #print(price_tag)
    price_tag = price_tag.replace("K", "").replace(",", "")
    price_tag = int(price_tag)
    return price_tag
def extract_product_status(tag, i):
    """Extract Product Status"""
    status = tag.find("span", class_=i)
    status = status.text
    return status

name_list = []
price_list = []
status_list = []




def main():
    last_page_number = extract_last_page_number()
    for i in tqdm(range(1,last_page_number+1)):
        url = "https://unique.com.mm/collections/mobile-phone" + "?page=" + str(last_page_number)
        #print(url)
        data = requests.get(url)

        #extract web code html,css,js,etc.
        web_data = data.text
        #print(web_data)

        #clear extracted web data
        bsObj = BeautifulSoup(web_data, "html5lib")

        #print(bsObj)
        #find main div
        main_tags = bsObj.find_all("div", class_="product-item__info-inner")
        #print(main_tags)
        #number = 1
        for Dummy_tag in main_tags: #tqdm is for progress meter
            try:
                #print("\n")
                #print(number)
                #print(type(Dummy_tag))
                #print(Dummy_tag)

                #Extract product name
                name = extract_product_name(Dummy_tag)
                name_list.append(name)
                #print("\n")

                price = extract_product_price(Dummy_tag)
                price_list.append(price)       
                #print("\n")
                
                status_type = ['product-item__inventory inventory',
                               'product-item__inventory inventory inventory--high',
                               'product-item__inventory inventory inventory--low']
                
                for i in status_type:        
                    try:
                        status = extract_product_status(Dummy_tag, i)
                        status_list.append(status)                
                    except:
                        continue
                #number += 1
                time.sleep(0)
            except:
                print(Dummy_tag)
                raise
                break
        #print(name_list)
        #print(price_list)
        #print(status_list)

        excel_list = {"Product Name": name_list,
                      "Product Price": price_list,
                      "Product Status": status_list}

        excel = pd.DataFrame(excel_list)
        current_time = datetime.now().strftime("%H_%M_%S")
        today = date.today().strftime("%Y-%m-%d")
        #print(today)
        #print(current_time)
        excel.to_excel("Output" + " " + today +".xlsx", index = False)
    print("To Excel is completed")
if __name__=="__main__":
    main()
    