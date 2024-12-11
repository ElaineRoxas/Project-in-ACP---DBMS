from tkinter import *
from tkinter import messagebox  
from viewacc import SeeAcc 

class Acc_Num(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        # Window properties
        self.title("Information Needed")
        self.config(bg="light pink")
        self.geometry("400x370")
        self.resizable(False, False)
        
        # Top Frame
        self.Top_frame = Frame(self, height=70, bg="light blue", relief=SUNKEN, bd=5)
        self.Top_frame.pack(fill=X)

        self.label_title1 = Label(self.Top_frame, text="   PENNYPAL", font='"MONACO" 25 bold', fg='black', bg="light blue")
        self.label_title1.place(x=60, y=10)

        # Information Label
        self.label_title2 = Label(self, text="     Information Needed", font='"Arial" 10 bold', fg="black", bg="pink")
        self.label_title2.place(x=110, y=80)
        
        # Account Number Input
        self.label_accnum = Label(self, text="Acc_Num:", font='arial 12 bold', fg="black", bg='light pink')
        self.label_accnum.place(x=10, y=130)
        
        self.entry_accnum = Entry(self, width=25, bd=4, font='arial 12')
        self.entry_accnum.insert(0, "Enter Account Number")
        self.entry_accnum.place(x=110, y=130)

        # Clear placeholder text when focused
        self.entry_accnum.bind("<FocusIn>", self.clear_placeholder)

        # Submit Button
        button = Button(self, text='SUBMIT', fg='black', font='arial 12', bg="light pink", command=self.acc_id, relief=RAISED)
        button.place(x=110, y=180)
                                
    def clear_placeholder(self, event):
        # Clear placeholder text on focus
        if self.entry_accnum.get() == "Enter Account Number":
            self.entry_accnum.delete(0, END)

    def acc_id(self):
        # Get Account Number Input
        accnum = self.entry_accnum.get().strip()

        if not accnum or accnum == "Enter Account Number":
            messagebox.showerror("Error", "Please enter a valid Account Number!")
            return

        try:
            # Call SeeAcc to view the account information
            SeeAcc(accnum)
            self.destroy()  # Close the window only if successful
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
