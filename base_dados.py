from pymongo import MongoClient


class BaseDados:
    def __init__(self, filtro):
        self.filtro = filtro
        self.result = None

    def conectar(self):
        try:
            client = MongoClient(
                'mongodb+srv://Caraio123:Caraio123@tcc.3kv1h.mongodb.net/test?authSource=admin&replicaSet=atlas-rhjxk6-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
            return client
        except:
            return 'Não foi possível conectar ao banco de dados.'

    def buscar(self):
        conexao = self.conectar()
        resultSet = conexao['myosotis']['desaparecidos'].find(
            filter=self.filtro)
        self.result = resultSet

    def imprimir(self):
        for desaparecido in self.result:
            print("NOME\t\tSTATUS\n{}\t{}\n".format(
                desaparecido[' nome'], desaparecido[' status']))


def main():

    filtro = {'id': '6'}
    teste = BaseDados(filtro)
    teste.buscar()
    teste.imprimir()


if __name__ == "__main__":
    main()
