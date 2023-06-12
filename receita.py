class Receita:
    
    def __init__(self, titulo, ingredientes, instrucoes):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes
    
    def criar(self, titulo, ingredientes, instrucoes):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes
    
    def ler(self):
        

    def atualizar(self, ler, titulo, ingredientes, instrucoes):
        self.ler = ler
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes
    
    def excluir(self, titulo, ingredientes, instrucoes):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self. instrucoes = instrucoes
        print('Receita excluída com sucesso!')