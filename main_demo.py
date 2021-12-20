# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:54:21 2021

@author: r.thorat
"""
#GUI file calling
import gui_demo
#Functions file calling
import functions_demo
#importing function Task1 from file Task1
from Task1_demo import Task1
#importing function Task2 from file Task2
from Task2_demo import Task2

#defining main() function
def main():
    Task1()
    Task2()
#calling main()    
if __name__ == "__main__": 
    main()