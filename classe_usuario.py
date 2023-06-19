import getpass
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def registrar(self):
        print('Registrando o usuário:', self.nome)
        print('Digite seu email', self.email)
        getpass.getpass('Digite sua senha', self.senha)

    def fazer_login(self, email, senha):
        if self.email == email and self.senha == senha:
            print('Usuário', self.nome, 'fez login com sucesso!')
        else:
            print('Falha no login. Verifique suas credenciais.')

    def fazer_logout(self):
        print('Usuário', self.nome, 'fez logout.')



        
               


