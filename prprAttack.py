# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import cookielib
import os
import requests


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



#定义一个要提交的数据数组(字典)
Formdata = {}
Formdata['cahe'] = {"id":0,"cacheid":""}
Formdata['oper'] = "listimages"
Formdata['data'] = {}

#设置Headers
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'  ,
#                        'Referer':'http://prprleg.com/test' }

#定义post的地址
url = 'http://prprleg.com/Mprpr/m'
post_data = urllib.urlencode(Formdata)

#提交，发送数据
request = urllib2.Request(url, post_data)
response = urllib2.urlopen(request)

#获取提交后返回的信息
#print response.read()
page = response.read()

#使用正则表达式提取地址
pattern = re.compile('{"id":(.*?),"url":"(.*?)","upload_time":".*?"}',re.S)
result = re.findall(pattern,page)


for i in result:
    # print i[0]
    # print i[1]
    save_file ("F:/play/", i[0] + ".jpg", getimg("http://cdn.img.prprleg.com/" + i[1]))
    print i[1] + "获取成功"
