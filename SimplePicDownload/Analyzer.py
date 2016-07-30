# coding:utf-8
from bs4 import BeautifulSoup


def startAnalysis(data):
    try:
        soup = BeautifulSoup(data, "lxml")
        contents = soup.select(".article > .content")
        content_list = []
        next_url = ''
        for text_content in contents:
            content = text_content.get_text(strip=True)
            result = ' '.join(filter(lambda x: x, content.split(' ')))
            content_list.append(result)

        tag_list = soup.select('.pagination > li > a')

        for tag in tag_list:
            if tag.get_text(strip=True) == '下一页':
                next_url = tag.get('href')
        return content_list, next_url
    except TypeError:
        print("出现错误！！！~~~~~~")
        print(data)
        print('放弃写入')