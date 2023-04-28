# base.py

import logging

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 数据库连接信息
DATABASE_HOST = 'localhost'
DATABASE_PORT = 3306
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'password'
DATABASE_NAME = 'myapp'