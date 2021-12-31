# find_element_by_id            通过元素id定位    element加s，定位多个

# find_element_by_name	        通过元素name定位   element加s，定位多个

# find_element_by_xpath	        通过xpath表达式定位   element加s，定位多个

# find_element_by_link_text     通过完整超链接定位     element加s，定位多个

# find_element_by_partial_link_text	    通过部分链接定位  element加s，定位多个

# find_element_by_tag_name	            通过标签定位   element加s，定位多个

# find_element_by_class_name	        通过类名进行定位    element加s，定位多个

# find_element_by_css_selector	        通过css选择器进行定位  element加s，定位多个

# set_window_size()	 设置浏览器的大小
# back()	         控制浏览器后退
# forward()	         控制浏览器前进
# refresh()	         刷新当前页面
# clear()	         清除文本
# send_keys (value)	 模拟按键输入
# click()	         单击元素
# submit()	         用于提交表单
# get_attribute(name) 获取元素属性值
# is_displayed()	设置该元素是否用户可见
# size	  返回元素的尺寸
# text	  获取元素的文本
from selenium import webdriver
from selenium.webdriver.common import by


a=webdriver.Chrome(r"C:\Users\Git\webdriver\chromedriver.exe")
a.implicitly_wait(10)   #等待时间  每隔半秒去寻找一次结果
a.get("http://www.baidu.com")
a.find_element(by.By.CSS_SELECTOR,"#kw").send_keys("python")    #定位输入框
a.find_element(by.By.CSS_SELECTOR,"#su").click()       #定位搜索按钮


# a.find_element(by.By.CSS_SELECTOR,"#kw").send_keys("python\n")  #打开百度，搜索python