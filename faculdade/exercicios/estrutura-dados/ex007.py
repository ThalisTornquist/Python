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

class ContaEspecial(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, saque):
        if saque > self.saldo + self.limite:
            print('Limite insuficiente')
        else:
            self.saldo -= saque





c1 = ContaEspecial('thalis', 100, 100)
c1.depositar(50)
c1.sacar(30)
c1.sacar(200)
c1.mostrar_saldo()