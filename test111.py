import tkinter as tk
window=tk.Tk()
window.title("number pad")
window.geometry("400x300")
f1=tk.Frame(master=window,width=200,height=250)
f1.place(x=100,y=40)

btn=tk.Button(master=f1,text="0",fg="red")
btn.place(x=0,y=0)

btn1=tk.Button(master=f1,text="1",fg="red")
btn1.place(x=60,y=0)

btn2=tk.Button(master=f1,text="2",fg="red")
btn2.place(x=120,y=0)

btn3=tk.Button(master=f1,text="3",fg="red")
btn3.place(x=0,y=50)

btn4=tk.Button(master=f1,text="4",fg="red")
btn4.place(x=60,y=50)

btn5=tk.Button(master=f1,text="5",fg="red")
btn5.place(x=120,y=50)

btn6=tk.Button(master=f1,text="6",fg="red")
btn6.place(x=0,y=100)

btn7=tk.Button(master=f1,text="7",fg="red")
btn7.place(x=60,y=100)

btn8=tk.Button(master=f1,text="8",fg="red")
btn8.place(x=120,y=100)

btn9=tk.Button(master=f1,text="9",fg="red")
btn9.place(x=0,y=150)


window.mainloop()
