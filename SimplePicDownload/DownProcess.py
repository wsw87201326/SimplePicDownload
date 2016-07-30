# coding:utf-8
from datetime import datetime
import multiprocessing
import time
import os


class DownProcess(multiprocessing.Process):
    def __init__(self, save_url, msg_queue):
        multiprocessing.Process.__init__(self)
        self.save_url = save_url
        self.msg_queue = msg_queue

    def run(self):
        while True:
            if not self.msg_queue.empty():  # 当queue不为空的时候进入
                msg = self.msg_queue.get()
                if type(msg) is list:
                    print(type(msg))
                    today_time = datetime.now().strftime('%F')
                    if not os.path.exists(self.save_url):
                        os.makedirs(self.save_url)
                    real_save_url = self.save_url + today_time + '.txt'
                    print('正在向||||' + real_save_url + '|||||中写入')
                    success_num = 0
                    with open(real_save_url, 'a', encoding='utf-8') as txt_file:
                        for content in msg:
                            content += '\n'
                            try:
                                txt_file.write('--  ' + content)
                                success_num += 1
                            except UnicodeEncodeError:
                                print('出现错误。放弃写入')
                                # 这是取序号的方法
                                # for index, content in enumerate(content_list):
                                #     number = index + 1
                                #     print(str(number) + "." + content)
                    print('文件写入完成 %d/%d , 失败个数: %d' % (success_num, len(msg), (len(msg) - success_num)))
                else:
                    break
            else:
                time.sleep(1)  # 等待1秒后再取数据
