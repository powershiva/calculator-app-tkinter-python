# calculator-app-tkinter-python
#CALCULATOR APP
import  tkinter
from tkinter import *
import ast
root=tkinter.Tk()
#root.geometry("250x300")
root.title("CALCULATOR")
i=0
def get_number(num):
     global i
     entry.insert(i,num)
     i+=1
def get_operators(operators) :
        
    global i 
    length=len(operators)
    entry.insert(i,operators)
    i+=length
def clear_all():
     
     entry.delete(0,END)    
def calculate():
    entire_string=entry.get()
    try:
        node=ast.parse(entire_string,mode="eval")
        result=eval(compile(node,"<string>","eval"))
        clear_all()
        entry.insert(0,result)
    except Exception:
         clear_all()
         entry.insert(0,"error")    
def undo():
     entire_string=entry.get()
     if len(entire_string):
          new_string=entire_string[:-1]   
          clear_all()
          entry.insert(0,new_string)
     else:
          clear_all()
          entry.insert(0,"")     



#creating a enter 
entry=Entry(root)
entry.grid(row=0,columnspan=6)
numbers=[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):

        button_text=numbers[counter]
        button=Button(root,text=button_text,width=2,height=2,command=lambda text=button_text:get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1
        button_0=Button(root,text="0",width=2,height=2,command=lambda :get_number(0))
        button_0.grid(row=5,column=1)

        count=0
        operators=["+","-","/","%","(","*",")","*33.14","**2"]
for x in range(4):
    for y in range(3):
            if count<len(operators):
                button=Button(root,text=operators[count],width=2,height=2,command=lambda text=operators[count]:get_operators(text))
                count+=1
                button.grid(row=x+2,column=y+3)
                button=Button(root,text="AC",width=2,height=2,command=clear_all)
                button.grid(row=5,column=0)
                button=Button(root,text="=",width=2,height=2,command=calculate)
                button.grid(row=5,column=2)
                button=Button(root,text="<-",width=2,height=2,command=lambda:undo()).grid(row=5,column=4)
                root.update_idletasks()
                root.minsize(root.winfo_width(),root.winfo_height())


            

root.mainloop()
