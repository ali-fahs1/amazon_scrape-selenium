import os
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class crawledArticle:
    def __inti__(self,title,price):
        self.title=title
        self.price=price

class bot:
    def article(self,name):
        count=2
        page=1
        pageIncrement=10
        maxRetrieves=100
        a=[]
        os.environ['PATH'] += r"C:\seleniumdriver"

        url=f"https://www.amazon.com/s?k={name}&page={str(page)}"
        #####
        Options =webdriver.ChromeOptions()
        #####
        # Options.headless=False
        
        Options.add_experimental_option("detach",True)
        browser= webdriver.Chrome(options=Options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(7)

        while True:
            # try:
                if pageIncrement*page >maxRetrieves:
                   break
                if count > pageIncrement:
                    count=2
                    page+=1

                #get title
                xpath=f'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
                title=browser.find_element(By.XPATH, xpath)
                title_text=title.get_attribute("innerHTML")
                title.click()
                
                
                #get price
                # price_xpath="/html/body/div[1]/div[2]/div[10]/div[5]/div[1]/div[6]/div/div[1]/div/div/form/div/div/div/div/div[2]/div[1]/div/span[1]/span[2]"
                # price=browser.find_element(By.XPATH, price_xpath)
                # price_text=price.get_attribute("inner.HTML")
                


                # url=f"https://www.amazon.com/s?k={name}&page={str(page)}"
                # browser.get(url)
                # browser.set_page_load_timeout(7)
                 

                # info=crawledArticle(title_text,price_text)
                # a.append(info)
            # except Exception as e:
            #     print("Exception",e)


                

                
              
              
            
          
        browser.close()
        return a
    



fetcher =bot()
fetcher.article("iphone 11")
# with open("results.csv","w",newline="",encoding="utf-8") as csvfile:
#  articleWriter=csv.writer(csvfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
#  for article in fetcher.article("iphone11"):
#      articleWriter.writerow([article.title_text,article.price_text])
