from builtins import IndexError



class Pergunta:
    def __init__(self, pergunta, opcoes, dificuldade, tema):
        self.pergunta = pergunta
        self.opcoes = opcoes  
        self.dificuldade = dificuldade
        self.tema = tema

    def esta_correta(self, indice):
        try:
            return self.opcoes[indice]["is_correct"]
        except IndexError:
            return False


class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, pergunta, opcoes, dificuldade, tema, dicas=None):
        super().__init__(pergunta, opcoes, dificuldade, tema)
        self.dicas = dicas or []

    def mostrar_dica(self):
        if self.dicas:
            print(f"Dica: {self.dicas[0]}")
        else:
            print("Sem dicas disponíveis.")

    def esta_correta(self, indices):
        if not isinstance(indices, list):
            indices = [indices]
        corretas = [i for i, op in enumerate(self.opcoes) if op["is_correct"]]
        return sorted(indices) == sorted(corretas)
