import sqlite3
connection = sqlite3.connect('bank_cx_details')
cursor = connection.cursor()


cursor.execute()

class BANK:
    def _init_(self, cx_id, cx_name, acc_type, branch_name, cx_address, balance):
        self.cx_id = cx_id
        self.cx_name = cx_name
        self.acc_type = acc_type
        self.branch_name = branch_name
        self.cx_address = cx_address
        self.balance = balance


        cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)",
                        (cx_id, cx_name, acc_type, branch_name, cx_address, balance))
        connection.commit()

    def display(self):

        cursor.execute("SELECT * FROM customers WHERE id = ?", (self.cx_id,))
        customer = cursor.fetchone()

        print(f"Customer ID: {customer[0]}")
        print(f"Customer Name: {customer[1]}")
        print(f"Account Type: {customer[2]}")
        print(f"Branch Name: {customer[3]}")
        print(f"Customer Address: {customer[4]}")
        print(f"Balance: {customer[5]}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")


        cursor.execute("UPDATE customers SET balance = ? WHERE id = ?", (self.balance, self.cx_id))
        connection.commit()

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f"Withdrawal Successful! Balance after withdrawal: {self.balance}")


            cursor.execute("UPDATE customers SET balance = ? WHERE id = ?", (self.balance, self.cx_id))
            connection.commit()
        else:
            print("Insufficient balance!")

    def loan(self, principle_amount, interest, time_period):
        total_amount = (principle_amount * interest * time_period) / 100
        emi = total_amount / time_period
        print(f"Total loan amount: {total_amount}")
        print(f"EMI/month: {emi}")

obj = BANK()
obj.display()

connection.close()