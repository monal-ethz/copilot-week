class OperationsProgram:
    def __init__(self, data_program):
        self.data_program = data_program

    def execute(self, operation_type):
        if operation_type == 'TOTAL':
            self.total()
        elif operation_type == 'CREDIT':
            self.credit()
        elif operation_type == 'DEBIT':
            self.debit()
        else:
            print("Invalid operation type.")

    def total(self):
        balance = self.data_program.read_balance()
        print(f"Current balance: {balance:.2f}")

    def credit(self):
        amount = float(input("Enter credit amount: "))
        balance = self.data_program.read_balance()
        balance += amount
        self.data_program.write_balance(balance)
        print(f"Amount credited. New balance: {balance:.2f}")

    def debit(self):
        amount = float(input("Enter debit amount: "))
        balance = self.data_program.read_balance()
        if balance >= amount:
            balance -= amount
            self.data_program.write_balance(balance)
            print(f"Amount debited. New balance: {balance:.2f}")
        else:
            print("Insufficient funds for this debit.")