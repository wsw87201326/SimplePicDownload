from SimplePicDownload.Analyzer import startAnalysis
from SimplePicDownload.Crawl import crawlHtml
from SimplePicDownload.Down import downContent


class MainScheduler:
    @staticmethod
    def startDownload(url, save_url):
        html = crawlHtml(url)
        content_list = startAnalysis(html)
        downContent(content_list, save_url)

        print('success!~~~')
