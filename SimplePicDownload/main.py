from SimplePicDownload.MainScheduler import MainScheduler

if __name__ == '__main__':
    page = 1
    url = 'http://www.qiushibaike.com/text/' + str(page)

    save_url = 'E:\\qsbk\\'
    while True:
        url = MainScheduler.startDownload(url, save_url)
        print(url)
        page += 1
        print(str(page)+"下载完毕")
        if url is None:
            break
