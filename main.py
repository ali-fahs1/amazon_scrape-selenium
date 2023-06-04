import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv

os.environ['PATH'] += r"C:\seleniumdriver"


name=input("enter the keyword: ")
count=2
page=1
pageIncrement=16
maxRetrieves=0


url=f"https://www.amazon.com/s?k={name}&page={str(page)}"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)
a=[]
b=[]

while maxRetrieves<2:
    
    # if pageIncrement*page>maxRetrieves:
    #     break
    if count >pageIncrement:
        count=2
        page+=1 
    
    try: ##get title
        xpath =f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
        title=driver.find_element(By.XPATH,xpath)
        title_text=title.get_attribute("innerHTML")
        driver.implicitly_wait(10)
        title.click()
        print(title_text)
        a.append(title_text)
        
            ##get price
        xpath_price= '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]' 
        price_title=driver.find_element(By.XPATH,xpath_price)
        driver.implicitly_wait(10)

        price_text=price_title.get_attribute("innerHTML")
        print(price_text)
        b.append(price_text)
    except Exception as e:
        print(e)
       


    count+=1
    maxRetrieves+=1

    url=f"https://www.amazon.com/s?k={name}&page={str(page)}"
    driver.get(url)
    driver.implicitly_wait(10)
    print("------------------------------------")

                 
with open('result.csv','w',newline="",encoding='utf-8') as csvfile:
    articlewriter=csv.writer(csvfile,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    articlewriter.writerows([a,b])
    
    
    

