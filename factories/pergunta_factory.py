
# Factory para criar instâncias de Pergunta
from models.pergunta import Pergunta


from models.pergunta import Pergunta, PerguntaMultiplaEscolha

class PerguntaFactory:
    @staticmethod
    def criar(pergunta_dict):
        if 'dicas' in pergunta_dict:
            return PerguntaMultiplaEscolha(
                pergunta_dict["pergunta"],
                pergunta_dict["opcoes"],
                pergunta_dict["dificuldade"],
                pergunta_dict["tema"],
                dicas=pergunta_dict["dicas"]
            )
        return Pergunta(
            pergunta_dict["pergunta"],
            pergunta_dict["opcoes"],
            pergunta_dict["dificuldade"],
            pergunta_dict["tema"]
        )
