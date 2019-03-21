#!/usr/bin/python
# coding=utf-8
import requests
import unittest

#class TestLogin(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
        #cls.login_url = 'http://lcrmmanagement.lunztech.cn/Login/Index?ReturnUrl=%2F#/dashboard'
        #cls.info_url = 'http://127.0.0.1:5000/info'
        #cls.username = 'wangxiaowen'
        #cls.password = '654321'
def test_login():
        """
        测试登录
        """
        data = {
            'username': 'wangxiaowen',
            'password': '654321'
        }
        response = requests.post('http://lcrmapi.lunztech.cn/api/membership/login?appKey=69800851-4554-4EEC-8D12-E4211B952798', data=data).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'
'''    def test_info(self):
        """
        测试info接口
        """
        data = {
            'username': self.username,
            'password': self.password
        }
        response_cookies = requests.post(self.login_url, data=data).cookies
        session = response_cookies.get('session')
        assert session
        info_cookies = {
            'session': session
        }
        response = requests.get(self.info_url, cookies=info_cookies).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'
        '''
        
if __name__ == '__main__':
        test_login()