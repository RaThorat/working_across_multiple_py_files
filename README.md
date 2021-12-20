# working_across_multiple_py_files
How to trigger tasks in main.py based on input from gui.py which contains commands from functions.py, which itself refers to task.py's?
When a user runs the main.py file, a GUI appears with a start page. On that start page, there are two buttons; Task1 and Task2. When he/she clicks on the Task1 button, Task1 page appears. On that page, there is a button. If it is clicked, a window appears to select an excel from documents directory. When this input is given, Task1 is performed, that is printing out the excel. After the completion of the Task1 I would like that the user still has GUI open, where he/she can click on the Task2 button to select another excel from the documents directory. When this input is given, the Task2 is performed, that is printing out the excel.

Extra info: On each of these pages (Start page, Task1, Task2) there is a button to close the gui. On page Task1 and Task2 there is also a button to go back to Startpage.
https://stackoverflow.com/questions/70285772/how-to-trigger-tasks-in-main-py-based-on-input-from-gui-py-which-contains-comman
