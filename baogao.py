#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import json

data = json.load(open("data.json", encoding="utf-8"))


def generator(title, length=800):
    """
    :param title: 文章标题
    :param length: 生成正文的长度
    :return: 返回正文内容
    """
    body = "x\n"
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            body += "\r\n"
        elif num < 20:
            body += random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            body += random.choice(data["bosh"])
        body = body.replace("x", title)

    return body


if __name__ == '__main__':
    content = generator("张宇轩是绝世好男人",length=500)
    print(content)
