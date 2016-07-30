# coding:utf-8
import multiprocessing
from urllib import parse

import requests
from time import sleep

from bs4 import BeautifulSoup


class AnalysisProcess(multiprocessing.Process):  # 内容获取线程
    headers = {
        'Host': 'www.qiushibaike.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Referer': 'http://www.qiushibaike.com/',
        'Connection': 'keep-alive'
    }

    def __init__(self, msg_queue, url):
        multiprocessing.Process.__init__(self)
        self.url = url
        self.msg_queue = msg_queue

    def run(self):
        while True:
            try:
                html_text = self.__startCrawl(self.url)
                if html_text is not None:
                    content_list, next_url = self.__startAnalysis(html_text)
                    if content_list is not None:  # 内容不为空
                        self.msg_queue.put(content_list)
                    if next_url is None:  # 没有下一页了,结束分析
                        self.msg_queue.put('over')
                        break
                    elif next_url is '':
                        print('分析完毕')
                        self.msg_queue.put('over')
                        break
                    else:  # 有下一页,继续分析
                        new_full_url = parse.urljoin(self.url, next_url)
                        print('开始分析下一页 %s ' % new_full_url)
                        self.url = new_full_url
                else:
                    self.msg_queue.put('over')
                    break
            except Exception as e:
                print(e)
                self.msg_queue.put('over')
                break

    def __startCrawl(self, url):  # 爬取器
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return r.text
            else:  # 503,500等错误，访问被拒绝的错误,再次尝试,5次
                for i in range(5):
                    print('访问出现%s错误，等待一秒后重试,当前重试次数:%d' % (r.status_code, (i + 1)))
                    sleep(1)  # 设置重试次数为1秒
                    r = requests.get(url, headers=self.headers)
                    if r.status_code == 200:
                        return r.text
                return None  # 说明已经无药可救,GG
        except Exception as e:
            print(e)
            return None

    def __startAnalysis(self, data):  # 分析器
        try:
            soup = BeautifulSoup(data, "lxml")
            contents = soup.select(".article > .content")
            content_list = []
            next_url = ''
            for text_content in contents:
                content = text_content.get_text(strip=True)
                result = ' '.join(filter(lambda x: x, content.split(' ')))
                content_list.append(result)
            tag_list = soup.select('.pagination > li > a')
            for tag in tag_list:
                if tag.get_text(strip=True) == '下一页':
                    next_url = tag.get('href')
            return content_list, next_url
        except Exception as e:
            print(e)
            print('分析网页 %s 时出现错误' % data)
            return None, None
