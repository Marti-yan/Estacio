class Pessoa:     # classe
    def __init__(self, nome, idade):   #metodos
        self.nome = nome    # no JS é 'this'
        self.idade = idade
        
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
        
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade    
        
class PessoaJuridica(Pessoa): 
    def __init__(self, cnpj ,nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = cnpj
             
    def setCNPJ(self, cnpj):
        self.CNPJ = cnpj
        
    def getCNPJ(self):
        return self.CNPJ     
   
   
   
   
   
   
        