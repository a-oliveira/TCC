from pymongo import MongoClient
import psycopg2


class BaseDados:
    def __init__(self, banco, caracteristica):
        self.banco = banco
        if self.banco == "MDB":
            self.filtro = caracteristica
        else:
            self.query = "select nome, status from ( select * from desaparecidos.pessoa p where p.cor_pele ="+"\'"+caracteristica + \
                "\'"+") as desaparecido inner join desaparecidos.registro_desaparecimento rd on rd.pessoa_id = desaparecido.id"
        self.result = None

    def conectarMongoDB(self):
        try:
            client = MongoClient(
                'mongodb+srv://Caraio123:Caraio123@tcc.3kv1h.mongodb.net/test?authSource=admin&replicaSet=atlas-rhjxk6-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
            return client
        except:
            print('Não foi possível conectar ao banco de dados.')

    def conectarPG(self):
        try:
            conexao = psycopg2.connect(user="postgres",
                                       password="Caraio123",
                                       host="localhost",
                                       port="5432",
                                       database="postgres")
            return conexao
        except:
            print('Não foi possível conectar ao banco de dados.')

    def buscar(self):
        if self.banco == "MDB":
            conexao = self.conectarMongoDB()
            resultSet = conexao['myosotis']['desaparecidos'].find(
                filter=self.filtro)
            self.result = resultSet

        elif self.banco == "PG":
            conexao = self.conectarPG()
            cursor = conexao.cursor()
            cursor.execute(self.query)
            resultSet = cursor.fetchall()
            self.result = resultSet

    def imprimir(self):
        if self.banco == "MDB":
            for desaparecido in self.result:
                print("NOME\t\tSTATUS\n{}\t{}\n".format(
                    desaparecido[' nome'], desaparecido[' status']))

        elif self.banco == "PG":
            for desaparecido in self.result:
                print("NOME\t\tSTATUS\n{}\t{}\n".format(
                    desaparecido[0], desaparecido[1]))


def main():

    #filtro = {'id': '6'}
    filtro = "branca"
    teste = BaseDados("PG", filtro)
    #teste = BaseDados("MDB", filtro)
    teste.buscar()
    teste.imprimir()


if __name__ == "__main__":
    main()
