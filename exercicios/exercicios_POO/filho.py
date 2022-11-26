class Veiculo():
    def __init__(self, nome,VM , KML):
        self.nome = nome
        self.velMax = VM
        self.KmL = KML
        
    def showText(self):
        print(f'Nome = {self.nome}')
        print(f'Velocidade maxima = {self.velMax}')
        print(f'Quilometros por litro = {self.KmL}')        
    
        
        
class Onibus(Veiculo):
    def __init__(self , nome , KML , VM, assentos = 70): #se eu não passar nenhum valor como paramentro, ele vai ser igual a 70
        super().__init__(nome, KML, VM)
        self.assentos = assentos
        
    def showText(self):
        super().showText()
        print(f'Quantidade de assentos = {self.assentos}') 


class Moto(Veiculo):
    pass


v1 = Onibus("busão",100,10) # posso ou não passar o valor do ultimo parametro 'assentos'
v1.showText()        
print()
v2 = Moto("Yamaha",150,20)
v2.showText() 
        