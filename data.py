class DataProgram:
    def __init__(self, filename='balance.dat'):
        self.filename = filename
        self.balance = 1000.00
        self.read_balance()

    def read_balance(self):
        try:
            with open(self.filename, 'r') as file:
                self.balance = float(file.read().strip())
        except FileNotFoundError:
            self.write_balance()
        return self.balance

    def write_balance(self, balance):
        self.balance = balance
        with open(self.filename, 'w') as file:
            file.write(f"{self.balance:.2f}")