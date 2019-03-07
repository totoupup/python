#!/usr/bin/python
#encoding: utf-8

import urllib.request
import re
import os
import random
import time
import socket
from hashlib import md5

rootDir = r"D:\03code\Python\UrlLib\BeautyImages\mm131"
try:
    os.mkdir(rootDir)
except:
    print ("目录已经存在，继续下载")

agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1']

#标识是第一次尝试下载图片
firstTime = True

# 下载图片
def getimg(imgUrl, path):
    global firstTime
    try:
        #下载并保存图片
        f = open(path, 'wb')
        req = urllib.request.Request(imgUrl)
        req.add_header('User-Agent', random.choice(agents))  # 换用随机的请求头
        pic = urllib.request.urlopen(req, timeout = 10)
        f.write(pic.read())
        f.close()
        print(imgUrl + ' 下载完成!')
    except Exception:
        #如果下载失败则重试
        if firstTime:
            print(imgUrl + ' 下载失败,重试...')
            firstTime = False
            getimg(imgUrl, path)
        # else:
        #     firstTime = True
        firstTime = True       
# https://www.169tp.com/
# date = 201812
# imgSet = [100,101,103,104,120]#201812
date = 201901
imgSet = ["094",108,120]#201901
# date = 201902
# imgSet = [114,103,104,107,109,110,112,114,117]#201902
for i in imgSet:
    for j in range(1, 50):
        path = rootDir + "\\" + str(date) + str(i)
        if not os.path.exists(path):
            os.makedirs(path)
        url = "http://724.169pp.net/169mm/" + str(date) + "/" + str(i) + "/" + str(j) + ".jpg"        
        getimg(url, os.path.join(path, str(j) + ".jpg"))

#001获得整个页面
def get_html(url):
    socket.setdefaulttimeout(10)
    papg = urllib.request.urlopen(url)
    html = papg.read()
    html = html.decode("gbk")
    #html = unicode(html, "gbk").encode("utf8")
    return html
	
#002   获得总页码数
def get_page_num(html,url_num):
    szurlre = re.compile(r'<a href=\'list_'+str(url_num)+'_(\d+).html\' class="page-en">末页')
    szresult = re.findall(szurlre, html)
    if len(szresult) == 0:
        page_num = 0
    else:
        page_num = int(szresult[0])
    print("pagenum:",page_num)
    return page_num
	
#003 获得相册
def get_ablum_list(base_url,html):
	#http://www.mm131.com/qipao/2288.html
    print(base_url)
    szurlre = re.compile(base_url+r'(\d+.html)')
    ablum_list = re.findall(szurlre, html);
    print("----------len-----------:",len(ablum_list))
    return ablum_list	

#004 获得单页的图片
def get_photo(html, photo_num, ablum):
    imgre = re.compile(r'(http://\S+.jpg)')
    imglist = re.findall(imgre, html)
    #print("len_imglist",len(imglist))
    for imgurl in imglist:
        print(imglist)
        path = rootDir + "\\" + ablum
        if not os.path.exists(path):
            os.makedirs(path)
        getimg(imgurl, os.path.join(path, imgurl.split("/")[-1]), imgurl)
        photo_num = photo_num + 1

        try:
            socket.setdefaulttimeout(2)
            #urllib.request.urlretrieve(imgurl, unicode('.\\photo\\%s\%05d.jpg'%(dir, photo_num), "utf8"))
            store_path='.\\mm131\\' + '\\'+ md5(imgurl.encode("utf8")).hexdigest() + "." + 'jpg'
            #print("#######:",store_path)
            urllib.request.urlretrieve(imgurl, store_path)
            print("正在下载第%s张图片"%photo_num)
            photo_num = photo_num + 1
        except:
            continue
    return photo_num	
	
"""
#test
html=get_html("http://www.mm131.com/chemo/")
get_page_num(html,3)
"""
print("123")

url_list=["http://www.mm131.com/qingchun/","http://www.mm131.com/xiaohua/","http://www.mm131.com/chemo/","http://www.mm131.com/qipao/","http://www.mm131.com/mingxing/","http://www.mm131.com/xinggan/"]
# url_list=["http://www.mm131.com/xinggan/"]
url_list=["http://www.mm131.com/qingchun/"]
url_num=1
for baseurl in url_list:
	base_url=baseurl
	print(base_url)
	html=get_html(base_url)
	print(url_num)
	page_num=get_page_num(html,url_num)
	for i in range(1,page_num):
		try:
			if i!=1: 
				baseurl=baseurl+"list_"+str(url_num)+"_"+str(i)+".html"
				html=get_html(baseurl)
			else:
				pass
			ablumlist=get_ablum_list(base_url,html)
			for find_url in ablumlist:
				photo_html=get_html(base_url+find_url)	
				photo_num=0
				photo_num = get_photo(photo_html, photo_num, find_url.split(".")[0])
		except:
			continue		
	url_num=url_num+1	