from poo import *
from pessoafisica import PessoaFisica
pessoa_1 = Pessoa("Yan Martins", 18)
pessoa_2 = PessoaFisica(17080617707,"Martins DEV", 19)
pessoa_3 = PessoaJuridica("2007/100-00", "Yan DEV", 20)

print(f"O nome da pessoa_1 é {pessoa_1.getNome()} e a idade é {pessoa_1.getIdade()}")
print(f"O nome da pessoa_2 é {pessoa_2.getNome()} e a idade é {pessoa_2.getIdade()} e seu cpf é: {pessoa_2.getCPF()}")
print(f"O nome da pessoa_3 é {pessoa_3.getNome()} e a idade é {pessoa_3.getIdade()} e seu cnpj é: {pessoa_3.getCNPJ()}")



