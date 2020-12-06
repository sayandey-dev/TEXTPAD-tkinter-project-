'''
Project name: TEXTPAD
author: Sayan Dey
Institute: Barrackpore Rastraguru Surendranath College
e-main id: sayandeyip@gmail.com

'''

#Creating a notepad project using tkinter (Python)
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

def newFile():
    global file #Declaring file as a global variable
    root.title("Untitled---TEXTPAD")
    file=None
    textArea.delete(1.0, END)   #1.0 denotes the 1st line and the 0th character and the argument is denoting to erase all the elements from 0th character of the 1st line till the END, here END is the tkinter constant

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file) + "- TEXTPAD")
        textArea.delete(1.0, END)   #Deleting all the elements in the textarea
        f=open(file, "r")
        textArea.insert(1.0, f.read())  #Inserts all the elements of the file into the textarea
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")] )

        if file == "":
            file=None
        else:
            #Save as a new file
            f=open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()  

            root.title(os.path.basename(file) + "- TEXTPAD")
            print("File saved")  

    else:
        #Save the file
        f=open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()          

def cut():
    textArea.event_generate(("<<Cut>>"))    #Autometically handels the cut event

def copy():
    textArea.event_generate(("<<Copy>>"))   #Handles the copy event

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("TEXTPAD", "TEXTPAD created by Sayan Dey")



if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("TEXTPAD")
    root.wm_iconbitmap("Logo_for_my_tkinter_textpad_Project.ico")
    root.geometry("800x500")

    #Code for adding text area
    textArea=Text(root, font="lucida 13")
    file=None
    textArea.pack(expand=True, fill=BOTH)

    #Code for menu bar
    menubar=Menu(root)
    filemenu=Menu(menubar)

    #to open new file for the TEXTPAD
    filemenu.add_command(label="New", command=newFile)

    #To open a file which is already there in the computer
    filemenu.add_command(label="Open", command=openFile)

    #To save the current file
    filemenu.add_command(label="Save", command=saveFile)
    #filemenu.add_separator()
    menubar.add_cascade(label="File", menu=filemenu)

    #File menu ends


    #Edit manu
    editmenu=Menu(menubar)  #Edit menu is for cut, copy and paste command
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)

    menubar.add_cascade(label="Edit", menu=editmenu)

    #Edit menu ends

    #Help menu begins here
    helpmenu=Menu(menubar)
    helpmenu.add_command(label="About us", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)


    root.config(menu=menubar)    

    #Code for adding scrollbar in TEXTPAD
    scrollbar=Scrollbar(textArea)   #Creating a scrollbar in the textbar widget
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbar.set)


    root.mainloop()






