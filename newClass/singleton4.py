#encoding:utf-8

#这个方法是将一个类下所有的实例属性指向同一个dict，内存空间不是同一块，这是真正的单例模式吗？

class Singleton(object):

    _dict = {}

    def __new__(cls, *args, **kwargs):



        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)

        ob.__dict__ = cls._dict

        return ob


class myClass(Singleton):

    a = 1

class Person(object):

    name = 'jack'



if __name__ == '__main__':

    mc = myClass()
    mc2 = myClass()
    mc.a = 2
    print mc2.a

    p1 = Person()
    p2 = Person()
    p1.name = 'peter'
    print p2.name #jack