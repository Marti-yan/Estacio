import psycopg2
conn = psycopg2.connect(database = "loja", user="postgres" , password="1234" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 

cur.execute("""select * from public."PRODUTO" """) 
registro=cur.fetchone() # so esta mostrando o primeiro
print(registro) 
conn.commit() 
print("Seleção realizada com sucesso!"); 


# cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (2, 'Pessoa 2' , '02299999000' )""") 
# conn.commit() 
# print("Inserção realizada com sucesso!")


# cur.execute("""Delete from public."AGENDA" where "id"=1""") 
# conn.commit() 
# cont=cur.rowcount 
# print(cont, "Registro excluído com sucesso!") 
# print("Exclusão realizada com sucesso!"); 



conn.close()