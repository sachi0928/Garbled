# class b(object):
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#
#     def dog_name(self):
#         return self.name
#
#     def dog_color(self):
#         return self.color
#
#     def dog_eat(self,eat):
#         return eat
#
#     def dog_all(self,dog_eat):
#         return "他的名字叫"+self.dog_name()+","+self.dog_color()+","+dog_eat
#
# if __name__ == "__main__":
#     c=b("招财","黑色")
#     e = b("进宝", "白色")
#     d=e.dog_all("喜欢吃肉")
#     print(c.dog_all("喜欢吃狗粮"))
#     print(d)
#     f=b("一夜","银色").dog_all("不喜欢吃狗粮,也不喜欢吃肉")
#     print(f)
#
#
#
# class h(b):
#     def __init__(self,name,color,type):
#         b.__init__(self,name,color)
#         self.type=type
#     def dogtype(self,dog_eat):
#         return "他的名字叫"+super().dog_name()+","+super().dog_color()+","+self.type+","+dog_eat
#     def dog_type(self,dog_eat):
#         a=list(super().dog_all(dog_eat))
#         print(a)
#         b=a.insert(3,self.type)
#         print(b)
#         c=str(b)
#         return c
# if __name__ == "__main__":
#     n=h("暴富","金色","金种")
#     k=n.dogtype("喜欢吃奥利给")
#     print(k)
#
#
# class h(b):
#     def __init__(self,name,color):
#         b.__init__(self,name,color)
#         self.type=type
#     def dogtype(self,type):
#         return type
#     def dog_type(self,dogtype,dog_eat):
#         a=super().dog_all(dog_eat)
#         b=list(a)
#         b.insert(13,dogtype)
#         c="".join(b)
#         return c
# if __name__ == "__main__":
#     d=h("尝试一下","尝试")
#     e=d.dog_type("金种,","喜欢吃黑暗料理")
#     print(e)


# def hi():
#     return "hi yasoob!"
# hi()
#
# def doSomethingBeforeHi(func):
#     print('I am doing some boring work before executing hi()')
#     print(func())
# doSomethingBeforeHi(hi)
#
#
# print("===============间隔==================")
#
#
# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# print("===============间隔==================")
#
#
#
#
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration()
#
#
#
#
#
#
#
#
#
#
#
#
# def a(b):
#     def d():
#         print("===执行前===")
#         b()
#         print("===执行后===")
#     return d
#
#
#
# def c():
#     print("===我被执行啦===")
# c=a(c)
# c()
#
#
# print("=============间隔==============")
#
#
# @a
# def d():
#     print("======我被装饰啦======")
# d()
#
#
#
#
# class a():
#     def __init__(self,c,d):
#         self.d=d
#         self.c=c
#     def e(self):
#         """面积"""
#         return self.c * self.d
#     def f(self):
#         """周长"""
#         return (self.c+self.d)*2
#     @classmethod
#     def g(cls):
#         pass
# h=a(6,4)
# print(a.g())
# i=h.e()
# print(i)
# j=h.f()
# print(j)
#
#
#
#
#
#
# class A(object):
#     bar = 1
#
#     def foo(self):
#         print('foo')
#
#     @staticmethod
#     def static_foo():
#         print('static_foo')
#         print(A.bar)
#
#     @classmethod
#     def class_foo(cls):
#         print('class_foo')
#         print(cls.bar)
#         cls().foo()
#
#
# A.static_foo()
# A.class_foo()
#
#
# class Kls(object):
#     no_inst = 0
#
#     def __init__(self):
#         self.no_inst = self.no_inst + 1
#
#
#     @classmethod
#     def get_no_of_instance(cls_obj):
#         return cls_obj.no_inst
#
#
# ik1 = Kls()
# ik2 = Kls()
# print(ik1.get_no_of_instance())
# print(Kls.get_no_of_instance())
#
#
#
#
#
# class ClassTest(object):
#     num = 0
#
#     @classmethod
#     def addNum(cls):
#         cls.num += 1
#
#     @classmethod
#     def getNum(cls):
#         return cls.num
#
#     # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
#     def __new__(self):
#         ClassTest.addNum()
#         return super(ClassTest, self).__new__(self)
#
#
# class Student(ClassTest):
#     def __init__(self):
#         self.name = ''
#
# a = Student()
# b = Student()
# c = Student()
# print(ClassTest.getNum())
#
#
#
#
#
#
#
#
# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date = cls(day, month, year)
#         return date
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
# date2 = Date.from_string('11-09-2012')
# print(date2)
# is_date = Date.is_date_valid('11-09-4000')
# print(is_date)
#
#
#
#
#
#
#
#
# class Fuck:
#     sex = '每日一撸'    #这就是非绑定的属性
#     @staticmethod
#     def sta():
#         return Fuck.sex
#     @classmethod
#     def cla(cls):
#         return cls.sex    #@classmethod里面必须要传入一个参数，这个参数代表就是当前的类
# class Fuck_everybody(Fuck):   #因为Fuck_everybody继承了父类Fuck，所以Fuck_everybody可以调用父类的sta()方法与cla()方法
#     pass
#
#
# print(Fuck_everybody.sta())
#
# print(Fuck_everybody.cla())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Recatangle:   # 新建一个长方形的类    属性=变量，方法（实例方法）=函数，实例化=必须要变量承接类函数的返回值，类方法=可以不需要变量承接的类函数
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     # 只能由实例调用，称为实例方法
#     def permeter(self):
#         return (self.length + self.width)*2
#
#     # 只能由实例调用，称为实例方法
#     def area(self):
#         return self.length * self.width
#
#     # 装饰器，表示下面的方法是类方法
#     @classmethod
#     def features(cls):
#         print('两边的长相等，两边的宽也相等，长和宽的角度为90°')
#
#     # 装饰器，表示下面的方法是静态方法
#     # 静态方法本质上是函数，只是写在了类里面
#     @staticmethod
#     def sumdata(a, b):
#         return a + b
#
#
#
#
# rec = Recatangle(6, 4)   # 实例化一个长方形
# rec.permeter()           # 调用周长计算公式方法
# rec.area()               # 调用面积计算公式方法
# rec.features()           # 调用类方法，由实例调用
# Recatangle.features()    # 调用类方法，由类调用
# rec.sumdata(10, 10)           # 调用静态方法，由实例调用
# Recatangle.sumdata(10, 10)    # 调用静态方法，由类调用
#

