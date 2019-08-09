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
    # 但是如果相应的环境中没有指定的浏览器，需要指定浏览器位置 webdriver.Chrome(ChromeDriver路径)
    driver = webdriver.Chrome()
    # 打开一个页面
    driver.get(url)
    # 通过函数查找title标签，启动
    print("Title:{0}".format(driver.title))

def testWebDriver01(url):
    # 操作哪个浏览器就可以对哪个浏览器建立一个实例
    # 这里是创建一个Chrome浏览器实例
    # 但是如果相应的环境中没有指定的浏览器，需要指定浏览器位置 webdriver.Chrome(ChromeDriver路径)
    driver = webdriver.Chrome()
    # 打开一个页面
    driver.get(url)
    # 根据ID找到指定的UI元素
    # nav0 = driver.find_element_by_id('nav_0')
    # 将里面的文字内容输出
    # print(nav0.text)
    # 输出页面的title的内容
    # print(driver.title)
    # 得到页面的快照，对指定的页面进行截图
    # driver.save_screenshot("test.png")
    # 根据ID获取指定的UI元素，如果是input，则可以设置输入内容
    # 百度的搜索输入框的ID是kw
    driver.find_element_by_id("kw").send_keys(u"大熊猫")
    # 获取su这个按钮，模拟点击
    driver.find_element_by_id("su").click()
    # 休眠5秒，为了浏览器能够执行完成，获取点击后的相应页面
    time.sleep(5)
    # 截图
    driver.save_screenshot("xiongmao.png")
    # 获取网页返回的所有的cookie
    print(driver.get_cookies())
    # 找到指定的UI元素，然后模拟输入两个按键 ctrl+a 全选操作
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
    # 将获全选的内容进行剪切
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
    # 针对指定的UI空间，输入指定的内容
    driver.find_element_by_id("kw").send_keys(u"航空母舰")
    #为了看见效果。截图操作
    driver.save_screenshot("hangkongmujian.png")
    # 获取指定的按钮，指定回车键操作
    driver.find_element_by_id("su").send_keys(Keys.RETURN)
    time.sleep(5)# 继续休眠5秒
    # 重新截图，查看回车是否生效
    driver.save_screenshot("hangkongmujian2.png")
    # 清空指定UI元素的内容
    driver.find_element_by_id("kw").clear()
    # 截图是否生效
    driver.save_screenshot("clear.png")
    # 最后关闭浏览器
    driver.close()

if __name__ == '__main__':
    # 电影网站
    url = 'http://localhost:8081/upload/forum.php?mod=post&action=newthread&fid=2'
    # 测试输入框的输入
    urlBaidu = "http://www.baidu.com"
    testWebDriver(url)
    # testWebDriver01(urlBaidu)