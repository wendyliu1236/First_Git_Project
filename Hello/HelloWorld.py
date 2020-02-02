# coding: utf-8

# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

class Hello:

    def __init__(self):
        print("this is init")

    def hello(self):
        print("hello world! This is my first git project launch!")


if __name__ == '__main__':
        h = Hello()
        h.hello()