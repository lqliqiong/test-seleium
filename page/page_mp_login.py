from time import sleep

import page
from base.web_base import WebBase


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        # 读取__init__py配置内容
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.bass_click(page.mp_login_but)

    # 获取昵称封装->测试脚本断言使用
    def page_get_nickname(self):
        nickname = self.base_get_text(page.mp_nickname)
        return nickname

    # 组合业务方法
    def page_mp_login(self, username, code):
        """
        调用相同页面的操作步骤
        跨页面不考虑
        :return:
        """
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法-发布文章依赖使用
    def page_mp_login_success(self, username, code):
        """
        调用相同页面的操作步骤
        跨页面不考虑
        :return:
        """
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
