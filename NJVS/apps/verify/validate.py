# encoding: utf-8
import re
import requests
from hashlib import md5

class Validate(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def judge(self):
        self.httpclient = requests.Session()
        self.rooturl = 'http://202.119.81.112:9080'
        data = {
            'method' : 'verify',
            'USERNAME' : self.username.encode('utf-8'),
            'PASSWORD' : md5(self.password.encode('utf-8')).hexdigest().upper()
        }
        r = self.httpclient.get(self.rooturl + '/njlgdx/xk/LoginToXk', params=data)
        if (r.url == self.rooturl + '/njlgdx/framework/main.jsp'):
            return True
        else:
            self.httpclient.cookies.clear()
            return False

    def fetch_info(self):
        res = self.httpclient.get(self.rooturl + '/njlgdx/grxx/xsxx')
        pattern = re.compile('<table\sid=\"xjkpTable\".*?>.*?' +
        '<tr.*?>.*?</tr>.*?' +
        '<tr.*?>.*?</tr>.*?' +
        '<tr.*?>.*?' +
        '<td.*?>院系：(?P<department>.*?)</td>.*?' +
        '<td.*?>专业：(?P<major>.*?)</td>.*?<td.*?>.*?</td>' +
        '<td.*?>班级：(?P<class>.*?)</td>.*?' +
        '<td.*?>学号：(?P<studentID>.*?)</td>.*?' +
        '</tr>.*?' +
        '<tr.*?>.*?' +
        '<td.*?>姓名</td>.*?' +
        '<td.*?>&nbsp;(?P<name>.*?)</td>.*?' +
        '<td.*?>性别</td>.*?' +
        '<td.*?>&nbsp;(?P<gender>.*?)</td>.*?' +
        '</tr>', re.S)
        res.encoding = 'utf-8'       
        info = re.search(pattern, res.text)
        if (info == None):
            return {
                'flag' : False
            }
        else:
            return {
                'flag' : True,
                'department' : info.group('department'),
                'major' : info.group('major'),
                'class' : info.group('class'),
                'studentID' : info.group('studentID'),
                'name' : info.group('name'),
                'gender' : info.group('gender')
            }

        
if __name__ == '__main__':
    v = Validate('914106840629', '174511')
    if (v.judge()) :
        print v.fetch_info()
        