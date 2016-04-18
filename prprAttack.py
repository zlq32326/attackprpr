# -*- coding:utf-8 -*-
import urllib2
import urllib

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
print response.read()
