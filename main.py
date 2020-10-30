# Main.py
#
# Author - Euan Hall
# Date - 30-OCT-2020
import tkinter as tk
import re


class Calculator:
    def __init__(self):
        # Command
        self.command = ""

        # Init root
        self.root = tk.Tk()

        # Init GUI
        self.display = tk.Label(self.root, text="---", bd=2, relief="sunken")
        self.display.pack()

        # Init Numbers
        self.number_bttns = tk.Frame(self.root)
        self.one = tk.Button(self.number_bttns, text="1", command=lambda: self.add_char("1"))
        self.two = tk.Button(self.number_bttns, text="2", command=lambda: self.add_char("2"))
        self.three = tk.Button(self.number_bttns, text="3", command=lambda: self.add_char("3"))
        self.four = tk.Button(self.number_bttns, text="4", command=lambda: self.add_char("4"))
        self.five = tk.Button(self.number_bttns, text="5", command=lambda: self.add_char("5"))
        self.six = tk.Button(self.number_bttns, text="6", command=lambda: self.add_char("6"))
        self.seven = tk.Button(self.number_bttns, text="7", command=lambda: self.add_char("7"))
        self.eight = tk.Button(self.number_bttns, text="8", command=lambda: self.add_char("8"))
        self.nine = tk.Button(self.number_bttns, text="9", command=lambda: self.add_char("9"))
        self.zero = tk.Button(self.number_bttns, text="0", command=lambda: self.add_char("0"))

        # Init functions
        self.add_bttn = tk.Button(self.number_bttns, text="+", command=lambda: self.add_char("+"))
        self.sub_bttn = tk.Button(self.number_bttns, text="-", command=lambda: self.add_char("-"))
        self.mul_bttn = tk.Button(self.number_bttns, text="*", command=lambda: self.add_char("*"))
        self.div_bttn = tk.Button(self.number_bttns, text="/", command=lambda: self.add_char("/"))
        self.eq_bttn = tk.Button(self.number_bttns, text="=", command=self.equal)
        self.clr_bttn = tk.Button(self.number_bttns, text="cl", command=self.clear)

        # Number grid
        self.seven.grid(column=0, row=0)
        self.eight.grid(column=1, row=0)
        self.nine.grid(column=2, row=0)
        self.add_bttn.grid(column=3, row=0)
        self.four.grid(column=0, row=1)
        self.five.grid(column=1, row=1)
        self.six.grid(column=2, row=1)
        self.sub_bttn.grid(column=3, row=1)
        self.one.grid(column=0, row=2)
        self.two.grid(column=1, row=2)
        self.three.grid(column=2, row=2)
        self.mul_bttn.grid(column=3, row=2)
        self.zero.grid(column=0, row=3)
        self.div_bttn.grid(column=1, row=3)
        self.eq_bttn.grid(column=2, row=3)
        self.clr_bttn.grid(column=3, row=3)
        self.number_bttns.pack()

    def add_char(self, char):
        self.command = self.command + char
        self.update_display()

    def equal(self):
        if self.command == "":
            self.display["text"] = "0"
        else:
            symbols = re.split(r"[0-9]+", self.command)  # Finds all symbols
            symbols = list(filter(None, symbols))  # Removes all blank items
            numbers = re.split(r"[+-/*]+", self.command)  # Finds all numbers
            print(numbers)
            print(symbols)
            answer = int(numbers[0])  # Sets answer to the first number
            for symbol in symbols:
                x = 1
                if symbol == "+":
                    answer += int(numbers[x])
                elif symbol == "-":
                    answer -= int(numbers[x])
                elif symbol == "/":
                    answer /= int(numbers[x])
                elif symbol == "*":
                    answer *= int(numbers[x])
                x+= 1
            self.command = str(answer)
            self.update_display()

    def clear(self):
        self.command = ""
        self.update_display()

    def update_display(self):
        self.display["text"] = self.command


c = Calculator()
c.root.mainloop()
