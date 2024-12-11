from tkinter import *
from tkinter import messagebox
import mysql.connector
from decimal import Decimal

class Deposit(Toplevel):
    def __init__(self, accnum):
        super().__init__()
        self.title("Deposit Money")
        self.geometry("500x500")
        self.resizable(False, False)
        self.accnum = accnum

        # Frames and Heading
        self.top = Frame(self, height=100, bg="light blue", relief=SUNKEN, bd=5)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="light pink")
        self.bottom.pack(fill=X)
        Label(self.top, text="Deposit Money", font='arial 20 bold', fg="black", bg='light blue').place(x=150, y=30)

        try:
            # Database connection
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="bank_db"
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name, account_number, account_money, contact_number, address FROM accounts WHERE account_number = %s",
                (self.accnum,),
            )
            result = cursor.fetchone()
            if not result:
                raise Exception("Account not found!")

            acc_name, acc_num, acc_money, contact_number, acc_address = result
            self.current_balance = Decimal(acc_money)

            # Display account information
            Label(self.bottom, text="Name:", font='arial 12 bold', bg='light pink').place(x=50, y=20)
            self.name_entry = self.create_readonly_entry(200, 20, acc_name)

            Label(self.bottom, text="Account Number:", font='arial 12 bold', bg='light pink').place(x=50, y=60)
            self.accnum_entry = self.create_readonly_entry(200, 60, acc_num)

            Label(self.bottom, text="Contact Number:", font='arial 12 bold', bg='light pink').place(x=50, y=100)
            self.contact_entry = self.create_readonly_entry(200, 100, contact_number)

            Label(self.bottom, text="Address:", font='arial 12 bold', bg='light pink').place(x=50, y=140)
            self.address_entry = self.create_readonly_entry(200, 140, acc_address)

            Label(self.bottom, text="Your Current Balance is:", font='arial 12 bold', bg='light pink').place(x=50, y=200)
            self.balance_label = Label(self.bottom, text=f"{self.current_balance:.2f}", font='arial 12', bg='light pink')
            self.balance_label.place(x=250, y=200)

            Label(self.bottom, text="Enter Amount to Deposit:", font='arial 12 bold', bg='light pink').place(x=50, y=240)
            self.deposit_entry = Entry(self.bottom, width=30, bd=4)
            self.deposit_entry.place(x=260, y=240)

            Button(self.bottom, text="Deposit", font='arial 12 bold', bg="light blue", command=self.deposit_money).place(x=200, y=280)

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error fetching account details: {e}")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.destroy()

    def create_readonly_entry(self, x, y, value):
        entry = Entry(self.bottom, width=30, bd=4)
        entry.insert(0, value)
        entry.config(state="readonly")
        entry.place(x=x, y=y)
        return entry

    def deposit_money(self):
        try:
            deposit_amount = self.deposit_entry.get()
            if not deposit_amount:
                messagebox.showerror("Error", "Please enter an amount to deposit.")
                return

            deposit_amount = Decimal(deposit_amount)
            if deposit_amount <= 0:
                messagebox.showerror("Error", "Invalid deposit amount.")
                return

            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="bank_db"
            )
            cursor = conn.cursor()
            new_balance = self.current_balance + deposit_amount
            cursor.execute(
                "UPDATE accounts SET account_money = %s WHERE account_number = %s",
                (new_balance, self.accnum),
            )
            conn.commit()

            self.current_balance = new_balance
            self.balance_label.config(text=f"{self.current_balance:.2f}")
            messagebox.showinfo("Success", "Deposit successful!")
            self.deposit_entry.delete(0, "end")
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error processing deposit: {e}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
