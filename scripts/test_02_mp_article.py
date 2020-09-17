import pytest

import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import readyaml


class TestMpLogin:
    # 初始化
    def setup_class(self):

        # 1:获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2:获取统一入口类获取类
        self.page_in = PageIn(driver)

        # 获取PageMpLogin对象并调用登录成功依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success("13812345678", 246810)

        # 获取PageMpLogin页面对象
        self.article = self.page_in.page_get_PageMpArticle()

        pass

    # 结束"
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()
        pass

    # 测试业务方法
    @pytest.mark.parametrize("title, content, click_text", readyaml("mp_article.yml"))
    def test_mp_login(self, title, content, click_text,expect):

        try:
            # 调用登录业务方法
            self.article.page_mp_articel(title, content, click_text)
            # 断言
            assert expect == self.article.page_get_info()
        except  Exception as e:
            print("错误原因", e)
            self.article.base_get_img()
            raise
