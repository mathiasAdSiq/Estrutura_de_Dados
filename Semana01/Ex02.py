
class Contato:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

agenda = []

luis = Contato("Luis",99552310,'luislelo@gmail.com')
ana = Contato("Ana",99230450,'analuisa@gmail.com')
joao = Contato("Joao",99436743,' joaopedro@gmail.com')

agenda.extend([luis,ana,joao])

for contato in agenda:
    print(f"Nome:{contato.nome}, Telefone:{contato.telefone}, Email:{contato.email}")

