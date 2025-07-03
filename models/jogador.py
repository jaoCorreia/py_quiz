from observers.observer import Subject

class Jogador(Subject):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.pontuacao = 0
        self.respostas_corretas = 0
        self.total_respostas = 0
    
    def responder_pergunta(self, pergunta, resposta_correta, pontos_obtidos):
        self.total_respostas += 1
        self.pontuacao += pontos_obtidos
        
        if resposta_correta:
            self.respostas_corretas += 1
        
        self.notificar_observers("resposta_respondida", {
            'jogador': self.nome,
            'pergunta': pergunta,
            'acertou': resposta_correta,
            'pontos': pontos_obtidos
        })
    
    def finalizar_quiz(self):
        self.notificar_observers("quiz_finalizado", {
            'jogador': self.nome,
            'pontuacao_final': self.pontuacao,
            'total_perguntas': self.total_respostas
        })
    
    def get_percentual_acertos(self):
        if self.total_respostas == 0:
            return 0
        return (self.respostas_corretas / self.total_respostas) * 100