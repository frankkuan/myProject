#encoding:utf-8

import logging

def add(a,b):

    return a + b

logging.basicConfig(level=logging.INFO)

def checkParams(func):

    def wrapper(a,b):

        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return func(a, b)

        logging.warning('a和b不能被相加！')

        return

    return wrapper #func引用add，并且被封存在闭包的执行环境中返回，不会随着checkParams函数的返回被垃圾回收器回收，这里面也将创建一个闭包

if __name__ == '__main__':

    add = checkParams(add) #等号左侧的add指向checkParams的返回值 wrapper（实际上是一个闭包）
    add('a',1)  #WARNING:root:a和b不能被相加！