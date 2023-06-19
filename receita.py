class Receita:
    
    def __init__(self, titulo = "", ingredientes = [], instrucoes = ""):
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes
    
    def criar(self):
        self.titulo = input("Digite o título da receita: ")
        num_ingredientes = int(input("Digite o número de ingredientes: "))
        for _ in range(num_ingredientes):
            ingrediente = input("Digite um ingrediente: ")
            self.ingredientes.append(ingrediente)
        self.instrucoes = input("Digite as instruções da receita: ")
        print("Receita criada com sucesso!")
    
    def ler(self):
        print("Título: ", self.titulo)
        print("Ingredientes: ")
        for ingrediente in self.ingredientes:
            print("-", ingrediente)
        print("Instruções: ", self.instrucoes)
        

    def atualizar(self):
        self.ler()
        opcao = input("O que você deseja atualizar? (título, ingredientes, instruções): ")
        if opcao == "título":
            self.titulo = input("Digite o novo título da receita: ")
        elif opcao == "ingredientes":
            num_ingredientes = int(input("Digite o novo número de ingredientes: "))
            self.ingredientes = []
            for _ in range(num_ingredientes):
                ingrediente = input("Digite um novo ingrediente: ")
                self.ingredientes.append(ingrediente)
        elif opcao == "instruções":
            self.instrucoes = input("Digite as novas instruções da receita: ")
        else:
            print("Opção inválida!")
            return
        print("Receita atualizada com sucesso!")
    
    def excluir(self):
        self.titulo = ""
        self.ingredientes = []
        self.instrucoes = ""
        print("Receita excluída com sucesso!")