from tkinter import *
from tkinter import messagebox
import mysql.connector
from decimal import Decimal

class Withdraw(Toplevel):
    def __init__(self, accnum):
        super().__init__()
        self.title("Withdraw Money")
        self.geometry("500x500")
        self.resizable(False, False)
        self.accnum = accnum

        # Frames and Heading
        self.top = Frame(self, height=100, bg="light blue", relief=SUNKEN, bd=5)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="light pink")
        self.bottom.pack(fill=X)
        Label(self.top, text="Withdraw Money", font='arial 20 bold', fg="black", bg='light blue').place(x=150, y=30)

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="bank_db")
            cursor = conn.cursor()
            cursor.execute("SELECT name, account_number, account_money, contact_number, address FROM accounts WHERE account_number = %s", (accnum,))
            result = cursor.fetchone()
            if not result:
                raise Exception("Account not found!")
            acc_name, acc_num, acc_money, contact_number, acc_address = result
            self.current_balance = Decimal(acc_money)

            # Account details display
            self.create_label_entry("Name:", 50, 20, acc_name)
            self.create_label_entry("Account Number:", 50, 60, acc_num)
            self.create_label_entry("Contact Number:", 50, 100, contact_number)
            self.create_label_entry("Address:", 50, 140, acc_address)

            # Balance and Withdrawal Input
            Label(self.bottom, text="Your Current Balance is:", font='arial 12 bold', bg='light pink').place(x=50, y=200)
            self.balance_label = Label(self.bottom, text=f"{self.current_balance:.2f}", font='arial 12', bg='light pink')
            self.balance_label.place(x=250, y=200)

            Label(self.bottom, text="Enter Amount of Withdraw:", font='arial 12 bold', bg='light pink').place(x=50, y=240)
            self.withdraw_entry = Entry(self.bottom, width=30, bd=4)
            self.withdraw_entry.place(x=260, y=240)

            Button(self.bottom, text="Withdraw", font='arial 12 bold', bg="light blue", command=self.withdraw_money).place(x=200, y=280)

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error fetching account details: {e}")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.destroy()

    def create_label_entry(self, label_text, x, y, value):
        Label(self.bottom, text=label_text, font='arial 12 bold', bg='light pink').place(x=x, y=y)
        entry = Entry(self.bottom, width=30, bd=4)
        entry.insert(0, value)
        entry.config(state="readonly")
        entry.place(x=200, y=y)

    def withdraw_money(self):
        try:
            withdraw_amount = self.withdraw_entry.get()
            if not withdraw_amount:
                messagebox.showerror("Error", "Please enter an amount to withdraw.")
                return

            withdraw_amount = Decimal(withdraw_amount)
            if withdraw_amount <= 0 or withdraw_amount > self.current_balance:
                messagebox.showerror("Error", "Invalid withdrawal amount.")
                return

            conn = mysql.connector.connect(host="localhost", user="root", password="", database="bank_db")
            cursor = conn.cursor()
            new_balance = self.current_balance - withdraw_amount
            cursor.execute("UPDATE accounts SET account_money = %s WHERE account_number = %s", (new_balance, self.accnum))
            conn.commit()
            self.current_balance = new_balance
            self.balance_label.config(text=f"{self.current_balance:.2f}")
            messagebox.showinfo("Success", "Withdrawal successful!")
            self.withdraw_entry.delete(0, "end")
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error processing withdrawal: {e}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
