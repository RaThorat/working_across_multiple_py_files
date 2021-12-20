# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:55:39 2021

@author: r.thorat
"""
#calling commands from functions files to get file 1 and file 2
from functions_demo import getfile1
from functions_demo import getfile2

#function to close the gui, used later in the functions per page
def Close():
    app.destroy()

##https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
import tkinter as tk
from tkinter import ttk
#from tkinter.messagebox import showinfo


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}
        

        
		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")
            


		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
   
     
# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
        
        # putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 1, padx = 10, pady = 10)
		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Task 1", 
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        ## button to show frame 2 with text layout2
		button3 = ttk.Button(self, text ="Task2", 
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
class Page1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Task1",  font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        # button to show proposalinfo with text
		# layout3
		my_label3 = ttk.Label(self, text ="Use below button for file1")

        # putting the button in its place by
		# using grid
		my_label3.grid(row = 1, column = 2, padx = 10, pady = 10)


		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Back to Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 1, padx = 10, pady = 10)
        # button to show proposalinfo with text
		# layout3
		button3 = ttk.Button(self, text ="Import file1",
							command =getfile1)
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 2, column = 2, padx = 10, pady = 10)
        
        
        
        # button to show proposalinfo with text
		# layout3
		button4 = ttk.Button(self, text ="Close",
							command =Close)
	
		# putting the button in its place by
		# using grid
		button4.grid(row = 2, column = 1, padx = 10, pady = 10)
        
       
#https://stackoverflow.com/questions/63374453/is-it-possible-to-reference-a-variable-directly-from-a-stored-tkinter-widget         
# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Task2",  font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
        # button to show proposalinfo with text
		# layout3
		my_label3 = ttk.Label(self, text ="Use below button for file2")

        # putting the button in its place by
		# using grid
		my_label3.grid(row = 1, column = 2, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Back to Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 1, padx = 10, pady = 10)
        # button to show Input file for clustering with text
		# layout3
		button3 = ttk.Button(self, text ="Input file 2",
							command =getfile2)
        # putting the button in its place by
		# using grid
		button3.grid(row = 1, column = 2, padx = 10, pady = 10)
        
		# layout3
		button5 = ttk.Button(self, text ="Close",
							command =Close)
	
		# putting the button in its place by
		# using grid
		button5.grid(row = 4, column = 1, padx = 10, pady = 10) 
        
# Driver Code
app = tkinterApp()
#https://newbedev.com/how-to-change-the-color-of-ttk-button
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#232323', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','#ff0000')])
app.title("This is my Interface")
#app.bind('<Return>', run_and_close)
#app.bind('<Escape>', close)

app.mainloop()