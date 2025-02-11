import mysql.connector

class MySQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
    
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão com o banco de dados estabelecida!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")
            self.conexao = None
    
    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def ler_dados(self, query: str) -> None:
        self.conectar()
        if self.conexao:
            print(f'QUERY: {query}')
            cursor = self.conexao.cursor()
            try:
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as err:
                print(f"Erro ao ler dados: {err}\nQUERY: {query}")
                return None
            finally:
                cursor.close()
            self.fechar_conexao()

    def inserir_dados(self, query: str):
        self.conectar()
        if self.conexao:
            print(f'QUERY: {query}')
            cursor = self.conexao.cursor()
            sql = query

            try:
                cursor.execute(sql)
                self.conexao.commit()
                print("Dados inseridos com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao inserir dados: {err}")
            finally:
                cursor.close()

    def atualizar_dados(self, query: str) -> None:
        if self.conexao:
            print(f'QUERY: {query}')
            cursor = self.conexao.cursor()
            try:
                cursor.execute(query)
                self.conexao.commit()
                print("Dados atualizados com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao atualizar dados: {err}")
            finally:
                cursor.close()
            self.fechar_conexao()

    def deletar_dados(self, query: str) -> None:
        self.conectar()
        if self.conexao:
            print(f'QUERY: {query}')
            cursor = self.conexao.cursor()
            try:
                cursor.execute(query)
                self.conexao.commit()
                print("Dados deletados com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao deletar dados: {err}")
            finally:
                cursor.close()
            self.fechar_conexao()
    
    def execute_sql(self, query: str) -> None:
        self.conectar()
        if self.conexao:
            print(f'QUERY: {query}')
            cursor = self.conexao.cursor()
            try:
                cursor.execute(query)
                self.conexao.commit()
                print("Dados deletados com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao deletar dados: {err}")
            finally:
                cursor.close()
            self.fechar_conexao()

# if __name__ == '__main__':
#     mysqldb = MySQLDB(host='localhost', user='root', password='Marcos@09', database='LISTA_GUIA')
#     mysqldb.conectar()
    # mysqldb.inserir_dados(query='INSERT INTO teste1 (nome, idade) VALUES ("MARCOS FARIAS", 240);')
    # mysqldb.inserir_dados(query='INSERT INTO teste1 (nome, idade) VALUES ("MARCOS TESTE", 545);')
    # mysqldb.atualizar_dados(query='UPDATE teste1 SET nome = "MARCOS HOFFMANN" WHERE nome = "MARCOS";')
    # input(f'RESULTADO: {mysqldb.ler_dados("SELECT * FROM teste1")}')
    # input(f'RESULTADO: {mysqldb.ler_dados("SELECT * FROM empresas where id = {int(10)}")}')
    # input(f'{mysqldb.ler_dados(f"SELECT * FROM empresas WHERE id = {int(10)}")}')
    # mysqldb.deletar_dados(query='DELETE FROM teste1 WHERE nome = "MARCOS TESTE";')
    # input(f'RESULTADO: {mysqldb.ler_dados("SELECT * FROM teste1")}')
