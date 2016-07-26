from datetime import datetime
import os


def downContent(content_list, save_url):
    today_time = datetime.now().strftime('%F')

    if not os.path.exists(save_url):
        os.makedirs(save_url)

    real_save_url = save_url + today_time + '.txt'
    print('正在向||||' + real_save_url + '|||||中写入')
    success_num = 0
    with open(real_save_url, 'a') as txt_file:
        for content in content_list:
            content += '\n'
            try:
                txt_file.write('●  ' + content)
                success_num += 1
            except UnicodeEncodeError:
                print('出现错误。放弃写入')
                # 这是取序号的方法
                # for index, content in enumerate(content_list):
                #     number = index + 1
                #     print(str(number) + "." + content)
    print('文件写入完成 %d/%d' % (success_num, len(content_list)))


if __name__ == '__main__':
    now = datetime.now().strftime('%F')
    L = ["a", "c", "w"]
    f = open('f:\\qsbk\\2016-07-26.txt', 'w')
    f.write("asdasd")
