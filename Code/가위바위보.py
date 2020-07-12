from tkinter import *
from tkinter import messagebox
import random as rd
comwin=0
userwin=0
gamecountrow=2
# user나 com 이 3번이기면 메시지창과 함께 종료
def close(winner):
    messagebox.showinfo("Winner","승리자 : {0}\n".format(winner))
    gui.destroy()

# 1 : 바위 2 : 보자기 3 : 가위 
#버튼 밑에 결과 출력 및 오른쪽에 전체 결과 출력
def Rock():
    global comwin
    global userwin
    global gamecountrow
    com = rd.randint(1,3)
    if com ==1:
        result=Label(gui,text="USER 무",fg="black")
        result2=Label(gui,text="USER 무",fg="black")
    elif com ==2:
        result=Label(gui,text="USER 패",fg="blue")
        result2=Label(gui,text="USER 패",fg="blue")
        comwin+=1
    elif com ==3:
        result=Label(gui,text="USER 승",fg="red")
        result2=Label(gui,text="USER 승",fg="red")
        userwin+=1

    result2.grid(row=3,column=1)
    result.grid(row=gamecountrow,column=4)
    gamecountrow+=1
    if comwin ==3:
        close("COMPUTER")
    elif userwin ==3:
        close("USER")
def Paper():
    global comwin
    global userwin
    global gamecountrow
    com = rd.randint(1,3)
    if com ==2:
        result=Label(gui,text="USER 무",fg="black")
        result2=Label(gui,text="USER 무",fg="black")
    elif com ==3:
        result=Label(gui,text="USER 패",fg="blue")
        result2=Label(gui,text="USER 패",fg="blue")
        comwin+=1
    elif com ==1:
        result=Label(gui,text="USER 승",fg="red")
        result2=Label(gui,text="USER 승",fg="red")
        userwin+=1

    result2.grid(row=3,column=1)
    result.grid(row=gamecountrow,column=4)
    gamecountrow+=1
    if comwin ==3:
        close("COMPUTER")
    elif userwin ==3:
        close("USER")

def Sciccors():
    global comwin
    global userwin
    global gamecountrow
    com = rd.randint(1,3)
    if com ==3:
        result=Label(gui,text="USER 무",fg="black")
        result2=Label(gui,text="USER 무",fg="black")
    elif com ==1:
        result=Label(gui,text="USER 패",fg="blue")
        result2=Label(gui,text="USER 패",fg="blue")
        comwin+=1
    elif com ==2:
        result=Label(gui,text="USER 승",fg="red")
        result2=Label(gui,text="USER 승",fg="red")
        userwin+=1

    result2.grid(row=3,column=1)
    result.grid(row=gamecountrow,column=4)
    gamecountrow+=1

    if comwin ==3:
        close("COMPUTER")
    elif userwin ==3:
        close("USER")


if __name__ == "__main__": 
    gui = Tk()

    gui.title("가위바위보")

    gui.geometry("300x300")
    

    button1 = Button(gui, text=' 가위 ', fg='white', bg='black', 
                     command=lambda: Sciccors(), height=2, width=9) 
    button1.grid(row=1, column=0)

    button2 = Button(gui, text=' 바위 ', fg='white', bg='black', 
                     command=lambda: Rock(), height=2, width=9) 
    button2.grid(row=1, column=1)

    button3 = Button(gui, text=' 보 ', fg='white', bg='black', 
                     command=lambda: Paper(), height=2, width=9) 
    button3.grid(row=1, column=2)


    gui.mainloop()