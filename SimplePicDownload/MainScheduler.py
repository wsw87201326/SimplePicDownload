from SimplePicDownload.Analyzer import startAnalysis
from SimplePicDownload.Crawl import crawlHtml
from SimplePicDownload.Down import downContent


class MainScheduler:
    @staticmethod
    def startDownload(url, save_url):
        html = crawlHtml(url)
        content_list, next_url = startAnalysis(html)
        downContent(content_list, save_url)
        print('next_Url:'+next_url)
        print('success!~~~')
