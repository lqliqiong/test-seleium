from base.web_base import WebBase


class PageMisLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        pass

    # 输入密码
    def page_input_pwd(self, password):
        pass

    # 点击登录按钮
    def page_click_login_btn(self):
        # 验证码校验
        # 点击提交按钮
        pass

    # 获取昵称封装
    def page_get_nickname(self):
        pass

    # 组合业务方法
    def page_mis_login(self, username, password):
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()
        self.page_get_nickname()
