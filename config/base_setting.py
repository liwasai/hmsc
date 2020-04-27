SERVER_PORT = 9000
SQLALCHEMY_DATABASE_URI = 'mysql://root:LCM123456@192.144.237.95/hmsc_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False 

# cookie
AUTH_COOKIE_NAME='hsmc_1901c'

# 设置拦截器的忽略规则
IGNORE_URLS = [
    '^/user/login'
]
IGNORE_CHECK_LOGIN_URLS =[
    '^/static',
    '/favicon.ico'
]