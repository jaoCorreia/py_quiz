from observers.observer import Observer
from utils.logger import Logger

class LogObserver(Observer):
    def __init__(self):
        self.logger = Logger()
    
    def update(self, evento, dados):
        if evento == "resposta_respondida":
            self.logger.log_resposta(
                dados['jogador'], 
                dados['pergunta'], 
                dados['acertou'], 
                dados['pontos']
            )
        elif evento == "quiz_finalizado":
            self.logger.log_quiz_fim(
                dados['jogador'], 
                dados['pontuacao_final'], 
                dados['total_perguntas']
            )