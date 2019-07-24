# 动态HTML的爬取，解析
'''
爬取动态HTML
'''
import requests ,re,time,os
from selenium import webdriver
# 通过keys模拟键盘输入需要导入的模块
from selenium.webdriver.common.keys import Keys


'''
通过keys模拟键盘输入
'''
def testWebDriver(url):
    # 操作哪个浏览器就可以对哪个浏览器建立一个实例
    # 这里是创建一个Chrome浏览器实例
    # 但是如果相应的环境中没有指定的浏览器，需要指定浏览器位置
    driver = webdriver.Chrome()
    # 打开一个页面
    driver.get(url)
    # 通过函数查找title标签，启动
    print("Title:{0}".format(driver.title))


if __name__ == '__main__':
    # 电影网站
    url = 'https://www.50s.wang/whole/1.html'
    testWebDriver(url)