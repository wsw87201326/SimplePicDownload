import requests


def crawlHtml(url):
    headers = {
        'Host': 'blog.csdn.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.baidu.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    try:
        r = requests.get(url,headers=headers)
        print(r.status_code)
        if r.status_code == 200:
            return r.text
        else:
            return 'Service_Error'

    except Exception as e:
        print("error!", e)

