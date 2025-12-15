# Arquivo: gestao_biblioteca.py

class Livro:
    """Representa um livro com título, autor e status de empréstimo."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} - Status: {status}"

class Biblioteca:
    """Gerencia o acervo e os empréstimos de livros."""
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        return f"Livro '{livro.titulo}' adicionado ao acervo."

    def emprestar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                return f"Livro '{titulo}' emprestado com sucesso."
        return f"Livro '{titulo}' não está disponível para empréstimo."

    def devolver_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                return f"Livro '{titulo}' devolvido com sucesso."
        return f"Livro '{titulo}' não pôde ser devolvido (talvez já esteja disponível)."

    def listar_acervo(self):
        if not self.acervo:
            return "A biblioteca está vazia."
        lista_str = "--- Acervo da Biblioteca ---\n"
        for livro in self.acervo:
            lista_str += f"- {livro}\n"
        return lista_str
