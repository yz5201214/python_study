# calendar 日历相关
'''
calendar:获取一年的日历字符串
参数：
w = 每个日期之间的间隔字符数
l = 每周所占用的函数
c = 每个月之间的间隔字符数
'''
import calendar
# 2018年的日历
# cal 是字符串
def test01():
    cal = calendar.calendar(2018)
    print(cal)
# 间隔小了点
def test02():
    cal = calendar.calendar(2018,l=0,c=0)
    print(cal)
# isleap：判断某一年是否是闰年
def test03():
    print(calendar.isleap(2019))
    print(calendar.isleap(2012))

# leapdays：获取指定年份之间的闰年个数
# 第一个参数，要比第二个参数小，否则异常
def test04():
    try:
        print(calendar.leapdays(2021,2012))
    except Exception as e:
        print(e)
    #help(calendar.leapdays(2001,2012))
# month() 获取某个月的日历字符串
def test05():
    try:
        print(calendar.month(2019,4))
    except Exception as e:
        print(e)
# monthrange() 获取某一个月的周记开始及天数
# 返回一个元祖类型，可以分别接受
def test05():
    try:
        w,t  = calendar.monthrange(2019,5)
        print(w,t)
    except Exception as e:
        print(e)
# monthcalendar()返回一个月每天的矩阵列表
# 返回值：二级列表
# 注意，矩阵中没有天数用0表示
# list里面包含了list
def test06():
    try:
        w = calendar.monthcalendar(2019,4)
        print(w)
    except Exception as e:
        print(e)

# prcal:print calendar 直接打印日历
# 参数：年份
def test07():
    try:
        calendar.prcal(2019)
    except Exception as e:
        print(e)
# prmonth() 直接打印整个月份
# 参数：年份，月份
def test08():
    try:
        calendar.prmonth(2019,4)
    except Exception as e:
        print(e)
# weekday()获取对应年份，月份，日期是周几，下标0开始
# 参数：年份，月份，日期
# 注意，这里的下标是0开始，0表示星期一，1表示星期二
def test09():
    try:
        print(calendar.weekday(2019,4,25))
    except Exception as e:
        print(e)
if __name__ == '__main__':
    test09()