import numpy as np
import pandas as pd
from time import sleep

# df=pd.DataFrame({"Id":[1001,1002,1003,1004,1005,1006,1007,1008],
#                  "date":pd.date_range("2021-11-16",periods=8),
#                  "city":["beijing","shanghai","chengdu","guangzhou","shenzhen","hangzhou","nanjing","xianggang"],
#                  "age":[21,22,23,24,25,26,27,28],
#                  "License_plate":["jing-A","hu-A","chuan-A","yue-A","yue-B","zhe-A","su-A",np.nan],
#                  "price":[1200,np.nan,4765,4365,7567,np.nan,np.nan,6454]}
#                 )
# df.to_csv(r"C:\Users\Administrator\Desktop\test1.csv",columns=["Id","date","city","age","License_plate","price"],
#           index=False,  #索引
#           sep=",",      #换行,根据逗号换行
#           na_rep="NaN",
#           encoding="utf-8",
#           header=True)  #列名
#na_rep   指定空值的输出方式，默认是空字符串,与np.nan搭配使用,np.nan想当与占位符
#index_label   索引列的列名
#columns    指定要输出的列,有些地方写的参数名是cols

#
# sleep(5)
# a=pd.read_csv(r"C:\Users\Administrator\Desktop\test1.csv",encoding="utf-8")
# print(a)


# import json,time,schedule,requests
#
# import self
#
#
# def job():
#     print("我被定时运行啦")
# job()
# schedule.every(10).seconds.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(5)



"""抢票"""
from splinter.browser import Browser
from time import sleep
import traceback


class Buy_Tickets(object):
    # 定义实例属性，初始化
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.xb = xb
        # self.pz = pz
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.driver_name = 'chrome'
        self.executable_path = r"C:\Users\Git\webdriver\chromedriver.exe"

    # 登录功能实现
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('loginUserDTO.user_name', self.username)
        # sleep(1)
        self.driver.fill('userDTO.password', self.passwd)
        # sleep(1)
        print('请输入验证码...')
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break

    # 买票功能实现
    def start_buy(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        # 窗口大小的操作
        self.driver.driver.set_window_size(700, 500)
        self.login()
        self.driver.visit(self.ticket_url)
        try:
            print('开始购票...')
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        self.driver.find_by_text('预订')[self.order - 1].click()
                        sleep(1.5)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        for i in self.driver.find_by_text('预订'):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            print('开始预订...')
            sleep(1)
            print('开始选择用户...')
            for p in self.passengers:

                self.driver.find_by_text(p).last.click()
                sleep(0.5)
                if p[-1] == ')':
                    self.driver.find_by_id('dialog_xsertcj_ok').click()
            print('提交订单...')
            # sleep(1)
            # self.driver.find_by_text(self.pz).click()
            # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            sleep(2)
            print('确认选座...')
            self.driver.find_by_id('qr_submit_id').click()
            print('预订成功...')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 用户名
    username = 'xxxx'
    # 密码
    password = 'xxx'
    # 车次选择，0代表所有车次
    order = 2
    # 乘客名，比如passengers = ['丁小红', '丁小明']
    # 学生票需注明，注明方式为：passengers = ['丁小红(学生)', '丁小明']
    passengers = ['丁彦军']
    # 日期，格式为：'2018-01-20'
    dtime = '2018-01-19'
    # 出发地(需填写cookie值)
    starts = '%u5434%u5821%2CWUY'  # 吴堡
    # 目的地(需填写cookie值)
    ends = '%u897F%u5B89%2CXAY'  # 西安

    # xb =['硬座座']
    # pz=['成人票']

    Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()