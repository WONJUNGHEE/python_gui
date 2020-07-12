from tkinter import *
  
expression = "" 
#메모리 저장하는 배열
memory=[]
#off 누르면 계산기 종료
def off():
    gui.destroy()
#M+ 누르면 배열에 + 값으면 저장
def memoryplus():
    global expression
    total1 = "+"+str(eval(expression))
    memory.append(total1)
    equation.set("")
    expression=""
#M- 누르면 배열에 -값으로 저장
def memoryminus():
    global expression
    total2 = "-"+str(eval(expression))
    memory.append(total2)
    equation.set("")
    expression=""
#메모리 초기화
def memoryclear():
    memory.clear()
    equation.set(memory)
    expression=""
#메모리 값들 계산
def memoryread():
    global expression
    sum=str(eval(''.join(memory)))
    equation.set(sum)
    expression=sum
    
#값 입력
def press(num): 
   
    global expression 
  
    expression = expression + str(num) 
  
    equation.set(expression) 
#expression 값들 계산 출력
def equalpress(): 

    try: 
  
        global expression 
  
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        expression = total 
  
    except: 
  
        equation.set(" error ") 
        expression = "" 
#expression 값 퍼센트로 계산
def percent():
    global expression
    percent = str(float(expression)/100)
    equation.set(percent)
    expression=percent
#expression 값 루트로 계산
def root():
    global expression
    percent = str(float(expression)**0.5)
    equation.set(percent)
    expression=percent
  
#expression 초기화
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
#on 및 0으로 초기화
def on(): 
    global expression 
    expression = "" 
    equation.set("0")
  
  
if __name__ == "__main__": 
  
    gui = Tk() 
  #배경 색 하얀색
    gui.configure(background="white") 
  #제목
    gui.title("Simple Calculator") 
  #프로그램 크기
    gui.geometry("360x170") 
  #결과 값 
    equation = StringVar() 
  
    expression_field = Entry(gui, textvariable=equation) 
  
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('숫자를 입력하시오.') 
  # 버튼 생성 및 버튼 눌렀을 시 함수 실행
  #grid 를 이용해 버튼 위치 정하기
    button1 = Button(gui, text=' MC ', fg='black', bg='green', 
                     command=lambda: memoryclear(), height=1, width=7) 
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text=' MR ', fg='black', bg='green', 
                     command=lambda: memoryread(), height=1, width=7) 
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' M- ', fg='black', bg='green', 
                     command=lambda: memoryminus(), height=1, width=7) 
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' M+ ', fg='black', bg='green', 
                     command=lambda: memoryplus(), height=1, width=7) 
    button4.grid(row=2, column=3)

    button5 = Button(gui, text=' % ', fg='black', bg='green', 
                     command=lambda: percent(), height=1, width=7) 
    button5.grid(row=2, column=4)

    button6 = Button(gui, text=' √  ', fg='black', bg='green', 
                     command=lambda: root(), height=1, width=7) 
    button6.grid(row=3, column=0)

    button7 = Button(gui, text=' 7 ', fg='black', bg='green', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=3, column=1)

    button8 = Button(gui, text=' 8 ', fg='black', bg='green', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=3, column=2)

    button9 = Button(gui, text=' 9 ', fg='black', bg='green', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=3, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='green', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=3, column=4) 

    button11 = Button(gui, text=' OFF ', fg='black', bg='green', 
                     command=lambda: off(), height=1, width=7) 
    button11.grid(row=4, column=0)

    button12 = Button(gui, text=' 4 ', fg='black', bg='green', 
                     command=lambda: press(4), height=1, width=7) 
    button12.grid(row=4, column=1)

    button13 = Button(gui, text=' 5 ', fg='black', bg='green', 
                     command=lambda: press(5), height=1, width=7) 
    button13.grid(row=4, column=2)

    button14 = Button(gui, text=' 6 ', fg='black', bg='green', 
                     command=lambda: press(6), height=1, width=7) 
    button14.grid(row=4, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='green', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=4) 

    clear = Button(gui, text='CE', fg='black', bg='green', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column=0) 

    button17 = Button(gui, text=' 1 ', fg='black', bg='green', 
                     command=lambda: press(1), height=1, width=7) 
    button17.grid(row=5, column=1)

    button18 = Button(gui, text=' 2 ', fg='black', bg='green', 
                     command=lambda: press(2), height=1, width=7) 
    button18.grid(row=5, column=2)

    button19 = Button(gui, text=' 3 ', fg='black', bg='green', 
                     command=lambda: press(3), height=1, width=7) 
    button19.grid(row=5, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='green', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=5, column=4) 

    button21 = Button(gui, text=' ON/C ', fg='black', bg='green', 
                     command=lambda: on(), height=1, width=7) 
    button21.grid(row=6, column=0)

    button22 = Button(gui, text=' 0 ', fg='black', bg='green', 
                     command=lambda: press(1), height=1, width=7) 
    button22.grid(row=6, column=1)

    Decimal= Button(gui, text='.', fg='black', bg='green', 
                    command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=2) 

    equal = Button(gui, text=' = ', fg='black', bg='green', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=6, column=3)

    plus = Button(gui, text=' + ', fg='black', bg='green', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=6, column=4)   

    gui.mainloop() 