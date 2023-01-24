class Veiculo():
    def __init__(self, nome,VM , KML):
        self.nome = nome
        self.velMax = VM
        self.KmL = KML
        
    def showText(self):
        print(f'Nome = {self.nome}')
        print(f'Velocidade maxima = {self.velMax}')
        print(f'Quilometros por litro = {self.KmL}')        
        
        

        
modelo_carro = Veiculo("GT-R",300,4)
modelo_carro.showText()        
        
        
        