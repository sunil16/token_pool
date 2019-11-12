# -*- coding: utf-8 -*-

import os
try:
    import configparser
except:
    from six.moves import configparser

BRAND_NAME = "Token Pooling"
SECRET_KEY = "df5JGZfDLMDF54RWrK_aq6Yb9HsdhdjGDDhdaPw="

APP_ENV = os.environ.get("APP_ENV") or "local"  # or 'live' to load live
INI_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "./conf/{}.ini".format(APP_ENV)
)

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

REDIS = CONFIG["redis"]
if APP_ENV == "dev" or APP_ENV == "live":  # credentials not available for dev and live
    R_CONFIG = (
        REDIS["r_host"],
        REDIS["r_port"],
        REDIS["r_db"]
    )
    REDISTOGO_URL = "redis://%s:%s/%s" % R_CONFIG
else:
    R_CONFIG = (REDIS["r_host"], REDIS["r_port"], REDIS["r_db"])
    REDISTOGO_URL = "redis://%s:%s/%s" % R_CONFIG

POOL_SIZE =  CONFIG["pool_size"]['size']
WAIT_TIME_SECONDS =  CONFIG["token_task_execution_time"]['wait_time_seconds']
