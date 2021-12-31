import time

import requests, json, re, os, bs4, lxml,threading
from bs4 import BeautifulSoup

# User-agent: *    支持所有的爬虫
# Disallow: /a/    禁止爬a目录
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

# url="https://www.baidu.com/s?"
# variable=input("Enter:")
# data={"wd":variable}
#
# baidu=requests.get(url=url,params=data,headers=headers)
# b=variable+".html"
# with open(b,"w",encoding="utf-8") as f :
#     f.write(baidu.text)


# url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
# city=input("Enter:")
# c=city+".json"
# d=[]
# for i in range(1,4):
#         post_data={
#         "cname": "",
#         "pid": "",
#         "keyword": city,
#         "pageIndex": str(i),
#         "pageSize": "10"
#                 }
#         kfc=requests.post(url=url,data=post_data,headers=headers)
#         list_kfc=kfc.json()
#         #print(type(list_kfc))
#         for a in list_kfc["Table1"]:
#                 d.append(a)
#         fp=open(c,"a",encoding="utf-8"+"\n")
#         json.dump(d,fp=fp,ensure_ascii=False)
#
# print("over!!!!!!!!")


# url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
# city=input("Enter:")
# c=city+".json"
# d=[]
# for i in range(1,4):
#         post_data={
#         "cname": "",
#         "pid": "",
#         "keyword": city,
#         "pageIndex": str(i),
#         "pageSize": "10"
#                 }
#         kfc=requests.post(url=url,data=post_data,headers=headers)
#         dict_kfc=json.loads(kfc.text)
#         print(type(dict_kfc))
#         for a in dict_kfc["Table1"]:
#                 d.append(a)
#
#
# e=json.dumps(d,ensure_ascii=False)
# with open(c,"a",encoding="utf-8") as f:
#         f.write(e+"\n")

# print("over!!!!!!!!")


# <div class="thumb">
#
# <a href="/article/124937647" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12493/124937647/medium/YNQ8QMGO7WLNJ3S6.jpg" alt="糗事#124937647" class="illustration" width="100%" height="auto">
# </a>
# </div>


# if not os.path.exists("./qiushi"):    #如果不存在文件夹xxx，那就创建xxx
#         os.mkdir("./qiushi")
#
#
# url="https://www.qiushibaike.com/imgrank/"
#
# img_qiushi=requests.get(url=url,headers=headers).text
#
#
# img_url='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'   #通过正则 提取图片的url
# img_list = re.findall(img_url,img_qiushi,re.S)      #把提取到的url作用到text中   re.S 单行匹配
# for i in img_list:
#         a ="https:"+i      #给提取到的URL拼一个完整的URL
#         img_url_list = requests.get(url=a,headers=headers).content    #返回所有图片
#         print(img_url_list)
#         img_name = a.split("/")[-1]        #图片名称
#         img_path = "./qiushi/" + img_name  #储存路径
#         with open(img_path,"wb") as f:
#                 f.write(img_url_list)
#                 print(img_name,"下载成功！！！")


# if not os.path.exists("./doutu"):
#         os.mkdir("./doutu")
# url="https://www.qiushibaike.com/imgrank/"
# qiushi=requests.get(url=url,headers=headers).text
# img_url = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
# img_url_list=re.findall(img_url,qiushi,re.S)
# for i in img_url_list:
#         a="https:"+i
#         qiushi_img = requests.post(url=a, headers=headers).content
#         img_name=a.split("/")[-1]
#         img_path="./doutu/"+img_name
#         with open(img_path,"wb")as f:
#                 f.write(qiushi_img)
#                 print(img_name,"下载成功！！！")


# if not os.path.exists("./add_happyimg"):
#         os.mkdir("./add_happyimg")
# re_add_img_url='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
#
# for i in range(1,14):
#         url=r"https://www.qiushibaike.com/imgrank/page/"+str(i)
#         add_img=requests.get(url=url,headers=headers).text    #提取text
#         add_img_url_list=re.findall(re_add_img_url,add_img,re.S)  #提取text中的URL，返回一个list
#         for a in add_img_url_list:
#                 b="https:"+a
#                 add_img_url = requests.get(url=b, headers=headers).content   #通过提取出来的URL，取出二进制格式的图片
#                 add_img_name=b.split("/")[-1]
#                 add_img_path="./add_happyimg/"+add_img_name
#                 with open(add_img_path,"wb") as f:
#                         f.write(add_img_url)
#
#                 print(add_img_name,"下载成功！！！")




# /,一个层级   //，多个层级，从任意位置开始定位
# 属性定位:
# //div[@class='song']         todo：@属性名，固定格式
# 索引定位:
# //div l@class="song"1/p[3]    todo:从div标签开始，定位class属性中第三个p标签（索引是从1开始的）
#取文本:
#/text()获取的是标签中直系的文本内容
#//text()标签中非直系的文本内容(所有的文本内容)
# 取属性:
#/@attrName(属性名)

#todo:需要转码的文本.encode('iso=8859-1').decode('gbk')  解决乱码通用方案

# url = r"https://sz.58.com/ershoufang/p1"
# five_city = requests.get(url=url, headers=headers).text
# a = etree.HTML(five_city)
# b = a.xpath('//div[@class="property-content-title"]/h3/@title')
# c=b
# for i in c:
#     print(i)





