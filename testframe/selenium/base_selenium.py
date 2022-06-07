#!/usr/bin/python
import os
import time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from config.setting import BROWSER_DRIVER
from testframe.common.logger import Log
from testframe.common.base_common import BaseCommon


class BaseSelenium(BaseCommon):
    def __init__(self):
        self.browser = None

    def sleep(self, sec):
        self.loggers.debug("等待" + str(sec) + "s")
        time.sleep(sec)

    # 隐式等待
    def wait(self, seconds):
        self.browser.implicitly_wait(seconds)
        self.loggers.debug("wait for %d seconds." % seconds)

    def openFirefox(self):
        # 打开浏览器
        self.browser = webdriver.Firefox(BROWSER_DRIVER)

    def openChrome(self):
        # 打开浏览器
        self.browser = webdriver.Chrome(BROWSER_DRIVER)

    def openChromeApp(self):
        # 打开浏览器
        mobile_emulation = {'deviceName': 'iPhone 6'}
        # mobile_emulation = {'deviceName': 'Google Nexus 7'}
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  # 划重点, 加上这句, 就不会报崩溃了, 当然也可能是chromedriver和chrome的版本匹配问题
        options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug

        options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(BROWSER_DRIVER, chrome_options=options)

    def openPhantomJS(self):
        # 打开浏览器
        self.browser = webdriver.PhantomJS(BROWSER_DRIVER)

    # 设置浏览器宽、高
    def setWindowSize(self, width, height):
        self.browser.set_window_size(width, height)

    # 浏览器后退
    def back(self):
        self.browser.back()

    # 浏览器前进
    def forward(self):
        self.browser.forward()

    def refresh(self):
        self.browser.refresh()
        self.loggers.debug("refresh page.")

    # 点击关闭当前窗口
    def close(self):
        self.browser.close()

    # 定位元素方法
    def findElement(self, selector):
        """
            Judge element positioning way, and returns the element.
        """
        element = ""
        if '=>' not in selector:
            return self.findElementById(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "" or selector_value == "":
            raise NameError(
                "Grammatical errors, reference: 'id=>useranme'.")
        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.findElementById(selector_value)
            except NoSuchElementException as e:
                self.loggers.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.findElementByName(selector_value)
        elif selector_by == "c" or selector_by == 'class':
            element = self.findElementByClassName(selector_value)
        elif selector_by == "l" or selector_by == 'linktext':
            element = self.findElementByLinkText(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.findElementByPartialLinkText(selector_value)
        elif selector_by == "t" or selector_by == 'tag':
            element = self.findElementByTagName(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.findElementByXpath(selector_value)
            except NoSuchElementException as e:
                self.loggers.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'css':
            element = self.findElementByCssSelector(selector_value)
        else:
            # element = self.findElementById(selector_value)
            raise NameError("Please enter a valid type of targeting elements.")
        self.loggers.debug("Had find the element successful "
                           "by %s via value: %s " % (selector_by, selector_value))
        return element

    def findElementById(self, eId):
        handle = None
        for num in range(0, 5):
            try:
                handle = self.browser.find_element_by_id(eId)
            except:
                time.sleep(1)
        return handle

    def findElementByName(self, eName):
        handle = None
        for num in range(0, 30):
            try:
                handle = self.browser.find_element_by_name(eName)
            except:
                time.sleep(1)
        return handle

    def findElementByClassName(self, eName):
        handle = None
        for num in range(0, 30):
            try:
                handle = self.browser.find_element_by_class_name(eName)
            except:
                time.sleep(1)
        return handle

    def findElementByTagName(self, eTName):
        handle = None
        for num in range(0, 30):
            try:
                handle = self.browser.find_element_by_tag_name(eTName)
            except:
                time.sleep(1)
        return handle

    def findElementByLinkText(self, text):
        handle = None
        for num in range(0, 30):
            try:
                handle = self.browser.find_element_by_link_text(text)
            except:
                time.sleep(1)
        return handle

    def findElementByXpath(self, xpath):
        handle = None
        for num in range(0, 5):
            try:
                handle = self.browser.find_element_by_xpath(xpath)
            except:
                time.sleep(1)
        return handle

    def findElementByCssSelector(self, xpath):
        handle = None
        for num in range(0, 5):
            try:
                handle = self.browser.find_element_by_css_selector(xpath)
            except:
                time.sleep(1)
        return handle

    def findElementByPartialLinkText(self, xpath):
        handle = None
        for num in range(0, 5):
            try:
                handle = self.browser.find_element_by_partial_link_text(xpath)
            except:
                time.sleep(1)
        return handle

    # 清除元素的内容
    def clear(self, element):
        element.clear()

    # 在元素上模拟按键输入
    def sendKeys(self, element, text):
        element.send_keys(text)

    # 提交表单
    def submit(self, element):
        element.submit()

    # 返回元素的尺寸
    def size(self, element):
        return element.size

    # 获取元素的文本
    def text(self, element):
        return element.text

    # 右击
    def contextClick(self, element):
        ActionChains(self.browser).context_click(element).perform()

    # 双击
    def doubleClick(self, element):
        ActionChains(self.browser).double_click(element).perform()

    # 拖动
    def dragAndDrop(self, element, target):
        ActionChains(self.browser).drag_and_drop(element, target).perform()

    # 鼠标悬停在一个元素上
    def moveToElement(self, element):
        ActionChains(self.browser).move_to_element(element).perform()

    # 按下鼠标左键在一个元素上
    def clickAndHold(self, element):
        ActionChains(self.browser).click_and_hold(element).perform()

    def getHandles(self):
        return self.browser.window_handles

    def getCurrentHandles(self):
        return self.browser.current_window_handle

    def url(self):
        return self.browser.current_url

    def title(self):
        return self.browser.title

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        img_name = rq + '.png'
        screen_name = os.path.join(Log.get_result_path(), img_name)
        try:
            self.browser.get_screenshot_as_file(screen_name)
            self.loggers.debug("Had take screenshot and save to folder : /screenshots")
            print('img: ', rq, '.png')
        except NameError as e:
            self.loggers.error("Failed to take screenshot! %s" % e)
            # import platform
            # if platform.system() == 'Windows':
            #     self.window_capture()
            # elif platform.system() == 'Linux':
            #     pass

    # # WINDOW屏幕截图，图片过大 注意使用
    # def window_capture(self):
    #     # pip install pywin32==227
    #     import win32gui, win32ui, win32con, win32api
    #     hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    #     # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    #     hwndDC = win32gui.GetWindowDC(hwnd)
    #     # 根据窗口的DC获取mfcDC
    #     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    #     # mfcDC创建可兼容的DC
    #     saveDC = mfcDC.CreateCompatibleDC()
    #     # 创建bigmap准备保存图片
    #     saveBitMap = win32ui.CreateBitmap()
    #     # 获取监控器信息
    #     MoniterDev = win32api.EnumDisplayMonitors(None, None)
    #     w = MoniterDev[0][2][2]
    #     h = MoniterDev[0][2][3]
    #     # print w,h　　　#图片大小
    #     # 为bitmap开辟空间
    #     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    #     # 高度saveDC，将截图保存到saveBitmap中
    #     saveDC.SelectObject(saveBitMap)
    #     # 截取从左上角（0，0）长宽为（w，h）的图片
    #     saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    #     # 存储路径和图片名
    #     rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    #     img_name = rq + '.png'
    #     screen_name = os.path.join(Log.get_result_path(), img_name)
    #     # screen_name = BASE_DIR + '/export/screenshots/' + rq + '.png'
    #
    #     saveBitMap.SaveBitmapFile(saveDC, screen_name)

    # 以元素为起点向下滑动，实现下拉操作；向下滑动为负数，向上滑动为正数
    def slippage(self, selector, x=0, y=0):
        button = self.findElement(selector)
        time.sleep(1)
        Action = TouchActions(self.browser)
        Action.scroll_from_element(button, x, y).perform()
        time.sleep(2)

    # 以元素为起点以一定速度向下滑动，实现下拉操作；向上滑动为负数，向下滑动为正数
    def slippage_speed(self, selector, x=0, y=0, speed=0):
        button = self.findElement(selector)
        time.sleep(1)
        Action = TouchActions(self.browser)
        Action.flick_element(button, x, y, speed).perform()
        time.sleep(2)
