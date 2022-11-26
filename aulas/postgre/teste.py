from faker import Faker
import psycopg2
conn = psycopg2.connect(database="teste", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()

#cur.execute("""select * from public."AGENDA" where "id"=2""")
#registro=cur.fetchone() # so esta mostrando o primeiro
#print(registro)
#conn.commit()
#print("Seleção realizada com sucesso!");


cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (15, 'Pessoa 15' , '022996139790' )""")
conn.commit()
print("Inserção realizada com sucesso!")


# cur.execute("""Delete from public."AGENDA" where "id"=1""") 
# conn.commit() 
# cont=cur.rowcount 
# print(cont, "Registro excluído com sucesso!") 
# print("Exclusão realizada com sucesso!"); 

conn.commit() 
print("Inserção realizada com sucesso!")
conn.close()