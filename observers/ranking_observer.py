
import json, os
from observers.observer import Observer


class RankingObserver(Observer):
    def __init__(self, arquivo_ranking='ranking.json', tamanho_max=5):
        self.arquivo_ranking = arquivo_ranking
        self.tamanho_max = tamanho_max
        self.ranking = self._carregar_ranking()

    def _carregar_ranking(self):
        if os.path.exists(self.arquivo_ranking):
            with open(self.arquivo_ranking, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def _salvar_ranking(self):
        with open(self.arquivo_ranking, 'w', encoding='utf-8') as f:
            json.dump(self.ranking, f, ensure_ascii=False, indent=4)

    def update(self, evento, dados):
        if evento == 'quiz_finalizado':
            usuario = dados.get('jogador')
            pontos = dados.get('pontuacao_final', 0)
            if usuario is None:
                return
            self._atualizar_ranking(usuario, pontos)
            self._salvar_ranking()
            self.exibir_ranking()

    def exibir_ranking(self):
        print("\n🏅 RANKING ATUALIZADO 🏅")
        for i, item in enumerate(self.ranking, 1):
            print(f"{i}º - {item['usuario']} : {item['pontos']} pontos")

    def _atualizar_ranking(self, usuario, pontos):
        # Remove usuário se já existe
        self.ranking = [item for item in self.ranking if item['usuario'] != usuario]
        # Adiciona novo score
        self.ranking.append({'usuario': usuario, 'pontos': pontos})
        # Ordena por pontos decrescente
        self.ranking.sort(key=lambda x: x['pontos'], reverse=True)
        # Mantém apenas os top N
        if len(self.ranking) > self.tamanho_max:
            self.ranking = self.ranking[:self.tamanho_max]
