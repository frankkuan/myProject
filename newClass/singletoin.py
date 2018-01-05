#encoding:utf-8



class Singleton(object):

    _singleton = {}  #定义该类的一个属性，这个类的所有创建的对象都会拥有

    def __new__(cls, *args, **kwargs):  #cls代表一个 "类对象"

        if not cls._singleton.has_key(cls):  #有没有这个对象

            cls._singleton[cls] = object.__new__(cls)

        return cls._singleton[cls]

if __name__ == '__main__':

    a = Singleton()

    print id(a) #4458414160

    b = Singleton()

    print id(b) #4458414160


# 新式类本身具有的特性： __new__(cls), __init__(c,2)