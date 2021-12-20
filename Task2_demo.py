# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:16:47 2021

@author: r.thorat
"""

import functions_demo


def Task2():
    df_train=functions_demo.df_f2
    df_train.to_excel('Task2_output.xlsx')