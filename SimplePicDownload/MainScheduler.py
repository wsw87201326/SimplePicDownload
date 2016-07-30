# coding:utf-8
import multiprocessing
from SimplePicDownload.AnalysisProcess import AnalysisProcess

from SimplePicDownload.DownProcess import DownProcess


class MainScheduler:
    @staticmethod
    def startDownload(url, save_url):
        msg_queue = multiprocessing.JoinableQueue()
        analysis = AnalysisProcess(msg_queue, url)
        down = DownProcess(save_url, msg_queue)

        analysis.start()
        down.start()

        analysis.join()
        down.join()
        print('今日糗百已经下载完毕.......')
