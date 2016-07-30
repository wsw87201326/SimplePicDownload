# coding:utf-8
from SimplePicDownload.MainScheduler import MainScheduler

if __name__ == '__main__':
    page = 0
    url = 'http://www.qiushibaike.com/text/'
    save_url = 'E:\\qsbk\\'
    MainScheduler.startDownload(url, save_url)
