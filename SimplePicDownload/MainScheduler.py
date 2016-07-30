# coding:utf-8
from urllib import parse
from SimplePicDownload.Analyzer import startAnalysis
from SimplePicDownload.Crawl import crawlHtml
from SimplePicDownload.Down import downContent


class MainScheduler:
    @staticmethod
    def startDownload(url, save_url):
        html = crawlHtml(url)
        if html is not None:
            content_list, next_url = startAnalysis(html)
            downContent(content_list, save_url)
            if next_url is not '':
                new_full_url = parse.urljoin(url, next_url)
                return new_full_url
            else:
                return None
        else:
            return 'Service_Error'
