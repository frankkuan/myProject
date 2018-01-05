#encoding:utf-8

#这种单例模式是利用装饰器来创建

def singleton(cls, *args, **kwargs): #传入一个类，无论是传入类还是方法都是对象

    instances = {}

    def getInstance():

        if cls not in instances:

            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return getInstance


@singleton
class myClass(object):

    pass

if __name__ == '__main__':

    mc = myClass()
    mc2 = myClass()
    print id(mc),id(mc2)