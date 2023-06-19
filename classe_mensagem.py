class Notificação(Usuario):
    def __init__(self, mensagem):
        super().__init__()
        self.mensagem = mensagem

    def enviar(self):
        print("Enviando notificação...")
        print("Destinatário:")
        self.exibir_informações()
        print(f"Mensagem: {self.mensagem}")

        

