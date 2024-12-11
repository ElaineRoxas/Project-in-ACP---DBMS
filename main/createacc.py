from tkinter import *
from tkinter import messagebox
import mysql.connector
import datetime

class Createacc(Toplevel):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry('500x600')
        self.title("Create Account")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=100, bg="light blue", relief=SUNKEN, bd=5)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=550, bg="light pink")
        self.bottom.pack(fill=X)

        # Heading and Date
        self.heading = Label(self.top, text="Create New Account", font='arial 20 bold', fg="black", bg='light blue')
        self.heading.place(x=120, y=30)

        date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.date_lbl = Label(self.top, text=f"Today's Date: {date}", font='arial 10 bold', bg='lightblue3', fg="black")
        self.date_lbl.place(x=300, y=65)

        # Name
        self.label_name = Label(self.bottom, text="Name", font='arial 12 bold', fg='black', bg='light pink')
        self.label_name.place(x=50, y=40)
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.place(x=150, y=40)

        # Account Number
        self.label_accnum = Label(self.bottom, text="Acc_Num", font='arial 12 bold', fg='black', bg='light pink')
        self.label_accnum.place(x=50, y=80)
        self.entry_accnum = Entry(self.bottom, width=30, bd=4)
        self.entry_accnum.place(x=150, y=80)

        # Account Money
        self.label_acc_money = Label(self.bottom, text="Acc_Money", font='arial 12 bold', fg='black', bg='light pink')
        self.label_acc_money.place(x=50, y=120)
        self.entry_acc_money = Entry(self.bottom, width=30, bd=4)
        self.entry_acc_money.place(x=150, y=120)

        # Contact Number
        self.label_contact = Label(self.bottom, text="Contact No.", font='arial 12 bold', fg='black', bg='light pink')
        self.label_contact.place(x=50, y=160)
        self.entry_contact = Entry(self.bottom, width=30, bd=4)
        self.entry_contact.place(x=150, y=160)

        # Address
        self.label_acc_address = Label(self.bottom, text="Address", font='arial 12 bold', fg='black', bg='light pink')
        self.label_acc_address.place(x=50, y=200)
        self.entry_acc_address = Text(self.bottom, width=30, height=5, bd=5)
        self.entry_acc_address.place(x=150, y=200)

        # Button
        button = Button(self.bottom, text='Create Account', fg='black', font='arial 10 bold', bg="RosyBrown1", command=self.add_people)
        button.place(x=250, y=300)

    def add_people(self):
        # Get input values
        name = self.entry_name.get()
        account_number = self.entry_accnum.get()
        account_money = self.entry_acc_money.get()
        contact = self.entry_contact.get()
        address = self.entry_acc_address.get("1.0", "end-1c")

        if not all([name.strip(), account_number.strip(), account_money.strip(), contact.strip(), address.strip()]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            account_money = float(account_money)

            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="bank_db")
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO accounts (name, account_number, account_money, contact_number, address)
            VALUES (%s, %s, %s, %s, %s)
            """, (name, account_number, account_money, contact, address))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Account created successfully!")

            # Clear input fields
            self.entry_name.delete(0, "end")
            self.entry_accnum.delete(0, "end")
            self.entry_acc_money.delete(0, "end")
            self.entry_contact.delete(0, "end")
            self.entry_acc_address.delete("1.0", "end")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Account Money!")

def initialize_database():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS bank_db")
        cursor.execute("USE bank_db")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            account_number VARCHAR(20) UNIQUE NOT NULL,
            account_money DECIMAL(10, 2) NOT NULL,
            contact_number VARCHAR(15) NOT NULL,
            address TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def main():
    initialize_database()
    root = Tk()
    root.withdraw()  
    Createacc().mainloop()

if __name__ == "__main__":
    main()
