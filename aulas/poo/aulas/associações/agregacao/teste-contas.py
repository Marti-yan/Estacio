from contas import Conta
from clientes import *
cliente1 = Cliente(123,"yan","rua 1")
cliente2 = Cliente(345, "maria","rua 2")
conta1 = Conta([cliente1,cliente2], 1,0) 
# conta1.gerarsaldo()
# conta1.depositar(1500)
# conta1.sacar(500)
# conta1.gerarsaldo()


cliente3 = Cliente(987,"cleitin", "rua 3")
cliente4 = Cliente(789, "rasta", "rua 4")
conta2 = Conta([cliente3,cliente4], 2, 500)
print(f"Nome: {conta2.clientes[0].nome} // Endereço: {conta2.clientes[0].endereco}")
print(f"Nome: {conta2.clientes[1].nome} // Endereço: {conta2.clientes[1].endereco}")