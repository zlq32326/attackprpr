# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import cookielib
import os
import requests

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
抓取网页文件内容，保存到内存

@url 欲抓取文件 ，path+filename
'''
def get_file(url):
    try:
        cj=cookielib.LWPCookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

        req = urllib2.Request(url)
        operate=opener.open(req)
        data=operate.read()
        return data
    except Exception as e:
        print e
        return None

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


class Spider:
    def __init__(self):
        self.siteURL = 'http://prprleg.com/test/'

    def getPage(self):
        #url = self.siteURL + "?page=" + str(pageIndex)
        url = self.siteURL #+ str(pageIndex)
        #headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        #            ,'Referer' : 'http://www.bilibili.com/'}
        #request = urllib2.Request(url,None,headers)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getimg(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getContents(self):
        page = self.getPage()
        #print page
        #pattern = re.compile('<div class="preview.*?>(.*?)</div>',re.S)
        #pattern = re.compile('<a class="i-link" href="http://www.bilibili.com/account/history">(.*?)</a>',re.S)
        #pattern = re.compile('data-title="registerImage"><img src="(.*?)" alt=".*?" title=".*?" border=".*?" /><div class="zoom-message">',re.S)
        pattern = re.compile('',re.S)
        result = re.search(pattern,page)
        if result:
            print '获取图片成功'
            #print result.group(1)  #测试输出
            save_file ("F:/play/", "123123.TXT", spider.getPage(result.group(1)))
            #return result.group(1).strip()
        else:
            print '获取图片失败'
            #return None

        #pattern = re.compile('<li class="work  "><a href="/member_illust.php\?mode=medium&amp;illust_id=(.*?)"><img src=',re.S)
        #result = re.findall(pattern,page)
        # if result:
        #     print '获取下一页成功'
        #     print result[3]
        #     #print result.group(2)  #测试输出
        #     #self.getContents(result[3])
        # else:
        #     print '获取下一页失败'
        #     #return None


#
# spider = Spider()
# spider.getContents()


#save_file ("F:/play/", "123123.TXT", spider.getimg('http://prprleg.com/test/'))


#定义post的地址
url = 'http://www.jdlingyu.org/page/2/'
#提交，发送数据
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()
# print page
pattern = re.compile('original=\'http://www.jdlingyu.org/wp-content/uploads/thumbnail(.*?)_200.jpg\' width=\'200\' height=',re.S)
result = re.findall(pattern,page)
for i in result:
    try:
        jpgurl = 'http://www.jdlingyu.org/wp-content/uploads/2016/02'+i+'.jpg'
        print "打开" + jpgurl + "中"
        request = urllib2.Request(jpgurl)
        print "第一步完成"
        response = urllib2.urlopen(request)
        print "第二步完成"
        page = response.read()
        print "保存中"
        save_file ("F:/play/", i + ".jpg",page)
        print i+ "保存成功"
    except Exception as e:
        print i+ "保存失败"
        raise
