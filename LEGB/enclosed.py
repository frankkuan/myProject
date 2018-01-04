#encoding:utf-8

import foo

def wrapper():
    filename = 'enclosed.py'
    def show_filename():
        return 'filename {0}'.format(filename)
    print foo.call_func(show_filename)

if __name__ == '__main__':

    print globals()
    # wrapper()



# {
#  '__builtins__': <module '__builtin__' (built-in)>,      内建作用域环境
#  '__file__': '/Users/wangjinkuan/PycharmProjects/myProject/LEGB/enclosed.py',
#  'wrapper': <function wrapper at 0x1005eb0c8>,           直接外围环境
#  '__package__': None, '__name__': '__main__',
#  'foo': <module 'foo' from '/Users/wangjinkuan/PycharmProjects/myProject/LEGB/foo.pyc'>,  全局环境
#  '__doc__': None
# }

# 当代码执行到 show_filename() 函数中的 return 'filename {0}'.format(filename)语句时，解析器会按照以下规则逐层查找
# 1、local环境，也就是 show_filename函数内部，并且没有被global关键字声明的
# 2、Enclosing,直接外围空间，上层函数wrapper的本地作用域
# 3、global，全局空间（模块 enclosed.py）
# 4、builtin，内置模块中预定义的变量名中查找filename


# 1、闭包最重要的使用价值在于：封存函数执行的上下文环境
# 2、闭包在其捕捉的执行环境（def语句块所在的上下文）中，也遵循LEGB逐层查找，直至符合要求的变量，或者抛出异常