#encoding:utf-8

#协作式调用父类方法

class A(object):

    def foo(self):

        print "A's foo "

class B(A):

    def foo(self):
        print "B's foo "
        # A.foo(self)
        super(B,self).foo()

class C(A):

    def foo(self):
        print "C's foo "
        # A.foo(self)
        super(C,self).foo()

class D(B,C):

    def foo(self):

        print "D's foo "
        # B.foo(self)
        # C.foo(self)
        super(D,self).foo()

if __name__ == '__main__':

    d = D()
    d.foo()   # D's foo
              # B's foo
              # A's foo
              # C's foo
              # A's foo

# 当子类重写了父类的一个方法时，通常会调用父类的同名方法做一些工作，这是比较常见的使用方式,但是基类A的方法执行了两次，我们只需要一次就足够，
# 如何避免？用super()函数





