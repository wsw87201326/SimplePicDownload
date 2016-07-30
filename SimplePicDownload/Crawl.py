# coding:utf-8
from time import sleep

import requests

headers = {
    'Host': 'www.qiushibaike.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': 'http://www.qiushibaike.com/',
    'Connection': 'keep-alive'
}


def crawlHtml(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        else:  # 503,500等错误，访问被拒绝的错误,再次尝试,5次
            for i in range(5):
                print('访问出现%s错误，等待一秒后重试,当前重试次数:%d' % (r.status_code, (i + 1)))
                sleep(1)  # 设置重试次数为1秒
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    return r.text
            return None  # 说明已经无药可救,GG
    except Exception as e:
        print(e)
        return
