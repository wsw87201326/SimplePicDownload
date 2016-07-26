import requests


def crawlHtml(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return None

    except Exception as e:
        print("error!", e)

