import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

# BACKENDをTextからSlackに修正
BACKEND = 'Slack'

# 前述のAPI Tokenを入力
env_token = os.getenv("TOKEN")
BOT_IDENTITY = {
    'token': env_token
}

# adminにしたいユーザのアカウント名をタプルのかたちで入力（複数可）
BOT_ADMINS = ('@chapa')

BOT_DATA_DIR = r'data'
BOT_EXTRA_PLUGIN_DIR = r'plugins'

BOT_LOG_FILE = r'errbot.log'
BOT_LOG_LEVEL = logging.DEBUG
