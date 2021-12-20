# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:00:18 2021

@author: r.thorat
"""

import os
os.getcwd()
from tkinter import filedialog as fd
import pandas as pd
#import seaborn as sns; sns.set()


#Commonpart
def getfile1():
    global df_f1
    import_file_path1 = fd.askopenfilename()
    df_f1 = pd.read_excel(import_file_path1,  engine='openpyxl')
    return df_f1

def getfile2():
    global df_f2
    import_file_path2 = fd.askopenfilename()
    df_f2 = pd.read_excel(import_file_path2,  engine='openpyxl')
    return df_f2