if not os.path.exists("./addBeauty"):
    os.mkdir("./addBeauty")

# for i in range(1,163):
#     if i==1:
#         add_url=r"https://pic.netbian.com/4kdongman/"
#     else:
#         add_url=r"https://pic.netbian.com/4kdongman/"+"/index_"+str(i)+".html"
#     print(add_url)
#     add_Beauty_img = requests.get(url=add_url, headers=headers).text
#     add_Beauty_img_text = etree.HTML(add_Beauty_img)
#     add_li_list = add_Beauty_img_text.xpath('//div[@class="slist"]//li')
#     #time.sleep(5)
#     for c in add_li_list:
#         li_src = c.xpath('./a/img/@src')[0]
#         a="https://pic.netbian.com"+li_src
#         img_url=requests.get(url=a,headers=headers).content
#         img_name = c.xpath('./a/img/@alt')[0]+".jpg"
#         new_img_name=img_name.encode('iso=8859-1').decode('gbk')
#         img_path="./addBeauty/"+new_img_name
#         with open(img_path,"wb")as f:
#             f.write(img_url)
#         print(new_img_name,"下载成功！！！")
# start=time.time()
# n=[]
#
# def photo(num):
#     for e in range(1,num):
#         if e==1:
#             add_url=r"https://pic.netbian.com/4kdongman/"   #todo:其它版块  1.shoujibizhi(68页)   2.4kmeinv(137页)   3.4kfengjing(205页)  4.4kdongman(161页)
#         else:
#             add_url=r"https://pic.netbian.com/4kdongman/"+"/index_"+str(e)+".html"
#         print(add_url)
#         add_Beauty_img = requests.get(url=add_url, headers=headers).text
#         add_Beauty_img_text = etree.HTML(add_Beauty_img)
#         add_li_list = add_Beauty_img_text.xpath('//div[@class="slist"]//li')
#         for f in add_li_list:
#             li_src=f.xpath('./a/img/@src')[0]
#             a="https://pic.netbian.com"+li_src
#             img_url=requests.get(url=a,headers=headers).content
#             img_name = f.xpath('./a/img/@alt')[0]+".jpg"
#             new_img_name = img_name.encode('iso=8859-1').decode('gbk')
#             img_path="./addBeauty/"+new_img_name
#             with open(img_path,"wb")as af:
#                 af.write(img_url)
#             n.append(f)
#             print(new_img_name, "图片下载成功！！！")
#         if e==num-1:
#             for m in enumerate(n):
#
#                 print("第{}图片下载成功！！！".format(m[0]+1))
# def main():
#     thread_1= threading.Thread(target=photo,args=[20])
#     thread_1.start()
#     thread_1.join()
#     thread_2 = threading.Thread(target=photo, args=[20])
#     thread_2.start()
#     thread_2.join()
#     thread_3 = threading.Thread(target=photo, args=[20])
#     thread_3.start()
#     thread_3.join()
#     thread_4 = threading.Thread(target=photo, args=[20])
#     thread_4.start()
#     thread_4.join()
#     thread_5 = threading.Thread(target=photo, args=[20])
#     thread_5.start()
#     thread_5.join()
#     thread_6 = threading.Thread(target=photo, args=[20])
#     thread_6.start()
#     thread_6.join()
#     thread_7 = threading.Thread(target=photo, args=[20])
#     thread_7.start()
#     thread_7.join()
#     thread_8 = threading.Thread(target=photo, args=[20])
#     thread_8.start()
#     thread_8.join()
#
#
# if __name__ == '__main__':
#     main()
start = time.time()
n = []
def photo(num,nums):
    for e in range(num,nums):
        if e == 1:
            add_url = r"https://pic.netbian.com/4kdongman/"  # todo:其它版块  1.shoujibizhi(68页)   2.4kmeinv(137页)   3.4kfengjing(205页)  4.4kdongman(161页)
        else:
            add_url = r"https://pic.netbian.com/4kdongman/" + "/index_" + str(e) + ".html"
        print(add_url)
        add_Beauty_img = requests.get(url=add_url, headers=headers).text
        add_Beauty_img_text = etree.HTML(add_Beauty_img)
        add_li_list = add_Beauty_img_text.xpath('//div[@class="slist"]//li')
        for f in add_li_list:
            li_src = f.xpath('./a/img/@src')[0]
            a = "https://pic.netbian.com" + li_src
            img_url = requests.get(url=a, headers=headers).content
            img_name = f.xpath('./a/img/@alt')[0] + ".jpg"
            new_img_name = img_name.encode('iso=8859-1').decode('gbk')
            img_path = "./addBeauty/" + new_img_name
            with open(img_path, "wb")as af:
                af.write(img_url)
            n.append(f)
            print(new_img_name, "图片下载成功！！！")
        if e == num - 1:
            for m in enumerate(n):
                print("第{}图片下载成功！！！".format(m[0] + 1))



def main():
    thread_list = []
    for i in range(1,3):
        thread = threading.Thread(target=photo,args=[1,10])
        thread.start()
        thread_list.append(thread)
    for num in thread_list:
        num.join()


ending = time.time()
print("一共用时{}秒".format(ending-start))