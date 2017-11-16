#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:51:44 2017

@author: sebastian
https://www.reddit.com/r/learnpython/comments/2hjxk5
/whats_the_proper_way_to_use_configparser_across
"""

from configparser import ConfigParser
import os

DEFAULT_CONFIG_FILE = '/Users/sebastian/Desktop/projects/config.ini'


def get_config_file():
    return os.environ.get('CONFIG_FILE', DEFAULT_CONFIG_FILE)

CONFIG_FILE = get_config_file()


def create_config(config_file=None):
    parser = ConfigParser()
    parser.read(config_file or CONFIG_FILE)
    return parser

CONFIG = create_config()

if __name__ == '__main__':
    pass
    # print(CONFIG.sections())
