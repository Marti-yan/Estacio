# class Circulo():
#     _total_circulos = 0
    
#     def __init__(self,pontox, pontoy, raio):
#         self.pontox = pontox
#         self.pontoy = pontoy
#         self.raio = raio
#         type(self)._total_circulos +=1
        
#         @classmethod
#         def get_total_circulos(cls): 
#             return cls._total_circulos
        
# circ1 = Circulo(1,1,10)
# print(circ1._total_circulos)
# circ2 = Circulo(1,1,10)
# # print(circ2.total_circulos)


class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    @classmethod
    def fromString(cls,texto):
        nome, sobrenome = map(str, texto.split(' '))
        obj = cls(nome, sobrenome)
        return obj
    
    @staticmethod
    def isValid(texto):
        nomes = texto.split(' ')
        return len(nomes) > 1
    
    
registro1 = NomeCompleto.fromString("Yan Martins")
print(f'{registro1.nome} \n{registro1.sobrenome}')    
    
print(NomeCompleto.isValid("Yan Martins")) 






