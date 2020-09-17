from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
import datetime
import os
from tool.get_logger import GetLogger
log = GetLogger.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        """
        解决driver
        """
        self.driver = driver
        pass

    # 查找方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 格式为列表或元组 内容：元素定位信息
        :param timeout: 查找元素超时时间 默认30s
        :param poll: 查找元素频率 默认为0.5s
        :return: 元素
        """
        log.info("正在查找元素:{}".format(loc))
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
                .until(lambda x: x.find_element(*loc)))

    # 输入方法封装
    def base_input(self, loc, value):
        """

        :param loc: 元素定位信息
        :param value:输入值
        """
        # 获取元素
        el = self.base_find(loc)
        # 清空操作
        el.clear()
        # 输入操作
        el.send_keys(value)
        # return el

    # 点击方法封装
    def bass_click(self, loc):
        """

        :param loc:  元素定位信息
        """
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        """

        :param loc:  元素定位信息
        :return: 元素文本
        """
        return self.base_find(loc).text

    def base_get_img(self):
        file_path = BASE_PATH + os.sep + "image" + os.sep + "{}_{}".format(
            datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S"), ".png")
        self.driver.save_screenshot(file_path)
        # self.driver.get_screenshot_as_file("./imge/err.png")
        self.__base_write_img(file_path)

    def __base_write_img(self, file_path):
        with open(file_path, "rb") as f:
            file = f.read()
            allure.attach("错误原因", file, allure.attach_type.PNG)

