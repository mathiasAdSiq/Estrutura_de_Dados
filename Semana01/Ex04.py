
class Livro:
    def __init__(self, titulo, autor, numero_pag):
        self.titulo = titulo
        self.autor = autor
        self.numero_pag = numero_pag

    def metodo(self):
        if self.numero_pag <= 100:
            print("Livro é curto")
        else:
            print("Livro é longo")

LOTR = Livro("O Senhor dos Anéis", "J.R.R. Tolkien",1000)
Cortico = Livro("O Cortiço", "Aluísio Azevedo",50)

LOTR.metodo()
Cortico.metodo()
