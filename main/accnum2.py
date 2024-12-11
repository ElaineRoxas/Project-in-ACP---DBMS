from tkinter import *
from tkinter import messagebox
from deposit import Deposit

class AccNum2(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Information Needed")
        self.geometry("400x370")
        self.config(bg="light pink")
        self.resizable(False, False)

        # Header
        Frame(self, height=70, bg="light blue", relief=SUNKEN, bd=5).pack(fill=X)
        Label(self, text="   PENNYPAL", font='"MONACO" 25 bold', bg="light blue").place(x=60, y=10)
        Label(self, text="Information Needed", font='"Arial" 10 bold', bg="pink").place(x=110, y=80)

        # Account Input
        Label(self, text="Account Number:", font='arial 12 bold', bg='light pink').place(x=10, y=130)
        self.entry_accnum = Entry(self, width=25, bd=4, font='arial 12')
        self.entry_accnum.insert(0, "Enter Account Number")
        self.entry_accnum.place(x=150, y=130)
        self.entry_accnum.bind("<FocusIn>", lambda _: self.entry_accnum.delete(0, END) if self.entry_accnum.get() == "Enter Account Number" else None)
        self.entry_accnum.bind("<FocusOut>", lambda _: self.entry_accnum.insert(0, "Enter Account Number") if not self.entry_accnum.get() else None)

        # Submit Button
        Button(self, text='SUBMIT', font='arial 12', bg="light pink", command=self.acc_id).place(x=160, y=200)

    def acc_id(self):
        accnum = self.entry_accnum.get().strip()
        if not accnum or accnum == "Enter Account Number":
            messagebox.showerror("Error", "Please enter a valid account number.")
        elif not accnum.isdigit():
            messagebox.showerror("Error", "Account number must be numeric.")
        else:
            try:
                Deposit(accnum)
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    AccNum2().mainloop()
