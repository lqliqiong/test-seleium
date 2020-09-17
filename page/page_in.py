from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin
from tool.get_logger import GetLogger

log = GetLogger.get_logger()


class PageIn:
    """
    调用业务层page方法
        通过统一入口类（PageIn）实现
    """

    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpLogin对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)
    # pass
