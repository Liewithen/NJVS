# encoding: utf-8
import re
import requests
from hashlib import md5
from verify.models import UserValidate
from users.models import User

class Validate(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.jwc_pwd = md5(self.password.encode('utf-8'))

    def judge(self):
        self.httpclient = requests.Session()
        self.rooturl = 'http://202.119.81.112:9080'
        data = {
            'method' : 'verify',
            'USERNAME' : self.username.encode('utf-8'),
            'PASSWORD' : self.jwc_pwd.hexdigest().upper()
        }
        r = self.httpclient.get(self.rooturl + '/njlgdx/xk/LoginToXk', params=data)
        try:
            u = UserValidate.objects.get(username=self.username)
            u.validate = 0
            u.save()
        except UserValidate.DoesNotExist:
            UserValidate.objects.create(username=self.username, validate=0)
        if (r.url == self.rooturl + '/njlgdx/framework/main.jsp'):
            print self.username + ' is OK'
            u = UserValidate.objects.get(username=self.username)
            u.validate = 1
            u.save()
            return True
        else:
            print self.username + ' is Faild'
            u = UserValidate.objects.get(username=self.username)
            u.validate = 2
            u.save()
            self.httpclient.cookies.clear()
            return False

    def fetch_info(self):
        res = self.httpclient.get(self.rooturl + '/njlgdx/grxx/xsxx')
        pattern = re.compile('<table\sid=\"xjkpTable\".*?>.*?' +
        '<tr.*?>.*?</tr>.*?' +
        '<tr.*?>.*?</tr>.*?' +
        '<tr.*?>.*?' +
        '<td.*?>院系：(?P<department>.*?)</td>.*?' +
        '<td.*?>专业：(?P<major>.*?)</td>.*?' +
        '</tr>.*?<tr.*?>.*?' + 
        '<td.*?>姓名</td>.*?<td.*?>&nbsp;(?P<name>.*?)</td>.*?' +
        '<td.*?>性别</td>.*?<td.*?>&nbsp;(?P<gender>.*?)</td>.*?</tr>'
        , re.S)    
        info = re.search(pattern, res.content)
        if info.group('gender') == '男':
            g = 'male'
        else:
            g = 'female'
        try:
            u = User.objects.get(username=self.username)
            u.username = self.username
            u.set_password(self.password)
            u.real_name = info.group('name')
            u.gender = g
            u.department = info.group('department')
            u.major = info.group('major')
            u.roles = 1
            u.save()
        except User.DoesNotExist:
            User.objects.create_user(username=self.username,
                                password = self.password,
                                real_name = info.group('name'),
                                gender = g,
                                department = info.group('department'),
                                major = info.group('major'),
                                roles = 1)
        
        