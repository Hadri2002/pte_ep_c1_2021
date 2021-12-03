class BankAccount:
    """Bankszámla osztálya"""

    def __init__(self, name:str, account_number:str, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyenleg_kiiratasa(self):
         print("Az egyenleg: {}".format(self.balance))

    def withdrawal(self, osszeg:int) -> None:
        if self.balance >= osszeg:
            self.balance -= osszeg
            print("Sikeres pénzfelvétel")
        else:
            print("Nincs rendelkezésre álló összeg")

    def deposit(self, osszeg:int) -> None:
        self.balance += osszeg

account1 = BankAccount("Jóska", "7171717171", 100)
account1.egyenleg_kiiratasa()
account1.withdrawal(10)
account1.egyenleg_kiiratasa()
account1.deposit(200)
account1.egyenleg_kiiratasa()
account2 = BankAccount("John", "33333333")
account2.egyenleg_kiiratasa()
account2.withdrawal(200)