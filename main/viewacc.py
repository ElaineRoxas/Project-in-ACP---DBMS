from tkinter import *
from tkinter import messagebox
import mysql.connector

class SeeAcc(Toplevel):
    def __init__(self, accnum):
        super().__init__()
        self.title("View Account")
        self.geometry("500x400")
        self.accnum = accnum

        # Frames
        self.top = Frame(self, height=100, bg="light blue", relief=SUNKEN, bd=5)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=300, bg="light pink")
        self.bottom.pack(fill=X)

        # Heading
        Label(self.top, text="Account Information", font='arial 20 bold', fg="black", bg='light blue').place(x=120, y=30)

        try:
            # Database connection
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="bank_db")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT account_number, name, account_money, address, contact_number
                FROM accounts WHERE account_number = %s
            """, (self.accnum,))
            result = cursor.fetchone()

            if result:
                self.show_account_info(*result)
            else:
                raise Exception("Account not found!")

            conn.close()

        except (mysql.connector.Error, Exception) as e:
            messagebox.showerror("Error", f"Error: {e}")
            self.destroy()

    def show_account_info(self, acc_num, acc_name, acc_money, acc_address, contact_number):
        # Display account details
        for idx, (label_text, value) in enumerate([("Name", acc_name), ("Account Number", acc_num),
                                                   ("Balance", f"{acc_money:.2f}"), ("Contact Number", contact_number)]):
            Label(self.bottom, text=f"{label_text}:", font='arial 12 bold', bg='light pink').place(x=50, y=40+40*idx)
            Entry(self.bottom, width=30, bd=4, state="readonly", textvariable=StringVar(value=value)).place(x=200, y=40+40*idx)

        # Address
        Label(self.bottom, text="Address:", font='arial 12 bold', bg='light pink').place(x=50, y=200)
        text_address = Text(self.bottom, width=30, height=3, bd=4)
        text_address.insert("1.0", acc_address)
        text_address.config(state="disabled")
        text_address.place(x=200, y=200)

# Test the class
if __name__ == "__main__":
    root = Tk()
    root.withdraw() 

    accnum = "123456789"  # Example account number
    SeeAcc(accnum)

    root.mainloop()
