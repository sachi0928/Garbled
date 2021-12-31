#todo 猜数字
import threading

import requests,time


# def digui(i):
#     #global num
#     if i>0:
#         return i + digui(i-1)
#     else:
#         return 0
#
#
# print(digui(100))
#
#
#
#
# def digui(n):
#     if n>0:
#         return digui(n-1) * 2
#     else:
#         return 1
#
# print(digui(4))
#
#
#
#
#
# def tri_recursion(k):
#   if(k>0):
#     return k+tri_recursion(k-1)
#     #print(result)
#   else:
#     return 0
#   #return result
#
# print(tri_recursion(6))







def requests_1(num):
    for i in range(1,num):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
        a=requests.get(url="http://www.baidu.com",headers=headers)
        #print(a.text)
        print("正在打印{}".format(int(i)))

def requests_2(nums):
    for a in range(1,nums):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
        c=requests.get(url="http://www.baidu.com",headers=headers)
        #print(c.text)
        print("正在打印{}".format(int(a)))



def main():
    t1=threading.Thread(target=requests_1,args=[10])    #todo  target=需要运行的函数，args=函数的实参,可在此处传入格式:[x]
    t2=threading.Thread(target=requests_2,args=[10])
    t1.start()  #开始执行线程
    t2.start()  #开始执行线程
    t1.join()   #让主线程挂起，等待所有子线程结束再执行
    t2.join()   #让主线程挂起，等待所有子线程结束再执行

if __name__ == '__main__':
    main()


















