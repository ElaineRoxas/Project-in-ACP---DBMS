from tkinter import *
from tkinter import messagebox
from withdraw import Withdraw  # Ensure the `Withdraw` class is properly implemented


class AccNum1(Toplevel):
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
        self.label_accnum = Label(self, text="Account Number:", font='arial 12 bold', fg="black", bg='light pink')
        self.label_accnum.place(x=10, y=130)
        
        self.entry_accnum = Entry(self, width=25, bd=4, font='arial 12')
        self.entry_accnum.insert(0, "Enter Account Number")
        self.entry_accnum.place(x=150, y=130)

        # Bindings for placeholder behavior
        self.entry_accnum.bind("<FocusIn>", self.clear_placeholder)
        self.entry_accnum.bind("<FocusOut>", self.restore_placeholder)

        # Submit Button
        button = Button(self, text='SUBMIT', fg='black', font='arial 12', bg="light pink", command=self.acc_id, relief=RAISED)
        button.place(x=160, y=200)

    def clear_placeholder(self, event):
        if self.entry_accnum.get() == "Enter Account Number":
            self.entry_accnum.delete(0, END)

    def restore_placeholder(self, event):
        if not self.entry_accnum.get():
            self.entry_accnum.insert(0, "Enter Account Number")

    def acc_id(self):
        accnum = self.entry_accnum.get()
        if accnum.strip() == "" or accnum == "Enter Account Number":
            messagebox.showerror("Input Error", "Please enter a valid account number.")
        else:
            try:
                Withdraw(accnum)  
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")


# For Testing Purposes
if __name__ == "__main__":
    root = Tk()
    root.withdraw() 

    acc_window = AccNum1()
    acc_window.mainloop()
