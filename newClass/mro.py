#encoding:utf-8

class D(object):

    def __init__(self):
        self.a = 1

class B(D):

    pass

class C(D):

    def __init__(self):

        self.a = 2

class A(B,C):

    pass

if __name__ == '__main__':

    a = A()
    print a.a

    print A.__mro__ #(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <type 'object'>)


#经典类是按照深度优先的方式进行查找，新式类是按照广度优先的方式进行查找，所以a.a = 2,这个顺序的实现是通过新式类中特殊的只读属性__mro__，
# 类型是一个元组，保存着解析顺序信息。只能通过类来使用，不能通过实例调用。