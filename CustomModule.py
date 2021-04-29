# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:58:35 2021

@author: Uday Sharma
"""

def output_message():
    print("Hey ! This is working ..... Cool")
    
def welcome_by_name(name):
    print("Hii There {} . Good to meet you ".format(name))
def multply():
    user_input = int(input("Please provide a number . we will multiply it by 314"))
    final_number = user_input * 314
    print("your number is {}".format(final_number))