import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from openpyxl import load_workbook, Workbook

import time

# 类开头字母大写
class Thief():
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def handle(self):
        self.goods_url_list = self.reader.read()
        for goodsURL in self.goods_url_list:
            try:
                result = self.steal(goodsURL)
            except:
                print("Failed to obtain goods information:", goodsURL)
                continue
            print("Success:", result["title"])
            self.writer.write(result)

        self.writer.save()

    # 从目标获取数据源
    def steal(self, url):  return dict()

class SimpleThief(Thief):
    HOST = "http://p.zwjhl.com"
    PRICE_API = "/price.aspx?url="

    def __init__(self, reader, writer):
        super(SimpleThief, self).__init__(reader, writer)

    def steal(self, url):
        # 拼接url 发起请求
        targetURL = SimpleThief.HOST + SimpleThief.PRICE_API + url
        req = requests.get(targetURL)

        # 从返回里提取需要的字段 存到result里
        soup = BeautifulSoup(req.text, "html.parser")
        Prices = soup.find("span", attrs={"style": "color: #333; font-size: 14px;"}).text.split()
        lowprice = float(Prices[2])
        highprice = float(Prices[4].split("：")[1])
        differ = highprice - lowprice
        result = {
            "title": soup.title.text.lstrip().split("--")[0],
            "source": Prices[0],
            "lowdate": Prices[3][1:-1],
            "lowprice": (lowprice),
            "hgigprice": (highprice),
            "differ": (differ)
        }
        return result

class CronThief(Thief):
    pass


class SelenThief(Thief):
    AGEN = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    HOST = "https://www.gwdang.com"
    TREND_API = "/trend?url="


    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chrome_options)

    def __init__(self, reader, writer):
        super(SelenThief, self).__init__(reader, writer)

    def steal(self,url):
        
        targetURL = SelenThief.HOST + SelenThief.TREND_API + url

        SelenThief.driver.get(targetURL)
        SelenThief.driver.implicitly_wait(10)
        lowprice = SelenThief.driver.find_element_by_id("ymj-min").text
        lowdata = SelenThief.driver.find_element_by_id("ymj-min-date").text
        highprice = SelenThief.driver.find_element_by_class_name("current-price").text
        # list1 = [lowdata.text,lowprice.text,highprice.text]
        # html = driver.execute_script("return document.documentElement.outerHTML")


        result = {
            "title": '-',
            "source": '-',
            "lowdate": lowdata,
            "lowprice": (lowprice),
            "hgigprice": (highprice),
            "differ": '-'
        }

        # print(result)
        return result
