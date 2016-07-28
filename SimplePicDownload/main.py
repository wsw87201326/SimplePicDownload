from SimplePicDownload.MainScheduler import MainScheduler

if __name__ == '__main__':
    page = 0
    url = 'http://www.qiushibaike.com/text/'

    save_url = 'E:\\qsbk\\'
    while True:
        url = MainScheduler.startDownload(url, save_url)
        print(url)
        page += 1
        print(str(page) + "下载完毕")
        if url is 'Service_Error':
            continue
        elif url is None:
            print('今日糗百已经下载完毕.......')
            break
