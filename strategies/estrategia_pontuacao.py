from abc import ABC, abstractmethod

class StrategyPontuacao(ABC):
    @abstractmethod
    def calcular_pontos(self, dificuldade, acertou):
        """
        Calcula os pontos para uma pergunta respondida
        
        Args:
            dificuldade (str): Nível de dificuldade da pergunta
            acertou (bool): Se a pergunta foi respondida corretamente
            
        Returns:
            int: Pontos obtidos
        """
        pass

class PontuacaoSimples(StrategyPontuacao):
    """Estratégia simples: 1 ponto por acerto, 0 por erro"""
    
    def calcular_pontos(self, dificuldade, acertou):
        return 1 if acertou else 0

class PontuacaoPorDificuldade(StrategyPontuacao):
    """Estratégia baseada na dificuldade: mais pontos para perguntas mais difíceis"""
    
    def __init__(self):
        self.pontos_por_dificuldade = {
            "facil": 1,
            "medio": 2,
            "dificil": 3
        }
    
    def calcular_pontos(self, dificuldade, acertou):
        if not acertou:
            return 0
        return self.pontos_por_dificuldade.get(dificuldade.lower(), 1)

class PontuacaoComPenalidade(StrategyPontuacao):
    """Estratégia com penalidade: perde pontos por erros"""
    
    def __init__(self):
        self.pontos_acerto = {
            "facil": 1,
            "medio": 2,
            "dificil": 3
        }
        self.penalidade_erro = {
            "facil": 0,
            "medio": -1,
            "dificil": -1
        }
    
    def calcular_pontos(self, dificuldade, acertou):
        dif_lower = dificuldade.lower()
        if acertou:
            return self.pontos_acerto.get(dif_lower, 1)
        else:
            return self.penalidade_erro.get(dif_lower, 0)

class PontuacaoProgessiva(StrategyPontuacao):
    """Estratégia progressiva: mais pontos por sequências de acertos"""
    
    def __init__(self):
        self.sequencia_acertos = 0
        self.multiplicador_base = 1
    
    def calcular_pontos(self, dificuldade, acertou):
        pontos_base = {
            "facil": 1,
            "medio": 2,
            "dificil": 3
        }.get(dificuldade.lower(), 1)
        
        if acertou:
            self.sequencia_acertos += 1
            multiplicador = 1 + (self.sequencia_acertos // 3)
            return pontos_base * multiplicador
        else:
            self.sequencia_acertos = 0
            return 0