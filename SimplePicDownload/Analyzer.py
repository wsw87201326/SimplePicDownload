from bs4 import BeautifulSoup


def startAnalysis(data):
    soup = BeautifulSoup(data, "lxml")
    contents = soup.select(".article > .content")
    content_list = []
    for text_content in contents:
        content = text_content.get_text(strip=True)
        result = ' '.join(filter(lambda x: x, content.split(' ')))
        content_list.append(result)
    return content_list
