import datetime
from observers.observer import Observer

class PlacarObserver(Observer):
    def __init__(self):
        self.historico_pontuacao = []
    
    def update(self, evento, dados):
        if evento == "resposta_respondida":
            jogador = dados['jogador']
            pontos = dados['pontos']
            acertou = dados['acertou']
            
            self.historico_pontuacao.append({
                'jogador': jogador,
                'pontos': pontos,
                'acertou': acertou,
                'timestamp': datetime.datetime.now()
            })
            
            if acertou:
                print(f"🎉 {jogador} acertou e ganhou {pontos} pontos!")
            else:
                print(f"😞 {jogador} errou. Pontos: {pontos}")
        
        elif evento == "quiz_finalizado":
            jogador = dados['jogador']
            pontuacao_final = dados['pontuacao_final']
            print(f"\n🏆 {jogador} finalizou com {pontuacao_final} pontos!")