class Comentario:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

    def publicar(self):
        # Lógica para publicar o comentário
        print(f"Usuário: {self.usuario}\nTexto: {self.texto}")