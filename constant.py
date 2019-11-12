#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : constant.py
 @Time       : 2019-07-01 21:00
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2017, iFuture Corporation Limited.
"""
import os
from envparse import env
from enum import Enum, unique

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
if os.path.exists('~/.env.prod'):
    env.read_envfile('~/.env.prod')
else:
    env.read_envfile('{0}/.env.dev'.format(CURRENT_DIR))

# 配置文件
MONGODB_HOST = env('MONGODB_HOST')
MONGODB_PORT = env.int('MONGODB_PORT')
MONGODB_USER = env('MONGODB_USER')
MONGODB_PWD = env('MONGODB_PWD')
PROD_MONGODB_HOST = env('PROD_MONGODB_HOST')
PROD_MONGODB_PORT = env.int('PROD_MONGODB_PORT')
PROD_MONGODB_USER = env('PROD_MONGODB_USER')
PROD_MONGODB_PWD = env('PROD_MONGODB_PWD')
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
REDIS_PWD = env('REDIS_PWD')
CHINESE_BERT_SERVICE = env('CHINESE_BERT_SERVICE')
MULTI_BERT_SERVICE = env('MULTI_BERT_SERVICE')
DAILY_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
HASH = "#"
LEFT_BRACKET = '['
RIGHT_BRACKET = ']'
GREATER_THAN = '>'
DESCRIPTION = '概要: '
LEFT_ROUND_BRACKET = '('
RIGHT_ROUND_BRACKET = ')'
FIRST_SECTION = 'FIRST_SECTION'
FIRST_SENTENCE = 'FIRST_SENTENCE'
LAST_SECTION = 'LAST_SECTION'
LAST_SENTENCE = 'LAST_SENTENCE'
BAR = '---'
TITLE = 'title'
TAGS = 'tags'
THUMBNAIL = 'thumbnail'
DATE = 'date'

# collections
COLLECTIONS = {
    "animation": "动漫",
    "technology": "科技",
    "novel": "小说",
    "paper": "论文"
    # "entertainment",
}
PUBLISHED = "article-{0}-node"


@unique
class MarkdownType(Enum):
    CATEGORY = 0,
    TITLE = 1,
    REFERENCE = 2,
    NOVEL = 3,
    PAPER = 4,
    IMAGE = 5,

