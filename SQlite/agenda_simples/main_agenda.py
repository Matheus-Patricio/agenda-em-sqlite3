import sqlite3

class AgendaDb:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
    
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone,  id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.conn.execute(consulta, (nome, telefone, id))
        self.conn.commit()
    
    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.conn.execute(consulta, (id,)) # uma vigula pois significa que é uma tupla , sem isso nao se torna uma tupla
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDb('agenda.db')
    agenda.inserir('Matheus', '999999') # adicionando dado no DB.
    agenda.inserir('Luiza', '199999')
    agenda.inserir('Lucas', '499999')
    agenda.inserir('Lianderson', '599999')
    agenda.inserir('Maria', '699999')

    agenda.listar() # listando o bando de dados dentro do terminal (ID, NOME, TELEFONE).

    agenda.editar('Ivete', '151515', 5) # => alterando um item da tabela do banco de dados (5, 'lucas', 499999).
    
    # agenda.excluir(25) # => excluindo o id25 que antes era o id5, porém foi alterado.

    agenda.inserir('Jaden', '666666')

    agenda.buscar('Jaden')
    
    agenda.excluir(35)

    