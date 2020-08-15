import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd

import datetime
import time

# login page or Acesss system

window = tk.Tk()
window.title("Access System")

window.geometry('790x520+0+0')
window.configure(background='black')

image = Image.open("image120.jpg")
photo1 = ImageTk.PhotoImage(image)
label_1 = Label(image=photo1)
label_1.pack()

# enter username  and password
un = tk.Label(window, text="Username", width=10, height=2, fg="black", bg="#2bd92b",
              font=('times', 10, ' bold '))

un.place(x=150, y=150)

pw = tk.Label(window, text="Password", width=10, height=2, fg="black", bg="#2bd92b",
              font=('times', 10, ' bold '))

pw.place(x=150, y=240)

un_entr1 = tk.Entry(window, width=20, bg="white", fg="red",
                    font=('times', 23, ' bold '))

un_entr1.place(x=270, y=150)

pw_entr2 = tk.Entry(window, width=20, show="*", bg="white", fg="red",
                    font=('times', 23, ' bold '))

pw_entr2.place(x=270, y=240)


def manually_fill():
    global sb

    sb = tk.Tk()

    sb.iconbitmap('AMS.ico')

    sb.title("Enter accesories name...")

    sb.geometry('580x320')

    sb.configure(background='snow')

    def err_screen_for_subject():

        def ec_delete():
            ec.destroy()

        global ec

        ec = tk.Tk()

        ec.geometry('300x100')

        ec.iconbitmap('AMS.ico')

        ec.title('Warning!!')

        ec.configure(background='snow')

        Label(ec, text='Please enter your subject name!!!', fg='red',
              bg='white', font=('times', 16, ' bold ')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="lawn green",
               width=9, height=1, activebackground="Red",
               font=('times', 15, ' bold ')).place(x=90, y=50)

    def fill():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')

        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        r = 0

        for col in fill:
            c = 0
            for row in col:
                # i've added some styling
                label = tk.Label(window, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                 bg="white", text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

        date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')

        global subb

        DB_table_name = str(subb + "" + Date + "_Time" + Hour + "" + Minute + "" + Second)

        import pymysql.connections

        try:
            global cursor
            connection = pymysql.connect(host='localhost', user='root', password='raja', db='manually_fill_')
            cursor = connection.cursor()
        except Exception as e:
            print(e)

        sql = "CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         ENROLLMENT varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """

        try:
            cursor.execute(sql)

        except Exception as ex:
            print(ex)  #

        if subb == '':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.iconbitmap('AMS.ico')

            MFW.title("Manually filled of " + str(subb))

            MFW.geometry('880x470')

            MFW.configure(background='snow')

            def del_errsc2():

                errsc2.destroy()

            def err_screen1():
                global errsc2

                errsc2 = tk.Tk()
                errsc2.geometry('330x100')

                errsc2.iconbitmap('AMS.ico')
                errsc2.title('Warning!!')
                errsc2.configure(background='snow')

                Label(errsc2, text='Please fill!!!', fg='red', bg='white',
                      font=('times', 16, ' bold ')).pack()
                Button(errsc2, text='OK',
                       command=del_errsc2, fg="black",
                       bg="lawn green", width=9, height=1,
                       activebackground="Red",
                       font=('times', 15, ' bold ')).place(x=90, y=50)

            def Attf():

                import subprocess
                subprocess.Popen(
                    r'explorer /select,"C:\Users\VIvek\Desktop\
                    PycharmProjects\managemnt system\Aex\"')

            attf = tk.Button(window, text="Check Sheets", fg="black",
                             bg="lawn green", width=12, height=1,
                             activebackground="Red",
                             font=('times', 14, ' bold '))

            attf.place(x=430, y=255)

            sub = tk.Label(window, text="Enter Subject", width=15,
                           height=2, fg="white",
                           bg="blue2",
                           font=('times', 15, ' bold '))
            sub.place(x=30, y=100)

            tx = tk.Entry(window, width=20, bg="yellow",
                          fg="red",
                          font=('times', 23, ' bold '))

            tx.place(x=250, y=105)

            fill_a = tk.Button(window, text="Fill Attendance",
                               fg="white", bg="deep pink",
                               width=20, height=2,
                               activebackground="Red",
                               font=('times', 15, ' bold '))
            fill_a.place(x=250, y=160)

            def testVal(inStr, acttyp):

                if acttyp == '1':  # insert

                    if not inStr.isdigit():
                        return False
                return True

            ENR = tk.Label(MFW, text="Enter price", width=15, height=2,
                           fg="white", bg="blue2",
                           font=('times', 15, ' bold '))
            ENR.place(x=30, y=100)

            STU_NAME = tk.Label(MFW, text="Enter accesories name",
                                width=15, height=2, fg="white", bg="blue2",
                                font=('times', 15, ' bold '))

            STU_NAME.place(x=30, y=200)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, width=20, validate='key',
                                 bg="yellow", fg="red", font=('times', 23, ' bold '))

            ENR_ENTRY['validatecommand'] = (ENR_ENTRY.register(testVal), '%P', '%d')

            ENR_ENTRY.place(x=290, y=105)


