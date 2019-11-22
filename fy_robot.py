#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 10:27
# @Author  : 牛仔很忙
# @FileName: fy_robot.py
# @Software: PyCharm
# @github    : https://github.com/zhangliu520
# @qq        : 752477168
# @qq群      : 779726535

import requests
from selenium import webdriver
import traceback
import time
class BDTransfer:
    '''
    即时翻译小程序
    '''
    db_fanyi_url='https://fanyi.baidu.com/?aldtype=16047#zh/en/%E4%B8%AD%E6%96%87'

    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  #没有界面模式

        self.driver = webdriver.Chrome(chrome_options=chrome_options) #获取浏览器对象

        self.driver.get(self.db_fanyi_url) #打开翻译网站
        self.driver.refresh()
        time.sleep(3)


    def output(self,input_word):
        '''
        :param input_word: 输入中文英文
        :return: 返回翻译
        '''
        input_word_element=self.driver.find_element_by_id('baidu_translate_input') #获取输入元素
        input_word_element.clear()#清空输入数据
        input_word_element.send_keys(input_word) #填入数据

        self.driver.find_element_by_id('translate-button').click()#按确认按钮

        #输出
        if len(input_word) >=20:
            time.sleep(3)  #todo 网络有延迟可以设置大点,有可能搜索前一个结果.
        else:
            time.sleep(0.3)

        return self.driver.find_element_by_class_name('target-output').text

    def __del__(self):
        self.driver.close()  # 关闭驱动


    def run(self):
        while 1:
            try:
                word=input("即时翻译系统(输入Q退出)》》》输入:")
                if word in ['Q','q']:break
                result=self.output(word)
            except Exception as e:
                result="翻译出现错误,原因:{}".format(str(e))

            print('翻译结果》》》:{}'.format(result))
if  __name__ == '__main__':
    BDTransfer().run()

