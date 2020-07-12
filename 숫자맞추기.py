from tkinter import *
from tkinter import messagebox
import random as rd
count=0
number=0
trynumber=""
#게임 결과
def close(text):
    global number
    messagebox.showinfo("결과","{0}  정답 : {1}\n".format(text,number))
#입력값에 따른 결과
def select(value): 
    global count
    global number
    global trynumber
    count+=1
    if (str(number)==value):
        close("정답입니다.")
        
    else:
        tryfalse=Label(gui,text="COUNT:{0} 시도:{1}\n".format(count,value))
        tryfalse.grid(row=count+1,column=1)
        if (count ==10):
            close("10번의 시도를 모두 사용하셨습니다. ")
            count=1
            
        trynumber=""

#게임 시작 및 다시하기
def start():
    global number
    global trynumber
    global count
    #1~100중에 랜덤으로 숫자 선택
    equation.set("")
    number=rd.randint(1,100)
    trynumber=""
    count=0
    button = Button(gui, text=' 다시하기 ', fg='white', bg='black', 
                     command=lambda: start(), height=2, width=9) 
    button.grid(row=1,column=0)
    for i in range(1,11):
        tryfalse=Label(gui,text="COUNT:{0} 시도:{1}\n".format(i,"00"))
        tryfalse.grid(row=i+1,column=1)
        
#키보드 입력 숫자
#backspace로 숫자 하나씩 지우기
#엔터로 입력값 보내기
#숫자는 1~100까지만 입력가능 
def key_input(value):
    global trynumber
    numbers='1234567890'
    if value.char in numbers :
            trynumber+=value.char
    elif value.keysym == "Return":
        if trynumber=="" or int(trynumber)>100:
            trynumber=""
            pass
        else:
            select(trynumber)
        equation.set("")
    elif value.keysym == "BackSpace":
        trynumber=trynumber[:-1]


if __name__ == "__main__":
    gui = Tk()

    gui.title("숫자 맞추기")

    gui.geometry("350x410")
    
    gui.bind('<Key>',key_input)

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation) 
  
    expression_field.grid(row=0,column=0, ipadx=30) 
    equation.set('시작 버튼을 누르시오')

    button1 = Button(gui, text=' 시작 ', fg='white', bg='black', 
                     command=lambda: start(), height=2, width=9) 
    button1.grid(row=1,column=0)

    trycount= Label(gui,text="도전 결과",fg="black")
    trycount.grid(row=1,column=1)
    for i in range(1,11):
        tryfalse=Label(gui,text="COUNT:{0} 시도:{1}\n".format(i,"00"))
        tryfalse.grid(row=i+1,column=1)


    gui.mainloop()