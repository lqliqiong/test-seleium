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
        self.mp = PageIn(driver).page_get_PageMpLogin()
        pass

    # 结束"
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()
        pass

    # 测试业务方法
    @pytest.mark.parametrize("username, code, expect", readyaml("mp_login.yml"))
    def test_mp_login(self, username, code, expect):

        try:
            # 调用登录业务方法
            self.mp.page_mp_login(username, code)
            # 断言
            assert expect == self.mp.page_get_nickname()
        except  Exception as e:
            print("错误原因",e)
            self.mp.base_get_img()
            raise
