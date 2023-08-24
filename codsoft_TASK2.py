from tkinter import*
from tkinter import ttk
r=Tk()
r.geometry("500x600")
r.title("SIMPLE CALCULATOR")
r.configure(bg="black")
r.resizable(0,0)
equation=" "


def show(value):
        global equation
        equation+=value
        label_result.configure(text=equation)

#defining clear function to delete the given equation 
def clear():
        global equation
        equation=""
        label_result.configure(text=equation)

#defining calculate function to evaluate the given equation
def calculate():
        global equation
        result=eval(equation)
        label_result.configure(text=result)
     

label_result=Label(r,width=40,height=3,text=" ",bg="white",font=("Source Sans pro semibold",20))
label_result.pack()

btn1=Button(r,text="C",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:clear())
btn1.place_configure(x=5,y=120)

btn2=Button(r,text="/",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("/"))
btn2.place_configure(x=130,y=120)

btn3=Button(r,text="%",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("%"))
btn3.place_configure(x=255,y=120)

btn4=Button(r,text="*",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("*"))
btn4.place_configure(x=380,y=120)

btn5=Button(r,text="7",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("7"))
btn5.place_configure(x=5,y=200)

btn6=Button(r,text="8",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("8"))
btn6.place_configure(x=130,y=200)

btn7=Button(r,text="9",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("9"))
btn7.place_configure(x=255,y=200)

btn8=Button(r,text="-",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("-"))
btn8.place_configure(x=380,y=200)

btn9=Button(r,text="4",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("4"))
btn9.place_configure(x=5,y=280)

btn10=Button(r,text="5",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("5"))
btn10.place_configure(x=130,y=280)

btn11=Button(r,text="6",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("6"))
btn11.place_configure(x=255,y=280)

btn12=Button(r,text="+",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("+"))
btn12.place_configure(x=380,y=280)

btn13=Button(r,text="1",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("1"))
btn13.place_configure(x=5,y=360)

btn14=Button(r,text="2",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("2"))
btn14.place_configure(x=130,y=360)

btn15=Button(r,text="3",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("3"))
btn15.place_configure(x=255,y=360)

btn16=Button(r,text="0",width=21,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("0"))
btn16.place_configure(x=5,y=440)

btn17=Button(r,text=".",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("."))
btn17.place_configure(x=255,y=440)

btn18=Button(r,text="=",width=10,height=5,font=("Source Sans pro semibold",15,"bold"),bg="Orange",fg="Black",command=lambda:calculate())
btn18.place_configure(x=380,y=360)

btn19=Button(r,text="**",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("**"))
btn19.place_configure(x=5,y=520)

btn20=Button(r,text="//",width=10,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:show("//"))
btn20.place_configure(x=130,y=520)

btn21=Button(r,text="Exit",width=21,height=2,font=("Source Sans pro semibold",15,"bold"),bg="skyblue",fg="Black",command=lambda:exit())
btn21.place_configure(x=255,y=520)

r.mainloop()





