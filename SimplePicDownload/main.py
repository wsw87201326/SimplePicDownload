from SimplePicDownload.MainScheduler import MainScheduler

if __name__ == '__main__':
    page = 1
    url = 'http://www.qiushibaike.com/text/' + str(page)

    save_url = 'E:\\qsbk\\'
    MainScheduler.startDownload(url, save_url)
