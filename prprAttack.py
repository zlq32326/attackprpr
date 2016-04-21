# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import cookielib
import os
import requests
import web
# import wx

def getimg(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()

'''創建文件目录，并返回该目录'''
def mkdir(path):
    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

'''
保存文件到本地
@path  本地路径
@file_name 文件名
@data 文件内容
'''
def save_file(path, file_name, data):
    if data == None:
        return
    mkdir(path)
    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()

def Attack(path):
    #定义一个要提交的数据数组(字典)
    pageIndex = 47;

    Formdata = {}
    Formdata['cache'] = {"id":10060,"cacheid":"mdZnfkEwJX9MtrgfnhTV"}
    Formdata['oper'] = "listimages"
    Formdata['data'] = {"pageIndex":pageIndex}

    #设置Headers
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {
            'Origin':'http://www.prprleg.com',
            'Referer':'http://www.prprleg.com/',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            #  'Content-Length':120,
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'prprleg.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
     }



    #定义post的地址
    url = 'http://prprleg.com/Mprpr/m'
    post_data = urllib.urlencode(Formdata)

    #提交，发送数据
    request = urllib2.Request(url, post_data, headers)
    response = urllib2.urlopen(request)

    #获取提交后返回的信息
    page = response.read()
    print page
    #使用正则表达式提取地址
    pattern = re.compile('{"id":(.*?),"url":"(.*?)","upload_time":".*?"}',re.S)
    result = re.findall(pattern,page)

    for i in result:
        print i[0]
        print i[1]
        # save_file (path, i[0] + ".jpg", getimg("http://cdn.img.prprleg.com/" + i[1]))
        # print i[1] + "获取成功"

Attack("D:/prprleg/")

# urls = (
#     '/(.*)', 'hello'
# )
# app = web.application(urls, globals())
#
# class hello:
#     def GET(self, name):
#         if not name:
#             name = 'World'
#         return 'Hello, ' + name + '!'
#
# if __name__ == "__main__":
#     app.run()
