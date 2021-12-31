import unittest,requests,json,urllib3




# class login(unittest.TestCase):
#     def setUp(self) -> None:
#         self.url=""
#         self.headers=""
#         self.data={}
#     def tearDown(self) -> None:
#         pass
#     def test_01_login(self):
#         r=requests.post(self.url,self.headers,self.data)
#         self.assertIn("操作成功",r.text)
#
# if __name__ == '__main__':
#     unittest.main()
#


# 







# a=[1,2,3,4,5,6,7,8,9,10]
# b=[ i for i in a if i>=5]
# print(b)










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





"""html常用标签"""
# <html>..</html> 表示标记中间的元素是网页
# <body>..</body> 表示用户可见的内容
# <div>..</div> 表示框架
# <p>..</p> 表示段落
# <li>..</li>表示列表
# <img>..</img>表示图片
# <h1>..</h1>表示标题
# <a href="">..</a>表示超链接


# -*- coding: utf-8 -*-




# """烟花代码"""
# import math, random, time
# import threading
# import tkinter as tk
# import re
#
# # import uuid
#
# Fireworks = []
# maxFireworks = 8
# height, width = 600, 600
#
#
# class firework(object):
#     def __init__(self, color, speed, width, height):
#         # uid=uuid.uuid1()
#         self.radius = random.randint(2, 4)  # 粒子半径为2~4像素
#         self.color = color  # 粒子颜色
#         self.speed = speed  # speed是1.5-3.5秒
#         self.status = 0  # 在烟花未爆炸的情况下，status=0；爆炸后，status>=1；当status>100时，烟花的生命期终止
#         self.nParticle = random.randint(20, 30)  # 粒子数量
#         self.center = [random.randint(0, width - 1), random.randint(0, height - 1)]  # 烟花随机中心坐标
#         self.oneParticle = []  # 原始粒子坐标（100%状态时）
#         self.rotTheta = random.uniform(0, 2 * math.pi)  # 椭圆平面旋转角
#
#         # 椭圆参数方程：x=a*cos(theta),y=b*sin(theta)
#         # ellipsePara=[a,b]
#
#         self.ellipsePara = [random.randint(30, 40), random.randint(20, 30)]
#         theta = 2 * math.pi / self.nParticle
#         for i in range(self.nParticle):
#             t = random.uniform(-1.0 / 16, 1.0 / 16)  # 产生一个 [-1/16,1/16) 的随机数
#             x, y = self.ellipsePara[0] * math.cos(theta * i + t), self.ellipsePara[1] * math.sin(
#                 theta * i + t)  # 椭圆参数方程
#             xx, yy = x * math.cos(self.rotTheta) - y * math.sin(self.rotTheta), y * math.cos(
#                 self.rotTheta) + x * math.sin(self.rotTheta)  # 平面旋转方程
#             self.oneParticle.append([xx, yy])
#
#         self.curParticle = self.oneParticle[0:]  # 当前粒子坐标
#         self.thread = threading.Thread(target=self.extend)  # 建立线程对象
#
#     def extend(self):  # 粒子群状态变化函数线程
#         for i in range(100):
#             self.status += 1  # 更新状态标识
#             self.curParticle = [[one[0] * self.status / 100, one[1] * self.status / 100] for one in
#                                 self.oneParticle]  # 更新粒子群坐标
#             time.sleep(self.speed / 50)
#
#     def explode(self):
#         self.thread.setDaemon(True)  # 把现程设为守护线程
#         self.thread.start()  # 启动线程
#
#     def __repr__(self):
#         return ('color:{color}\n'
#                 'speed:{speed}\n'
#                 'number of particle: {np}\n'
#                 'center:[{cx} , {cy}]\n'
#                 'ellipse:a={ea} , b={eb}\n'
#                 'particle:\n{p}\n'
#                 ).format(color=self.color, speed=self.speed, np=self.nParticle, cx=self.center[0], cy=self.center[1],
#                          p=str(self.oneParticle), ea=self.ellipsePara[0], eb=self.ellipsePara[1])
#
#
# def colorChange(fire):
#     rgb = re.findall(r'(.{2})', fire.color[1:])
#     cs = fire.status
#
#     f = lambda x, c: hex(int(int(x, 16) * (100 - c) / 30))[2:]  # 当粒子寿命到70%时，颜色开始线性衰减
#     if cs > 70:
#         ccr, ccg, ccb = f(rgb[0], cs), f(rgb[1], cs), f(rgb[2], cs)
#     else:
#         ccr, ccg, ccb = rgb[0], rgb[1], rgb[2]
#
#     return '#{0:0>2}{1:0>2}{2:0>2}'.format(ccr, ccg, ccb)
#
#
# def appendFirework(n=1):  # 递归生成烟花对象
#     if n > maxFireworks or len(Fireworks) > maxFireworks:
#         pass
#     elif n == 1:
#         cl = '#{0:0>6}'.format(hex(int(random.randint(0, 16777215)))[2:])  # 产生一个0~16777215（0xFFFFFF）的随机数，作为随机颜色
#         a = firework(cl, random.uniform(1.5, 3.5), width, height)
#         Fireworks.append({'particle': a, 'points': []})  # 建立粒子显示列表，‘particle’为一个烟花对象，‘points’为每一个粒子显示时的对象变量集
#         a.explode()
#     else:
#         appendFirework()
#         appendFirework(n - 1)
#
#
# def show(c):
#     for p in Fireworks:  # 每次刷新显示，先把已有的所以粒子全部删除
#         for pp in p['points']:
#             c.delete(pp)
#
#     for p in Fireworks:  # 根据每个烟花对象，计算其中每个粒子的显示对象
#         oneP = p['particle']
#         if oneP.status == 100:  # 状态标识为100，说明烟花寿命结束
#             Fireworks.remove(p)  # 移出当前烟花
#             appendFirework()  # 新增一个烟花
#             continue
#         else:
#             li = [[int(cp[0] * 2) + oneP.center[0], int(cp[1] * 2) + oneP.center[1]] for cp in
#                   oneP.curParticle]  # 把中心为原点的椭圆平移到随机圆心坐标上
#             color = colorChange(oneP)  # 根据烟花当前状态计算当前颜色
#             for pp in li:
#                 p['points'].append(
#                     c.create_oval(pp[0] - oneP.radius, pp[1] - oneP.radius, pp[0] + oneP.radius, pp[1] + oneP.radius,
#                                   fill=color))  # 绘制烟花每个粒子
#
#     root.after(50, show, c)  # 回调，每50ms刷新一次
#
#
# if __name__ == '__main__':
#     appendFirework(maxFireworks)
#
#     root = tk.Tk()
#     cv = tk.Canvas(root, height=height, width=width)
#     cv.create_rectangle(0, 0, width, height, fill="black")
#
#     cv.pack()
#
#     root.after(50, show, cv)
#     root.mainloop()



#
# list=[1,2,3,4,5,6,7,8,9,10]
#
# # count=0
# # for item in list:
# #     #print ("item")
# #     count +=1
# #     if count % 10 == 0:
# #      print("{}".format(count))
# #
#
#
#
# for count in range(0,len(list)):
#
#         print ('第{}张下载成功'.format(list[count]))

#proxies={"https":"103.73.160.89"}
url="https://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
a=requests.get(url=url,headers=headers,proxies={}).text
with open("ip.html","w",encoding="utf-8") as f:
    f.write(a)