# check id-password

# openning expense-tracker

def admin_panel():
    email = un_entr1.get()
    passw = pw_entr2.get()

    if email == 'vivek':
        if passw == 'vivek123':
            window.destroy()

            win = tk.Tk()
            win.iconbitmap('AMS.ico')
            win.title("EXPENSE TRACKER")
            win.geometry('1280x720+0+0')


        else:
            valid = 'Incorrect ID or Password'
            l.configure(text=valid, bg="white", fg="black", width=20,
                        font=('times', 19, 'bold'))

            l.place(x=280, y=380)

    else:
        valid = 'Incorrect ID or Password'
        l.configure(text=valid, bg="white",
                    fg="black", width=20, font=('times', 19, 'bold'))
        l.place(x=280, y=380)

    lbl = tk.Label(win, text="Income", width=8, height=2, fg="black", bg="gray",
                   font=('times', 8, ' bold '))
    lbl.place(x=500, y=170)

    lbl2 = tk.Label(win, text="Accessories", width=8, fg="black", bg="gray",
                    height=2, font=('times', 8, ' bold '))

    lbl2.place(x=200, y=280)

    lbl2 = tk.Label(win, text="Price", width=8, fg="black", bg="gray",
                    height=2, font=('times', 8, ' bold '))

    lbl2.place(x=200, y=380)

    lbl2 = tk.Label(win, text="Accessories", width=8,
                    fg="black", bg="gray", height=2, font=('times', 8, ' bold '))

    lbl2.place(x=500, y=280)

    lbl2 = tk.Label(win, text="Price", width=8, fg="black",
                    bg="gray", height=2, font=('times', 8, ' bold '))

    lbl2.place(x=500, y=380)

    lbl2 = tk.Label(win, text="Accessories", width=8,
                    fg="black", bg="gray", height=2, font=('times', 8, ' bold '))

    lbl2.place(x=800, y=280)

    lbl2 = tk.Label(win, text="Price", width=8,
                    fg="black", bg="gray", height=2, font=('times', 8, ' bold '))

    lbl2.place(x=800, y=380)

    message = tk.Label(win, text="Expense Tracker", relief="flat", fg="#9c150b",
                       width=50,
                       height=3, font=('times', 30, 'bold '))

    message.place(x=70, y=-50)

    def testVal(inStr, acttyp):

        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True

    t = tk.Entry(win, validate="key", width=8, bg="snow",
                 fg="black", font=('times', 15, ' bold '))

    t['validatecommand'] = (t.register(testVal), '%P', '%d')

    t.place(x=600, y=170)

    txt3 = tk.Entry(win, validate="key", width=8,
                    bg="green", fg="black", font=('times', 15, ' bold '))

    txt3['validatecommand'] = (txt3.register(testVal), '%P', '%d')
    txt3.place(x=300, y=385)
    txtp = tk.Entry(win, validate="key", width=8, bg="green",
                    fg="black", font=('times', 15, ' bold '))

    txtp['validatecommand'] = (txtp.register(testVal), '%P', '%d')

    txtp.place(x=600, y=385)

    txtp1 = tk.Entry(win, validate="key", width=8, bg="green",
                     fg="black", font=('times', 15, ' bold '))

    txtp1['validatecommand'] = (txtp1.register(testVal), '%P', '%d')

    txtp1.place(x=900, y=385)

    """txt = tk.Entry(win, validate="key", width=8, bg="snow",
     fg="black", font=('times', 13, ' bold '))

    txt['validatecommand'] = (txt.register(testVal), '%P', '%d')

    txt.place(x=500, y=190)"""

    txt2 = tk.Entry(win, width=8, bg="yellow",
                    fg="black", font=('times', 15, ' bold '))

    txt2.place(x=300, y=285)

    txt0 = tk.Entry(win, width=8, bg="yellow", fg="black",
                    font=('times', 15, ' bold '))

    txt0.place(x=600, y=285)

    txtl = tk.Entry(win, width=8, bg="yellow", fg="black",
                    font=('times', 15, ' bold '))

    txtl.place(x=900, y=285)

    # calculating balance and income spend money

    def bal():

        income = t.get()

        price = txt3.get()

        p = txtp.get()

        p2 = txtp1.get()

        rr = txt2.get()

        xx = txt0.get()

        yyy = txtl.get()

        if (income == "" or price == "" or p == "" or p2 == ""):
            messagebox.showinfo("Insert Status", "All field Are Required")
        else:
            tero = int(price) + int(p) + int(p2)
            if int(tero) > int(income):
                messagebox.showinfo("Balance", "Insufficient Balance")
            else:
                balance = int(income) - int(price) - int(p) - int(p2)
                messagebox.showinfo("Balance", balance)

                # connection to database

                import mysql.connector
                mydb = mysql.connector.connect(host='localhost', user='root', password='1234', db='vivekexpenses',
                                               auth_plugin='mysql_native_password')
                # mycursor = connection.cursor()
                mycursor = mydb.cursor()

                """creating table in datbase"""

                # mycursor.execute("Create table expenses(name varchar(200),pricesalary int(20))")

                """#inserting value in database"""

                sqlform = "Insert into expenses(name,pricesalary) values(%s,%s)"
                expenses = [("Income", income), (rr, price), (xx, p), (yyy, p2), ("Balance", balance)]

                mycursor.executemany(sqlform, expenses)
                mydb.commit()

                """creating csv file"""

                import csv
                data_list = [["SN", "Name", "price-spend"],
                             [1, "Income", income],
                             [2, "Total spend money ", tero],
                             [3, "Balance", balance]]

                with open('expensetracker.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerows(data_list)

                # visualization of income ,expenses, balances

                import matplotlib.pyplot as plt

                # defining labels
                activities = ['Income', rr, yyy, xx, 'Balance']

                # portion covered by each label
                slices = [int(income), int(price), int(p2), int(p), int(balance)]

                # color for each label
                colors = ['r', 'y', 'g', 'b', 'm']

                # plotting the pie chart
                plt.pie(slices, labels=activities, colors=colors,
                        startangle=90, shadow=True, explode=(0, 0, 0.1, 0, 0),
                        radius=1.2, autopct='%1.1f%%')

                # plotting legend
                plt.legend()

                # showing the plot
                plt.show()

    lbl = tk.Button(win, text="Check Balance", command=bal, width=13, height=2, fg="black", bg="gray",
                    font=('times', 10, ' bold '))

    lbl.place(x=550, y=500)


l = Label(window, bg="ivory", fg="darkgreen")

window.grid_rowconfigure(0, weight=1)

window.grid_columnconfigure(0, weight=1)

window.iconbitmap('AMS.ico')


def on_closing():
    from tkinter import messagebox

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

image0 = Image.open("image99.jpg")

photo2 = ImageTk.PhotoImage(image0)

Notification = tk.Label(window, text="All things good", bg="Green",
                        fg="white", width=15,
                        height=3,
                        font=('times', 17, 'bold'))

AP = tk.Button(window, text="LogIn", command=admin_panel,
               fg="black", bg="gray", width=10,
               height=1, activebackground="Red",
               font=('times', 15, ' bold '))

AP.place(x=467, y=305)

img2 = PhotoImage(file="image104.png")

window.mainloop()