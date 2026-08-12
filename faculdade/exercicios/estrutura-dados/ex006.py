class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= saque

    def mostrar_saldo(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.saldo}')

c1 = ContaBancaria('thalis', 100)
c1.depositar(50)
c1.sacar(30)
c1.sacar(200)
c1.mostrar_saldo()