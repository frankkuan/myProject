#encoding:utf-8


#这种单例模式是使用 __new__(cls, *args, **kwargs)

class Singleton(object):

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls,'_instance'):
        # if not cls._instance:  # 会报错，没有这个属性，hasattr()方法不会报错
            origin = super(Singleton,cls) #super(type, type2) -> bound super object; requires issubclass(type2, type)

            cls._instance = origin.__new__(cls) #或者直接用object.__new__(cls,*args,**kwargs)

        return cls._instance

class myClass(Singleton):

    name = 'jack'


if __name__ == '__main__':

    mc = myClass()
    mc2 = myClass()
    print id(mc),id(mc2)
