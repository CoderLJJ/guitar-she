import os
import requests
from bs4 import BeautifulSoup
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
https://www.it610.com/article/1290633329900593152.htm  处理canvas
'''

class Guitar:

    def __init__(self):
        #self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
        self.option = webdriver.ChromeOptions()
        # 设置为开发者模式，避免被识别
        self.option.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()

    def url_list(self):
        self.data = xlrd.open_workbook('guitar.xlsx')
        self.table = self.data.sheets()[0]
        self.links = self.table.col_values(int(2))[1:]

    def file(self):
        # 自动创建qupu文件夹
        if not os.path.exists('video'):
            os.mkdir('video')

    def page(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e)
        self.wait = WebDriverWait(self.driver, 10, 0.2)  # 设置等待时间
        try:
            self.title = self.driver.find_element_by_xpath(
                '//*[@class="gb-title"]').text
            self.imgs = self.driver.find_elements_by_xpath(
                '//*[@class="imgtab maintabview"]/ignore_js_op/picture/img')
            # print(self.title,self.imgs)
            '''
            self.im = self.wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, 'canvas')), message="不存在图片")
            print(len(self.im))
            '''
            # self.im.screenshot(f'search.png')
        except Exception as e:
            print(e)

    def get_img(self):
        for a in self.links:
            self.page(a)
            try:
                n = 1
                for i in self.imgs:
                    url = i.get_attribute('src')
                    print(url)
                    r = requests.get(url)
                    # 将获取到的图片二进制流写入本地文件
                    # try:
                    if '.jpg' in url:
                        with open(f"video//{self.title}{n}.jpg", 'wb') as f:
                            # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
                            f.write(r.content)
                            f.close()
                            print("下载成功!")
                            n += 1
                    elif '.png' in url:
                        with open(f"video//{self.title}{n}.png", 'wb') as f:
                            # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
                            f.write(r.content)
                            f.close()
                            print("下载成功!")
                            n += 1
                    elif '.gif' in url:
                        with open(f"video//{self.title}{n}.gif", 'wb') as f:
                            # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
                            f.write(r.content)
                            f.close()
                            print("下载成功!")
                            n += 1
                    else:
                        pass
            except:
                pass
                # canvas =self.driver.find_elements_by_xpath('//*[@class="alphaTabSurface"]/canvas')
                # # canvas = self.driver.find_element_by_tag_name('canvas')
                # print(canvas)
                # e = 1
                # for c in canvas:
                #     c.screenshot(f"video//{self.title}{e}.png")
                #     e+=1



if __name__ == '__main__':
    # 程序入口
    g = Guitar()  # 实例化类 初始化
    g.url_list()  # 调用函数
    g.file()
    g.get_img()
