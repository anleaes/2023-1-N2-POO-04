from django.db import models



# Create your models here.

class Revenue(models.Model):
    def __init__(self, titulo="", ingredientes=[], instrucoes=""):
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

    def excluir(self):
        confirmacao = input("Tem certeza de que deseja excluir a receita? (S/N): ")
        if confirmacao.upper() == "S":
            self.titulo = ""
            self.ingredientes = []
            self.instrucoes = ""
            print("Receita excluída com sucesso!")
        else:
            print("Exclusão cancelada.")

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering =['id']

    def __str__(self):
        return self.name


receita1 = Revenue()
receita1.criar()
receita1.ler()
receita1.excluir()
