from tkinter import *  #Import everything in Tkinter

root = Tk() #Root widget. First thing you should always do
root.config(bg="#032f42")

root.title("Simple Calculator")

def button_click(number): #Inserts number in Display Box
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number))
	return

def button_clear(): #Clears Display Box
	e.delete(0,END)	

def button_add(): #Takes the first number as an input for Addition
	firstnumber=e.get()
	global f_num
	global math
	math = "+"
	f_num = int(firstnumber)
	e.insert("end", " + ")
	#e.delete(0,END)

def button_subtract(): #Takes the first number as an input for Subtraction
	firstnumber=e.get()
	global f_num
	global math
	math = "-"
	f_num = int(firstnumber)
	e.insert("end", " - ")
	
def button_multiply(): #Takes the first number as an input for Multiplication
	firstnumber=e.get()
	global f_num
	global math
	math = "X"
	f_num = int(firstnumber)
	e.insert("end", " X ")

def button_divide(): #Takes the first number as an input for Division
	firstnumber=e.get()
	global f_num
	global math
	math = "/"
	f_num = int(firstnumber)
	e.insert("end", " / ")
	
def button_equal(): #Computes Result
	secondnumber = e.get()
	e.delete(0,END)
	
	if math == "+": 
		second = secondnumber.split('+')
		e.insert(0,f_num+int(second[1]))
	elif math== "-": 
		second = secondnumber.split('-')
		e.insert(0,f_num-int(second[1]))	
	elif math== "X": 
		second = secondnumber.split('X')
		e.insert(0,f_num*int(second[1]))	
	elif math== "/": 
		second = secondnumber.split('/')
		e.insert(0,f_num/int(second[1]))	

#Display Box
e=Entry(root,width=43,borderwidth=5,justify="right")
e.config(font=("Courier", 16,'bold'),fg= "#ffffff",bg="#032f42")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10,ipady=20)

#Buttons for numbers
button_1 = Button(root,text="1",padx=81,pady=20,command=lambda :button_click(1))
button_1.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_2 = Button(root,text="2",padx=81,pady=20,command=lambda :button_click(2))
button_2.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_3 = Button(root,text="3",padx=81,pady=20,command=lambda :button_click(3))
button_3.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_4 = Button(root,text="4",padx=81,pady=20,command=lambda :button_click(4))
button_4.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_5 = Button(root,text="5",padx=81,pady=20,command=lambda :button_click(5))
button_5.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_6 = Button(root,text="6",padx=81,pady=20,command=lambda :button_click(6))
button_6.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_7 = Button(root,text="7",padx=81,pady=20,command=lambda :button_click(7))
button_7.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_8 = Button(root,text="8",padx=81,pady=20,command=lambda :button_click(8))
button_8.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_9 = Button(root,text="9",padx=81,pady=20,command=lambda :button_click(9))
button_9.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")
button_0 = Button(root,text="0",padx=81,pady=20,command=lambda :button_click(0))
button_0.config(font=("Courier", 16,'bold'),bg="#085171",fg="white")

#Buttons for Operations
button_add = Button(root,text="+",padx=81,pady=20,command=button_add)
button_add.config(font=("Courier", 18,'bold'),fg="#085171")
button_equal = Button(root,text="=",padx=179,pady=20,command=button_equal)
button_equal.config(font=("Courier", 16,'bold'),bg="#032f42",fg="white")
button_clear = Button(root,text="Clear",padx=153,pady=20,command=button_clear)
button_clear.config(font=("Courier", 16,'bold'),bg="#032f42",fg="white")

button_subtract = Button(root,text="-",padx=81,pady=20,command=button_subtract)
button_subtract.config(font=("Courier", 18,'bold'),fg="#085171")
button_multiply = Button(root,text="X",padx=81,pady=20,command=button_multiply)
button_multiply.config(font=("Courier", 18,'bold'),fg="#085171")
button_divide = Button(root,text="/",padx=81,pady=20,command=button_divide)
button_divide.config(font=("Courier", 18,'bold'),fg="#085171")
#Put buttons on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()