class Receita:
    
    def __init__(self, titulo, ingredientes, instrucoes):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes
    
    def criar(self, titulo, ingredientes, instrucoes):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes  
