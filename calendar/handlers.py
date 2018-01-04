#encoding:utf-8

from __future__ import print_function
import datetime


ORIGINALDAY = datetime.date(2010,01,03)
TOTALWEEKDAY = 7
ListWeeks = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
ListDays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]


def getDaysOfWeek(date1):
    '''
    todo 获取当前日期是星期几
    :param date1:
    :return:
    '''

    if ORIGINALDAY > date1:
        dayOfRemainder = 7 - ((ORIGINALDAY - date1).days) % TOTALWEEKDAY
    else:
        dayOfRemainder = ((date1 - ORIGINALDAY).days) % TOTALWEEKDAY

    return dayOfRemainder

def printCanlendar(year,month,day,dayOfRemainder):

    if month in [1,3,5,7,8,10,12]:
        listDay = ListDays[:]
    elif month in [4,6,9,11]:
        listDay = ListDays[0:-1]
    elif month in [2]:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            listDay = ListDays[0:-2]
        else:
            listDay = ListDays[0:-3]
    else:
        raise ImportError

    for i in range(dayOfRemainder):
        listDay.insert(0,' ')

    for i in ListWeeks:
        print(i.center(1),'',end = '')

    print('\n',end='')


    for count, day in enumerate(listDay):

        count = count + 1

        day = str(day)
        if len(day) < 2:
            day = ' '+day

        print(' ',day.center(1),' ',end = '')

        if count % 7 == 0:
            print('\n',end = '')



if __name__ == '__main__':

    data1 = raw_input('请输入日期，比如 2009.12.20: ')
    year,month,day = data1.split('.')
    year = int(year)
    month = int(month)
    date1 = datetime.date(year,month,01)
    dayOfRemainder = getDaysOfWeek(date1)
    print ('----------------------------')
    print (month,type(month))
    printCanlendar(year,month,day,dayOfRemainder)



'''
星期日  星期一 星期二  星期三  星期四  星期五  星期六
         1     2      3      4      5      6
  7      8     9      10     11     12     13
'''

