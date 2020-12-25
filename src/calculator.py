from tkinter import *

class User_Interface:

    def __init__(self, main):

        frame = Frame(main)
        frame.pack()

        self.large_font =('Arial', 24)

        self.ent = Entry(frame, width = 22, borderwidth = 5, font = self.large_font, justify = "right")
        self.ent.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10, ipady = 10)

        # digit buttons
        self.decimal = Button(frame, text = ".", padx = 41, pady = 20, command = lambda: self.buttonadd('.'))
        self.zero = Button(frame, text = "0", padx = 96, pady = 20, command = lambda: self.buttonadd(0))
        self.one = Button(frame, text = "1", padx = 40, pady = 20, command = lambda: self.buttonadd(1))
        self.two = Button(frame, text = "2", padx = 40, pady = 20, command = lambda: self.buttonadd(2))    
        self.three = Button(frame, text = "3", padx = 40, pady = 20, command = lambda: self.buttonadd(3))
        self.four = Button(frame, text = "4", padx = 40, pady = 20, command = lambda: self.buttonadd(4))
        self.five = Button(frame, text = "5", padx = 40, pady = 20, command = lambda: self.buttonadd(5))    
        self.six = Button(frame, text = "6", padx = 40, pady = 20, command = lambda: self.buttonadd(6))
        self.seven = Button(frame, text = "7", padx = 40, pady = 20, command = lambda: self.buttonadd(7))
        self.eight = Button(frame, text = "8", padx = 40, pady = 20, command = lambda: self.buttonadd(8))    
        self.nine = Button(frame, text = "9", padx = 40, pady = 20, command = lambda: self.buttonadd(9))

        # mapping the digit buttons
        self.decimal.grid(row = 4, column = 2, pady = 5)
        self.zero.grid(row = 4, column = 0, columnspan = 2, pady = 5)
        self.one.grid(row = 3, column = 0, pady = 5)
        self.two.grid(row = 3, column = 1, pady = 5)
        self.three.grid(row = 3, column = 2, pady = 5)
        self.four.grid(row = 2, column = 0, pady = 5)
        self.five.grid(row = 2, column = 1, pady = 5)
        self.six.grid(row = 2, column = 2, pady = 5)
        self.seven.grid(row = 1, column = 0, pady = 5)
        self.eight.grid(row = 1, column = 1, pady = 5)
        self.nine.grid(row = 1, column = 2, pady = 5)

        # function buttons
        self.add = Button(frame, text = "+", padx = 39, pady = 20, command = self.addition)
        self.equal = Button(frame, text = "=", padx = 90, pady = 20, command = self.equal)
        self.clear = Button(frame, text = "Clear", padx =85, pady = 20, command =self.clear)
        self.subtract = Button(frame, text="-", padx=39, pady=20, command=self.subtraction)
        self.multiply = Button(frame, text="*", padx=40, pady=20, command=self.multiplication)
        self.divide = Button(frame, text="/", padx=41, pady=20, command=self.division)

        # mapping the function buttons
        self.add.grid(row = 4, column = 3, pady = 5)
        self.equal.grid(row = 5, column = 2, columnspan = 2, pady = 5, padx = 10)
        self.clear.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 10)
        self.subtract.grid(row = 3, column = 3, pady = 5)
        self.multiply.grid(row = 2, column = 3, pady = 5)
        self.divide.grid(row = 1, column = 3, pady = 5)

    def clear(self):
        self.ent.delete(0, END)

    def buttonadd(self, number):
        #self.ent.delete(0, END)
        current = self.ent.get()
        self.ent.delete(0, END)
        self.ent.insert(0, str(current) + str(number))

    def addition(self):
        firstnumber = self.ent.get()
        global f_num
        global math
        math = "addition"
        f_num = float(firstnumber)
        self.ent.delete(0, END)

    def subtraction(self):
        firstnumber = self.ent.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(firstnumber)
        self.ent.delete(0, END)

    def multiplication(self):
        firstnumber = self.ent.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(firstnumber)
        self.ent.delete(0, END)

    def division(self):
        firstnumber = self.ent.get()
        global f_num
        global math
        math = "division"
        f_num = float(firstnumber)
        self.ent.delete(0, END)

    def equal(self):
        secondnumber = self.ent.get()
        self.ent.delete(0, END)

        if math == "addition":
            self.ent.insert(0, f_num + float(secondnumber))

        if math == "subtraction":
            self.ent.insert(0, f_num - float(secondnumber))

        if math == "multiplication":
            self.ent.insert(0, f_num * float(secondnumber))

        if math == "division":
            self.ent.insert(0, f_num / float(secondnumber))

if __name__ == "__main__":
    root = Tk()

    calculator = User_Interface(root)

    root.title("Calculator")

    root.mainloop()
