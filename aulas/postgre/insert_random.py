from faker import Faker
import psycopg2

conn = psycopg2.connect(database="loja", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cursor = conn.cursor()
fake = Faker('pt_BR')

n=20
for i in range(n):
    codigo = i
    nome = 'produto_'+str(i+1)
    preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(preco , '\n' , nome)
    querySQL = """INSERT INTO public."PRODUTO"("CODIGO","NOME","PRECO") VALUES (%s,%s,%s)"""
    registro = (codigo, nome, preco)
    cursor.execute(querySQL, registro)

conn.commit()
print("Inserção realizada com sucesso")
conn.close()






