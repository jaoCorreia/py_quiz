from builtins import enumerate, input, int, print

class Quiz:
    def __init__(self, perguntas, estrategia_selecao=None, estrategia_pontuacao=None):
        self.perguntas = estrategia_selecao.selecionar(perguntas) if estrategia_selecao else perguntas
        self.estrategia_pontuacao = estrategia_pontuacao

    def iniciar(self):
        pontuacao_total = 0
        
        for i, pergunta in enumerate(self.perguntas):
            print(f"\n📋 Pergunta {i + 1} - Dificuldade: {str(pergunta.dificuldade).title()}")
            print(f"{pergunta.pergunta}")
            
            for j, opcao in enumerate(pergunta.opcoes):
                print(f"{j + 1}. {opcao['label']}")
            
            try:
                resposta = int(input("Digite o número da resposta: ")) - 1
                acertou = pergunta.esta_correta(resposta)
                
                if acertou:
                    print("✅ Correto!")
                else:
                    print("❌ Errado.")
                
                if self.estrategia_pontuacao:
                    pontos_obtidos = self.estrategia_pontuacao.calcular_pontos(
                        str(pergunta.dificuldade), acertou
                    )
                    pontuacao_total += pontos_obtidos
                    
                    if pontos_obtidos > 0:
                        print(f"🎯 +{pontos_obtidos} pontos!")
                    elif pontos_obtidos < 0:
                        print(f"📉 {pontos_obtidos} pontos (penalidade)")
                else:
                    if acertou:
                        pontuacao_total += 1
                        
            except ValueError:
                print("⚠️ Entrada inválida.")
                if self.estrategia_pontuacao:
                    pontos_obtidos = self.estrategia_pontuacao.calcular_pontos(
                        str(pergunta.dificuldade), False
                    )
                    pontuacao_total += pontos_obtidos
                    if pontos_obtidos < 0:
                        print(f"📉 {pontos_obtidos} pontos (penalidade por entrada inválida)")
        
        return pontuacao_total