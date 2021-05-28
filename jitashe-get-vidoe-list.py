'''
//*[@class="text"]/a
'''
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
'''
https://www.jitashe.org/guide/newtab/
https://www.jitashe.org/guide/hottab/
'''

def get():
    infos = []
    for i in range(1, 5):
        # url = 'https://www.jitashe.org/guide/hottab/t4/' + str(i)
        # url = 'https://www.jitashe.org/guide/hottab/' + str(i)
        url = 'https://www.jitashe.org/guide/newtab/t4/' + str(i)
        html = requests.get(
            url, headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
            timeout=30)  # 获取网页
        dom = etree.HTML(html.text)
        titles = dom.xpath("//*[@class='text']/a/text()")
        print(titles[0])
        urls = dom.xpath('//*[@class="text"]/a')
        for i in range(60):
            info = []
            print(i)
            url = 'https://www.jitashe.org/' + urls[i].get('href')
            title = titles[i]
            print(url)
            print(title)
            info.append(title)
            info.append(url)
            infos.append(info)
        df = pd.DataFrame(infos, columns=['title', 'urls'])
    df.to_excel('guitar_newtab_t4.xlsx', encoding='utf-8')


if __name__ == '__main__':
    get()
