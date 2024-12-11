from tkinter import *
import time 
from createacc import Createacc
from viewacc import SeeAcc
from accnum import Acc_Num
from withdraw import Withdraw 
from accnum1 import AccNum1
from deposit import Deposit
from accnum2 import AccNum2

class Application:
    def __init__(self, master):
        
        self.master = master
        
        #========================Frames
        self.top = Frame(master, height=140, bg="gray")
        self.top.pack(fill=X)
        
        self.bottom = Frame(master, height=600, bg="light pink")
        self.bottom.pack(fill=X)
        
        #=========================TITLE
        self.top_image = PhotoImage(file="icons/icon1.png")
        
        self.top_label = Label(self.top, image=self.top_image, bg="gray", height=100)
        self.top_label.place(x=250, y=25) 
        
        self.top_image1 = PhotoImage(file="icons/icon1.png")
        self.top_label1 = Label(self.top, image=self.top_image1, bg="gray", height=100)
        self.top_label1.place(x=950, y=28) 
        
        self.heading = Label(self.top, text="PENNYPAL", font=("Monaco 70 bold"), bg="gray")
        self.heading.place(x=420, y=30)
        
        #========================buttons
        self.bottom_image1 = PhotoImage(file="icons/icon2..png")
        self.bottom_label1 = Label(self.bottom, image=self.bottom_image1, bg="light pink")
        self.bottom_label1.place(x=480, y=90) 
        
        self.create_btn = Button(self.bottom, text="Create Account", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8, command=self.create_acc)
        self.create_btn.place(x=100, y=100)        
        
        self.see_acc = Button(self.bottom, text="View Account", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8, command=self.view_acc)
        self.see_acc.place(x=100, y=200)           
        
        self.withdraw_btn = Button(self.bottom, text="Withdraw Money", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8, command=self.withdraw)
        self.withdraw_btn.place(x=100, y=300)      
        
        self.deposite_btn = Button(self.bottom, text="Deposit Money", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8, command=self.deposit)
        self.deposite_btn.place(x=887, y=100)        
        
        self.about_us = Button(self.bottom, text="About Us", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8)
        self.about_us.place(x=887, y=200)           
        
        self.exit_btn = Button(self.bottom, text="Exit", font='arial 20 bold', fg='white', bg='gray', width=15, anchor=W, relief=RAISED, bd=8, command=self.exit)
        self.exit_btn.place(x=887, y=300) 
        
        self.clock = Label(self.bottom, font=('time', 25, 'bold'), relief=GROOVE, background='light pink', foreground='black')     
        self.clock.place(x=380, y=5)
        
        self.update_time()
    
    def update_time(self):
        time_string = time.strftime("%H:%M:%S")  
        date_string = time.strftime("%d/%m/%Y")  
        self.clock.config(text=f"Time: {time_string}   Date: {date_string}")
        self.clock.after(1000, self.update_time)  
    
    def create_acc(self):
        createacc=Createacc()                                                          
    def view_acc(self):
        accountnumber=Acc_Num()
    def withdraw(self):
        accountnumber=AccNum1()
    def deposit(self):
        accountnumber=AccNum2()  
    def exit(self):
        self.master.destroy()   
 
def main():
    root = Tk()
    app = Application(root)
    
    root.title("Piggy Bank")
    root.resizable(False, False)
    root.geometry("1280x850")
    root.mainloop()

if __name__ == "__main__":
    main()  