'''
使用python自动化运营微博
1.掌握Selenuim自动化测试工具，以及元素定位方法
2.学会编写微博自动化模块：加关注、写平路、发微博
3.对微博自动化做自我总结
selenium:关注程序执行的流程本身，比如找到指定的元素，设置相应的值，然后点击操作
如果我们想定位一个元素，可以通过id、name、class、tag，链接上的全部文本，链接上的部分文本，
XPath或者CSS进行定位
在Selenium Webdriver中提供了8种方法，方便我们定位元素
1.通过id定位，比如：browser.find_element_by_id('loginName')
2.通过name定位，比如：browser.find_element_by_name('key_word')
3.通过class：find_element_by_class_name()
4.通过tag：find_element_by_tag_name()
5.通过link上的完整文本定位：find_element_by_link_text()
6.通过link上的部分文本定位：find_element_by_partical_link_text()
7.通过XPath定位，使用find_element_by_xpath(),使用xpath通用性比较好
8.通过CSS定位，使用find_element_by_css_selector(),使用xpath通用性比较好
对元素操作，有以下函数
clear：清空输入框内容；
send_keys(content):传入要输入的文本
click(),submit()
'''
from selenium import webdriver
import time

browser = webdriver.Chrome()


# 登录微博
def weibo_login(username, password):
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)


# 设置用户名、密码
username = '18616908332'
password = "921202zx"
weibo_login(username, password)


# 添加指定的用户
def add_follow(uid):
    browser.get('https://m.weibo.com/u/' + str(uid))
    time.sleep(1)
    # browser.find_element_by_id("follow").click()
    follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
    follow_button.click()
    time.sleep(1)
    # 选择分组
    group_button = browser.find_element_by_xpath('//div[@class="m-btn m-btn-white m-btn-text-black"]')
    group_button.click()
    time.sleep(1)


# 每天学点心理学 UID
# uid = '1890826225'
# add_follow(uid)


# 给指定某条微博添加内容
def add_comment(weibo_url, content):
    browser.get(weibo_url)
    browser.implicitly_wait(5)
    content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
    content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
    time.sleep(2)
    comment_button = browser.find_element_by_css_selector(".W_btn_a").click()
    time.sleep(1)


# 发文字微博
def post_weibo(content):
    # 跳转到用户的首页
    browser.get('https://weibo.com')
    browser.implicitly_wait(5)
    # 点击右上角的发布按钮
    post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
    # 在弹出的文本框中输入内容
    content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
    time.sleep(2)
    # 点击发布按钮
    post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
    time.sleep(1)


# 给指定的微博写评论
weibo_url = 'https://weibo.com/1890826225/HjjqSahwl'
content = 'Gook Luck! 好运已上路！'
# 自动发微博
content = '每天学点心理学'
post_weibo(content)
