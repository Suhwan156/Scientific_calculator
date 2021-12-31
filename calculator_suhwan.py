import tkinter
from tkinter import *
import tkinter.font as tkFont
from math import *

class suhwan_calculator:
    def __init__(self):
        window = Tk()
        window.title('공학용 계산기_수환')          # 타이틀 지정
        window.configure(background="black")            # 배경 색 검정

        self.string = StringVar()           # 계산기 창 대상, 키보드 입력 이용 가능 / 단 =는 눌러도 결과X(구현을 못했습니다 ㅠ)
        display = Entry(window, textvariable=self.string, justify='right')
        display.grid(row=0, column=0, columnspan=7, ipadx=188, ipady=15)
        display.config(font=("Arial", 20), background="black", fg="white")
        display.focus_set()

        self.string2 = StringVar()          # 하단 메모기능 추가를 위해 row8에 입력 가능 칸 배치
        notepad = Entry(window, textvariable=self.string2, justify='right')
        notepad.grid(row=8, column=0, columnspan=7, ipadx=188, ipady=15)
        notepad.config(font=("Arial", 20), background="white", fg="black")

        values = ["radians", "degrees", "*0.01", "(", ")", "cleanAC", "AC",             # 계산기 값 배치
                  "factorial", "pi", "e", "7", "8", "9", "/",
                  "sin", "cos", "tan", "4", "5", "6", "*",
                  "log", "log1p", "log2", "1", "2", "3", "-",
                  "gamma", "**(1/2)", "**2", "0", ".", "=", "+"
                  ]
        mage = tkinter.PhotoImage(file="ac2.png")           # 추가기능, 버튼에 AC 이미지 입힘
        number_font = tkFont.Font(family="Arial", size=14, weight="bold")
        text_font = tkFont.Font(family="Arial", size=14, weight="bold")
        i = 0
        row = 1        # 줄
        col = 0        # 칸
        for txt in values:          # 버튼 7칸별로 줄 배열 반복문 활용
            padx = 20
            pady = 20
            if (i == 7):
                row = 2
                col = 0
            if (i == 14):
                row = 3
                col = 0
            if (i == 21):
                row = 4
                col = 0
            if (i == 28):
                row = 5
                col = 0
            if (i == 35):
                row = 6
                col = 0
            if (txt == '='):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.equal())
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="dodgerblue", font=text_font)
            elif (txt == 'cleanAC'):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text="←",
                             command=lambda txt=txt: self.delete())
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", fg="black", font=text_font)
            elif (txt == 'AC'):
                button = Button(window, padx=padx, pady=pady, image=mage,
                             command=lambda txt=txt: self.cleanAC())
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", font=text_font)
            elif (txt == 'factorial'):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text="!",
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", fg="white", font=text_font)
            elif (txt == '**2'):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text="제곱",
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", fg="white", font=text_font)
            elif (txt == '**(1/2)'):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text="√",
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", fg="white", font=text_font)
            elif (txt == '*0.01'):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text='%',
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", fg="white", font=text_font)
            elif (txt.isdigit() == True):
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="black", fg="white", font=number_font)
            else:
                button = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addcharacter(txt))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.configure(background="grey", font=text_font, fg='white')

            col = col + 1
            i = i + 1

        window.mainloop()

    def cleanAC(self):
        self.string.set("")

    def equal(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "값 오류. 함수의 경우 함수(숫자). 다시 하려면 AC 클릭"
        self.string.set(result)

    def addcharacter(self, char):
        self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

suhwan_calculator()