class Extrato:
    def __init_(self):
        self.transacoes = []

    def imprimir(self):
        self.transacoes = []
        for p in self.transacoes:
            print(f"{p[0]} {p[1]}")
            
            
class Conta():
    def __init__(self,clientes,numero,saldo):  
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()
        
    def depositar(self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor])
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE",valor])
            return True
    
class Cliente():
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco    
        
c1 = Cliente("11111111","yan","rua dos carralos")
c2 = Cliente("22222222","Martins","imbigo")
conta = Conta([c1,c2], 25135 , 2500)
conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()
 
            
            