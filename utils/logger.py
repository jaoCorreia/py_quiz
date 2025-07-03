import datetime
import os

class Logger:
    _instance = None
    _initialized = False
    
    def __new__(self):
        if self._instance is None:
            self._instance = super(Logger, self).__new__(self)
        return self._instance
    
    def __init__(self):
        if not Logger._initialized:
            self.log_file = "quiz_logs.txt"
            Logger._initialized = True
    
    def log(self, message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Erro ao escrever log: {e}")
    
    def log_quiz_start(self, jogador_nome, tema, estrategia):
        self.log(f"Quiz iniciado - Jogador: {jogador_nome}, Tema: {tema}, Estratégia: {estrategia}")
    
    def log_resposta(self, jogador_nome, pergunta, resposta_correta, pontos):
        status = "ACERTO" if resposta_correta else "ERRO"
        self.log(f"Jogador: {jogador_nome} - {status} - Pontos: {pontos}")
    
    def log_quiz_fim(self, jogador_nome, pontuacao_final, total_perguntas):
        self.log(f"Quiz finalizado - Jogador: {jogador_nome}, Pontuação: {pontuacao_final}/{total_perguntas}")
