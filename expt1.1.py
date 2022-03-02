from tkinter import * 
from tkinter import messagebox
from functools import partial  
import pyshorteners
import re
from selenium import webdriver
import time

root=Tk()

myLabel=Label(root,text="Select the function",bg='#EEEEEE',fg='#555555',font=('Times New Roman',25,UNDERLINE))
root.geometry('500x500')
root.configure(background='coral')
root.title('python mini project')

def my2():

    def evaluate(event):
        
        password =str(enteryy2.get())
        flag = 0
        while True:  
            if (len(password)<8):
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                r=("Strong Password!")
                break
        
        if flag ==-1:
            r=("Weak Password!")
        res.configure(text = "Result: " + r,font='Helvetica 11 bold')   
    
    nw2=Toplevel(root)
    nw2.geometry('250x250')
    nw2.title('password strength')
    lbl2=Label(nw2,text='Enter password',font=('Times New Roman',18,UNDERLINE))
    lbl2.pack()    
    enteryy2=Entry(nw2)
    enteryy2.pack()
    enteryy2.bind("<Return>",evaluate)

    nw2.configure(background='cyan')

    res =Label(nw2)
    res.pack()
    exitbuton=Button(nw2,text='exit',bg='magenta',command=nw2.destroy)
    exitbuton.pack()

    

def my3():
    def evaluate1(event):
        
        
        url1=enteryy3.get()
            
        driver=webdriver.Chrome (executable_path="C:/Users/aryan/Downloads/chromedriver.exe")

        driver.get(url1)

        refreshrate=int(30)

        while True:
            time.sleep(refreshrate)
            driver.refresh()
            
        
          
    
    nw3=Toplevel(root)
    nw3.title('Increase views on url')
    nw3.geometry('250x250')
    lbl3=Label(nw3,text='Enter URL',font=('Times New Roman',18,UNDERLINE))
    lbl3.pack()
    enteryy3=Entry(nw3)
    enteryy3.pack()
    enteryy3.bind("<Return>",evaluate1)

    nw3.configure(background='beige')
    res =Label(nw3)
    res.pack()
    exitbuton=Button(nw3,text='exit',bg='magenta',command=nw3.destroy)
    exitbuton.pack()

def my4():
    def evaluate2(event):
        url=str(enteryy4.get())
        s = pyshorteners.Shortener()
        d=s.tinyurl.short(url)
        res.configure(text = "Result: " + d,font='Helvetica 11 bold')     
    
    nw4=Toplevel(root)
    nw4.title('Shorten URL')
    nw4.geometry('500x500')
    lbl4=Label(nw4,text='Enter URL',font=('Times New Roman',18,UNDERLINE)) 
    lbl4.pack()
    enteryy4=Entry(nw4)
    enteryy4.pack(padx=10,
               pady=10,
               ipadx=100,
               ipady=10)
    enteryy4.bind("<Return>",evaluate2)

    nw4.configure(background='DeepPink')
    res =Label(nw4)
    res.pack()
    exitbuton=Button(nw4,text='exit',bg='magenta',command=nw4.destroy)
    exitbuton.pack()

myLabel.pack()

myButton2=Button(root,text='Password strength',bg='cyan',padx=57,pady=20, command=my2)
myButton2.pack()

myButton4=Button(root,text='Shorten URL',bg='cyan',padx=73,pady=20,command=my4)
myButton4.pack()

myButton3=Button(root,text='Increase views on url',bg='cyan',padx=50,pady=20,command=my3)
myButton3.pack()

exitbutton=Button(root,text='exit',bg='magenta',command=root.destroy).pack()
root.mainloop()
