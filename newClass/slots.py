#encoding:utf-8

class myClass(object):

    def __init__(self):
        self.name = 'jack'
        self.age = 32

    __slots__ = ('name','age','__dict__')  #__slots__是一个类变量，__slots__属性可以赋值一个包含类属性名的字符串元组，或者是可迭代变量，或者
                              # 是一个字符串，只要在类定义的时候，使用__slots=aTuple来定义该属性就可以了


if __name__ == '__main__':

    mc = myClass()

    print dir(mc) # 实例mc中没有 __dict__属性

    mc.address = 'huma' #AttributeError: 'myClass' object has no attribute 'address',将 address 或者将 "__dict__" 添加进 __slots__元组里就可以增加 address 属性

'''
通常每一个实例x都会有一个__dict__属性，用来记录实例中所有的属性和方法，也是通过这个字典，
可以让实例绑定任意的属性。而__slots__属性作用就是，当类C有比较少的变量，而且拥有__slots__属性时，
类C的实例 就没有__dict__属性，而是把变量的值存在一个固定的地方。如果试图访问一个__slots__中没有
的属性，实例就会报错。这样操作有什么好处呢？__slots__属性虽然令实例失去了绑定任意属性的便利，
但是因为每一个实例没有__dict__属性，却能有效节省每一个实例的内存消耗，有利于生成小而精
干的实例。



为什么需要这样的设计呢？
在一个实际的企业级应用中，当一个类生成上百万个实例时，即使一个实例节省几十个字节都可以节省
一大笔内存，这种情况就值得使用__slots__属性。



使用时__slots__时需要注意的几点：
1.  当一个类的父类没有定义__slots__属性，父类中的__dict__属性总是可以访问到的，所以只在子
类中定义__slots__属性，而不在父类中定义是没有意义的。

2. 如果定义了__slots属性，还是想在之后添加新的变量，就需要把'__dict__'字符串添加到__slots__的
元组里。

3. 定义了__slots__属性，还会消失的一个属性是__weakref__，这样就不支持实例的weak reference，
如果还是想用这个功能，同样，可以把'__weakref__'字符串添加到元组里。

4. __slots__功能是通过descriptor实现的，会为每一个变量创建一个descriptor。

5. __slots__的功能只影响定义它的类，因此，子类需要重新定义__slots__才能有它的功能。
'''