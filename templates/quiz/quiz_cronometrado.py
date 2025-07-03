import time
from templates.quiz.quiz_template import TemplateQuiz

class QuizCronometrado(TemplateQuiz):
    def __init__(self, jogador, perguntas, estrategia_pontuacao, tempo_limite=30):
        super().__init__(jogador, perguntas, estrategia_pontuacao)
        self.tempo_limite = tempo_limite
        self.tempo_total = 0
    
    def inicializar_quiz(self):
        super().inicializar_quiz()
        print(f"⏰ Tempo limite por pergunta: {self.tempo_limite} segundos")
        self.tempo_inicio = time.time()
    
    def preparar_pergunta(self, indice, pergunta):
        print(f"\n📋 Pergunta {indice + 1} - Dificuldade: {pergunta.dificuldade}")
        print(f"⏰ Tempo restante: {self.tempo_limite} segundos")
        print(f"{pergunta.pergunta}")
        
        for j, opcao in enumerate(pergunta.opcoes):
            print(f"{j + 1}. {opcao['label']}")
        
        self.tempo_pergunta_inicio = time.time()
    
    def obter_resposta(self, pergunta):
        try:
            # Simulação de input com timeout (em um sistema real, usaria threading)
            resposta = int(input("Digite o número da resposta: ")) - 1
            tempo_resposta = time.time() - self.tempo_pergunta_inicio
            
            if tempo_resposta > self.tempo_limite:
                print("⏰ Tempo esgotado!")
                return -1
            
            return resposta
        except ValueError:
            return -1
    
    def finalizar_quiz(self):
        self.tempo_total = time.time() - self.tempo_inicio
        super().finalizar_quiz()
    
    def mostrar_resultado_final(self):
        super().mostrar_resultado_final()
        print(f"⏰ Tempo total: {self.tempo_total:.1f} segundos")