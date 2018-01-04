#encoding:utf-8

import foo

filename = 'func.py'

def show_filename():
    return 'filename: {0}'.format(filename)

if __name__ == '__main__':

    print foo.call_func(show_filename)