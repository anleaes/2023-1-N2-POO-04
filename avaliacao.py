class Avaliacao:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

    def avaliar(self):
        # lógica de avaliar
        print(f"Usuario: {self.usuario}\nValor: {self.valor}")
        