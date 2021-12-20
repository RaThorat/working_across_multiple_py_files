# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:12:05 2021

@author: r.thorat
"""

import functions_demo


def Task1():
    df_train=functions_demo.df_f1
    df_train.to_excel('Task1_output.xlsx')