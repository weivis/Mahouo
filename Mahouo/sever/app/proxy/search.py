import re, urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup as BS
import time
import socket 

def getsearch(content, page):

    #传入搜索页数
    if page == 1 or page == 0:
        page_nbr = 0
    else:
        page_nbr = (page-1) *9

    #默认搜索路径
    baseUrl = 'https://cn.bing.com/search?'

    #转换用户搜索内容
    search_data = content.encode(encoding='utf-8', errors='strict')

    #判断搜索页数范围
    if page == 0:
        data = {'q':search_data}
    else:
        data = {'q':search_data, 'sp1':-1, 'pq':'b', 'qs':'n', 'sc':'0-1', 'first':page_nbr, 'FORM':'PERE'}#, 'FORM':'PERE'

    #获取方式
    data = urllib.parse.urlencode(data)
    url = baseUrl+data #url主体
    print(url)

    #请求
    try:
        html = urllib.request.urlopen(url)
    except:
        html = 'error'

    #定义对象
    soup = BS(html,"html.parser")
    #获取所有li对象
    li = soup.findAll("li", class_='b_algo')

    listdata = []

    if html == 'error':
        pass
    else:

        try:
            datapcs = soup.find('span',attrs={"class": "sb_count"}).get_text()
        except:
            datapcs = '未知'

        #遍历出li的内容
        for i in li:
            title = i.find('h2') #获取li-h2标签内容
            a = i.find('a')['href'] #获取li-a内容
            p = i.find('p') #获取li-p内容
            content = p.get_text()
            title = title.get_text() #title输出为纯文本

            val = {"_source":{'title':title, 'content': content, 'url': a}}
            listdata.append(val)

        data = {
            "hits": {"total": datapcs, "hits":listdata},
        }

    return(data)