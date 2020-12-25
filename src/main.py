from tkinter import *
from calculator import User_Interface


if __name__ == "__main__":
    root = Tk()

    calculator = User_Interface(root)

    root.title("Calculator")

    root.mainloop()