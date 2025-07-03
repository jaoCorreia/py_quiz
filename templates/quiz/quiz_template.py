from abc import ABC, abstractmethod
from utils.logger import Logger
 
class TemplateQuiz(ABC):
    def __init__(self, jogador, perguntas, estrategia_pontuacao):
        self.jogador = jogador
        self.perguntas = perguntas
        self.estrategia_pontuacao = estrategia_pontuacao
        self.logger = Logger()
    
    def executar_quiz(self):
        self.inicializar_quiz()
        self.executar_perguntas()
        self.finalizar_quiz()
        return self.resultado_final()

    def executar_perguntas(self):
        """Hook method para execução das perguntas. Pode ser sobrescrito."""
        for i, pergunta in enumerate(self.perguntas):
            self.preparar_pergunta(i, pergunta)
            resposta = self.obter_resposta(pergunta)
            self.processar_resposta(pergunta, resposta)

    def resultado_final(self):
        """Hook method para retornar o resultado final. Pode ser sobrescrito."""
        return self.jogador.pontuacao
    
    def inicializar_quiz(self):
        """Hook method - pode ser sobrescrito"""
        print(f"\n🎮 Iniciando quiz para {self.jogador.nome}!")
        self.logger.log_quiz_start(
            self.jogador.nome, 
            "tema_generico", 
            self.estrategia_pontuacao.__class__.__name__
        )
    
    @abstractmethod
    def preparar_pergunta(self, indice, pergunta):
        """Método abstrato - deve ser implementado pelas subclasses"""
        pass
    
    @abstractmethod
    def obter_resposta(self, pergunta):
        """Método abstrato - deve ser implementado pelas subclasses"""
        pass
    
    def processar_resposta(self, pergunta, resposta):
        """Hook method - pode ser sobrescrito"""
        try:
            acertou = pergunta.esta_correta(resposta)
            pontos = self.estrategia_pontuacao.calcular_pontos(
                str(pergunta.dificuldade), acertou
            )
            
            self.jogador.responder_pergunta(pergunta.pergunta, acertou, pontos)
            
            if acertou:
                print("✅ Correto!")
            else:
                print("❌ Errado.")
                
        except (ValueError, IndexError):
            print("⚠️ Entrada inválida.")
            pontos = self.estrategia_pontuacao.calcular_pontos(
                str(pergunta.dificuldade), False
            )
            self.jogador.responder_pergunta(pergunta.pergunta, False, pontos)
    
    def finalizar_quiz(self):
        """Hook method - pode ser sobrescrito"""
        self.jogador.finalizar_quiz()
        self.mostrar_resultado_final()
    
    def mostrar_resultado_final(self):
        """Hook method - pode ser sobrescrito"""
        print(f"\n🏆 RESULTADO FINAL 🏆")
        print(f"Jogador: {self.jogador.nome}")
        print(f"Pontuação: {self.jogador.pontuacao}")
        print(f"Total de perguntas: {self.jogador.total_respostas}")
        print(f"Percentual de acertos: {self.jogador.get_percentual_acertos():.1f}%")
