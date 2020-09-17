from selenium import webdriver


class GetDriver:
    # 1:声明变量
    __web_driver = None

    # 2：获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 设置driver
            cls.__web_driver = webdriver.Chrome()
            # 获取浏览器
            cls.__web_driver.maximize_window()
            # 最大化浏览器
            cls.__web_driver.get(url)
            # 打开url
        # 返回driver
        return cls.__web_driver

    # 3：退出driver
    @classmethod
    def quit_web_driver(cls):

        # 判断driver不为空
        if cls.__web_driver is not None:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver=None
