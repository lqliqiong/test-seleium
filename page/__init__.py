from selenium.webdriver.common.by import By

"""
以下数据为模块配置数据
 1:元素配置信息统一存放管理
 2：能使用css选择器定位，不适用xpath
"""
url_mp = "http://ttmp.research.itcast.cn/"

# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_but = (By.CSS_SELECTOR, ".el-button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")

# 内容管理
mp_content_manage = (By.XPATH, "//span[text()='内容管理']/..")
# 发布文章
mp_publish_article = (By.XPATH, "//*[contains(text(),'发布文章')]")
# 文章title
mp_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
# iframe
mp_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
# 文章内容
mp_content = (By.CSS_SELECTOR, "#tinymce")
# 封面
mp_cover = (By.XPATH, "//*[text()='自动']")
# 发表
mp_submit = (By.XPATH, "//*[text()='发表']/..")
# 信息
mp_message = (By.XPATH, "//*[contains(text(),'新增文章成功')]")


"""
后台管理元素
"""
url_mp = "http://ttmis.research.itcast.cn"

# 用户名
mp_username = (By.CSS_SELECTOR, "[name='username']")
# 密码
mp_pwd = (By.CSS_SELECTOR, "[name='password']")
# 密码
mp_pwd_ver = (By.CSS_SELECTOR, ".yzm_btn")
# 登录按钮
mp_login_but = (By.CSS_SELECTOR, "#inp1")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")







