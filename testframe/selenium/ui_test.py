#!/usr/bin/python
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from config.setting import BROWSER_DRIVER
from testframe.selenium.base_selenium import BaseSelenium


class UITest(BaseSelenium):
    # 打开浏览器
    def openBrowser(self, type1, url):
        if BROWSER_DRIVER is None:
            raise WebDriverException('Driver executable needs to be in PATH. Please set the `BROWSER_DRIVER` value')

        self.loggers.info('Request url:  %s' % url)
        if type1 == 'firefox' or type1 == 'f':
            self.openFirefox()
        elif type1 == 'chrome' or type1 == 'c':
            self.openChrome()
        elif type1 == 'app' or type1 == 'a':
            self.openChromeApp()
        elif type1 == 'phantomjs' or type1 == 'js':
            self.openPhantomJS()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'Chrome' or 'Firefox','c', 'f'." % type1)
        # 开始请求
        self.browser.get(url)
        time.sleep(2)
        return self.browser.current_window_handle

    # 跳转url
    def goto(self, url):
        self.browser.get(url)
        self.loggers.debug("跳转到" + url)

    # 回退
    def goback(self):
        self.browser.back()
        self.wait(2)

    # 窗口最大化显示
    def maximizeWindow(self):
        self.browser.maximize_window()

    # 在新标签页中打开窗口，用firefox浏览器会打开两个窗口而不是两个标签页，所以最好用chrome
    def newWindow(self, url):
        self.browser.execute_script('window.open("' + url + '")')
        time.sleep(5)
        handles = self.browser.window_handles  # 获取当前窗口句柄集合（列表类型）
        # count = -1;
        # for handle in handles:
        #     count = count + 1
        self.browser.switch_to_window(handles[-1])
        return self.browser.current_window_handle

    # 根据页面title切换窗口，需要用准确的title，F12页面元素中有
    def selectWindowByTitle(self, titlename):
        handles = self.browser.window_handles
        count = -1
        windows = {}
        for handle in handles:
            count = count + 1
            self.browser.switch_to_window(handles[count])
            title = self.browser.title
            windows[title] = handle
        for key in windows:
            if titlename == key:
                self.loggers.info("匹配到窗口：" + titlename + ",该窗口句柄：" + windows[titlename])
                self.browser.switch_to_window(windows[titlename])
                break

    # 关闭当前窗口
    def closeWindow(self):
        self.browser.close()

    # 关闭所有窗口
    def closeWindowAll(self):
        self.browser.quit()

    # 获取元素属性值
    def getAttribute(self, selector, attr):
        attrvalue = self.findElement(selector)
        attrvalue = attrvalue.get_attribute(attr)
        self.loggers.info("通过<getAttribute>[" + selector + "]获取属性值：" + attrvalue)
        return attrvalue

    # 判断元素是否存在
    def isElementExists(self, selector):
        s = self.findElement(selector)
        if s is not None:
            self.loggers.info("通过<isElementExists>[" + selector + "]" + "元素存在")
            return s
        else:
            self.get_windows_img()
            self.loggers.error("通过<isElementExists>[" + selector + "]" + "元素不存在")

    # 返回元素的结果是否可见（逻辑可视visible），返回结果为True 或False
    def isDisplayed(self, selector):
        s1 = self.findElement(selector)
        if s1 is not None:
            s2 = s1.is_displayed()
            if s2 is not None:
                self.loggers.info("通过<isElementVisible>[" + selector + "]" + "元素可视")
                return s2
            else:
                self.get_windows_img()
                self.loggers.error("通过<isElementVisible>[" + selector + "]" + "元素不可视")
        else:
            self.get_windows_img()
            self.loggers.error("通过<isElementVisible>[" + selector + "]" + "元素不存在")

    # 鼠标左键点击
    def click(self, selector):
        if self.findElement(selector) is not None:
            self.loggers.info("通过<click>[" + selector + "]点击")
            self.findElement(selector).click()
            time.sleep(1)
        else:
            self.get_windows_img()
            self.loggers.error("通过<click>[" + selector + "]未查找到元素")

    # 文本框输入
    def inputText(self, selector, text1):
        if self.findElement(selector) is not None:
            self.loggers.info("通过<inputText>[" + selector + "]输入文本：" + text1)
            self.findElement(selector).clear()
            self.findElement(selector).send_keys(text1)
        else:
            self.get_windows_img()
            self.loggers.error("通过<input>[" + selector + "]未查找到元素")

    # 获取文本
    def getText(self, selector):
        if self.findElement(selector) is not None:
            summary = self.findElement(selector).text
            self.loggers.info("通过<getText>[" + selector + "]获取文本：" + summary)
            return summary
        else:
            self.get_windows_img()
            self.loggers.error("通过<getText>[" + selector + "]未查找到元素")

    # 元素内容应该包含预期
    def elementTextShouleContain(self, locator, excepted):
        if self.findElement(locator) is not None:
            actual = self.findElement(locator).text
            if excepted in actual:
                self.loggers.info("通过<elementTextShouleContain>[" + locator + "]匹配成功:" + excepted)
            else:
                self.get_windows_img()
                self.loggers.error("通过<elementTextShouleContain>[" + locator + "]查到内容是：" + actual)
        else:
            self.get_windows_img()
            self.loggers.error("通过<elementTextShouleContain>[" + locator + "]未查找到元素")

    # 元素内容应该等于预期
    def elementTextShouleBe(self, locator, excepted):
        if self.findElement(locator) is not None:
            actual = self.findElement(locator).text
            if excepted == actual:
                self.loggers.info("通过<elementTextShouleBe>[" + locator + "]匹配成功:" + excepted)
            else:
                self.get_windows_img()
                self.loggers.error("通过<elementTextShouleBe>[" + locator + "]查到内容是：" + actual)
        else:
            self.get_windows_img()
            self.loggers.error("通过<elementTextShouleBe>[" + locator + "]未查找到元素")

    # 元素属性应该等于预期
    def elementAttrShouldBe(self, locator, attr, excepted):
        if self.findElement(locator) is not None:
            actual = self.getAttribute(locator, attr)
            if excepted == actual:
                self.loggers.info("通过<elementAttrShouldBe>[" + locator + "]匹配成功:" + excepted)
            else:
                self.get_windows_img()
                self.loggers.error("通过<elementAttrShouldBe>[" + locator + "]查到内容是：" + actual)
        else:
            self.get_windows_img()
            self.loggers.error("通过<elementAttrShouldBe>[" + locator + "]未查找到元素")

    # 返回 alert/confirm/prompt 中的文字信息
    def get_alert_text(self):
        return self.browser.switch_to.alert.text

    # 接受现有警告框
    def accept_alert(self):
        self.browser.switch_to.alert.accept()

    # 解散现有警告框
    def dismiss_alert(self):
        self.browser.switch_to.alert.dismiss()

    # 当被定位的元素在frame里，需要先选择frame，否则无法定位
    def selectFrame(self, frame):
        self.browser.switch_to_frame(frame)
        self.loggers.info("选择frame:" + frame)

    # 对应去除选择frame
    def unselectFrame(self):
        self.browser.switch_to_default_content()
        self.loggers.info("去除选择frame")

    # 下拉菜单选择by value，定位的元素必须是select
    def selectFromListByValue(self, locator, value):
        select = Select(self.findElement(locator))  # 实例化Select
        select.select_by_value(value)
        self.loggers.info("通过value选择下拉菜单：" + value)

    # 下拉菜单选择by index，定位的元素必须是select
    def selectFromListByIndex(self, locator, index):
        select = Select(self.findElement(locator))
        select.select_by_index(index)
        self.loggers.info("通过index选择下拉菜单：" + index)

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.browser.execute_script(src)

    # HTML 调用JS 定位class参数位置 修改当前值
    def alter_class(self, cla, css):
        '''
        x=document.getElementsByName;getElementById;getElementsByClassName
        alert(x[0].value) 取值
        alert(x[0].innerHTML = "333") 赋值
        alert(x.length);字段个数
        '''
        js = "var q=document.getElementsByClassName(\"" + cla + "\");q[0].innerHTML = \"" + css + "\";"
        try:
            self.loggers.debug("JS = %s" % js)
            self.browser.execute_script(js)  # 调用js
        except NoSuchElementException as e:
            self.get_windows_img()
            self.loggers.error("NoSuchElementException: %s" % e)
            self.loggers.error("js = %s" % js)

    # HTML修改常用参数
    def alter_name_size(self, cla, css):
        # < input name = "myInput" type = "text"  size = "20" / > <br />
        # js = "var list=document.getElementsByName(""myInput");for(i=0;i<list.length;i++){list[i].size= 10;}"
        js = "var list=document.getElementsByName(\"" + cla + "\");for(i=0;i<list.length;i++){list[i].size=" + css + ";}"
        try:
            self.browser.execute_script(js)  # 调用js
        except NoSuchElementException as e:
            self.get_windows_img()
            self.loggers.error("NoSuchElementException: %s" % e)
            self.loggers.error("js = %s" % js)

    # 调用JS 定位class参数位置，修改指定参数的值
    def alter_class_date(self, cla1, cla2, val):
        '''
        <input name="myInput" id="zoom2" type="text" size="20" data-date= "2019-02-15" aaa="sqes" /><br />
        var a=document.getElementsByName("myInput");
        var value_datadate = a[0].getAttribute("data-date");//获取值
        a[0].setAttribute("data-date", "small"); //设置值
        '''
        js = "var a=document.getElementsByClassName(\"" + cla1 + "\"); var value_datadate = a[0].getAttribute(\"" + cla2 + "\");a[0].setAttribute(\"" + cla2 + "\", \"" + val + "\");"
        try:
            self.loggers.debug("JS = %s" % js)
            self.browser.execute_script(js)  # 调用js
        except NoSuchElementException as e:
            self.get_windows_img()
            self.loggers.error("NoSuchElementException: %s" % e)
            self.loggers.error("js = %s" % js)

    # 调用JS 定位name参数位置，修改指定参数的值
    def alter_name_date(self, cla1, cla2, val):
        '''
        <input name="myInput" id="zoom2" type="text" size="20" data-date= "2019-02-15" aaa="sqes" /><br />
        var a=document.getElementsByName("myInput");
        var value_datadate = a[0].getAttribute("data-date");//获取值
        a[0].setAttribute("data-date", "small"); //设置值
        '''
        js = "var a=document.getElementsByName(\"" + cla1 + "\"); var value_datadate = a[0].getAttribute(\"" + cla2 + "\");a[0].setAttribute(\"" + cla2 + "\", \"" + val + "\");"
        try:
            self.loggers.debug("JS = %s" % js)
            self.browser.execute_script(js)  # 调用js
        except NoSuchElementException as e:
            self.get_windows_img()
            self.loggers.error("NoSuchElementException: %s" % e)
            self.loggers.error("js = %s" % js)

    # 调用JS 定位ID参数位置，修改指定参数的值
    def alter_id_date(self, cla1, cla2, val):
        '''
        <input name="myInput" id="zoom2" type="text" size="20" data-date= "2019-02-15" aaa="sqes" /><br />
        var a = document.getElementById("zoom1");
        var value_big = a.getAttribute("big");//获取值
        a.setAttribute("big", "small"); //设置值
        '''
        js = "var a=document.getElementById(\"" + cla1 + "\"); var value_datadate = a.getAttribute(\"" + cla2 + "\");a.setAttribute(\"" + cla2 + "\", \"" + val + "\");"
        try:
            self.browser.execute_script(js)  # 调用js
        except NoSuchElementException as e:
            self.get_windows_img()
            self.loggers.debug("NoSuchElementException: %s" % e)
            self.loggers.debug("js = %s" % js)

    # 时间
    def timeFormat(self, a):
        if a > 0:
            days = 86400 * a
            da = time.strftime('%Y-%m-%d', time.localtime(time.time() + days))
            self.loggers.debug("Day is %s" % da)
        else:
            da = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            self.loggers.debug("Today's date is %s" % da)
        return da


if __name__ == '__main__':
    c = UITest()
    c.openBrowser("c", "http://www.baidu.com")
    c.wait(1)
    c.maximizeWindow()
    c.wait(1)
    c.inputText("id=>kw", "selenium")
    c.click("id=>su")
    c.closeWindowAll()
