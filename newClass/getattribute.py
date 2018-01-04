#encoding:utf-8

class listNoAppend(list):

    def __getattribute__(self, item):

        if item == 'append':
            raise AttributeError,item

        return list.__getattribute__(self,item)

if __name__ == '__main__':

    newList = listNoAppend()
    # print dir(newList)
    newList.append(1) #AttributeError: append

# 对新式类的实例来说，所有属性和方法的访问操作都是通过__getattribute__完成，
# 这是由object基类实现的。如果有特殊的要求，可以重载__getattribute__方法，上面
# 实现一个不能使用append方法的list






