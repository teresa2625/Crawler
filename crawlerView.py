from tkinter import *
import math


class MainScreen(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.root = root
        self.controller = controller
        self.category_name = self.controller.getSpecialCategory()

        self.option_frame = Frame(self.root)
        self.option_frame.pack(side=TOP, fill=X)

        option_list = ["Please chose the category you would like to view "]
        for category in self.category_name:
            option_list.append(category)
        self.variable = StringVar(self)
        self.variable.set(option_list[0])

        opt = OptionMenu(self.option_frame, self.variable, *option_list)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack()
        self.variable.trace("w", self.callback)

        self.table_frame = Listbox(self.root)
        self.table_frame.pack(side=TOP, fill=BOTH)

    def CreateTable(self):
        self.table_frame = Listbox(self.root)
        self.table_frame.pack(side=TOP, fill=BOTH)

        if self.product_info != None:
            # adding table
            table_heading = ["Product Name", "Special Price"]
            if len(self.product_info[0]) > 25:
                for i in range(1, math.ceil(len(self.product_info[0]) / 25)):
                    table_heading += table_heading

            for column in range(len(table_heading)):
                new_row = 1
                for row in range(len(self.product_info[0])):
                    if row == 0:
                        label = Label(self.table_frame, text=table_heading[column], bg="#E0E0E0", fg="black", padx=3,
                                      pady=3)
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        self.table_frame.grid_columnconfigure(column, weight=1)
                    elif row < 25:
                        label = Label(self.table_frame, text=self.product_info[0][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=row, column=0, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        label = Label(self.table_frame, text=self.product_info[1][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=row, column=1, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                    elif 25 <= row < (25 * 2):
                        label = Label(self.table_frame, text=self.product_info[0][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=2, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        label = Label(self.table_frame, text=self.product_info[1][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=3, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        new_row += 1
                    elif (25 * 2) <= row < (25 * 3):
                        label = Label(self.table_frame, text=self.product_info[0][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=4, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        label = Label(self.table_frame, text=self.product_info[1][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=5, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        new_row += 1
                    elif (25 * 3) <= row < (25 * 4):
                        label = Label(self.table_frame, text=self.product_info[0][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=6, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        label = Label(self.table_frame, text=self.product_info[1][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=7, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        new_row += 1
                    elif (25 * 4) <= row < (25 * 5):
                        label = Label(self.table_frame, text=self.product_info[0][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=8, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        label = Label(self.table_frame, text=self.product_info[1][row - 1], bg="#F0F0F0", fg="black")
                        label.grid(row=new_row, column=9, sticky="nsew", padx=1, pady=1)
                        label.grid_columnconfigure(column, weight=1)
                        new_row += 1
                    else:
                        break

    def callback(self, *args):
        self.table_frame.destroy()

        if self.variable.get() == "Half Price":
            pass
            # self.product_info = self.controller.getHalfPrice()
        elif self.variable.get() == "Meats":
            pass
            # self.product_info = self.controller.getMSDSpecial()
        else:
            self.product_info = self.controller.getVegAndFruitsSpecial()

        self.CreateTable()
