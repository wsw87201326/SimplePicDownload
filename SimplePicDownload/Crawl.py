import requests


def crawlHtml(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            return r.text
        else:
            return 'Service_Error'

    except Exception as e:
        print("error!", e)

