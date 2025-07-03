from builtins import Exception, input, print
from factories.pergunta_factory import PerguntaFactory
from strategies.estrategia_pontuacao import (
    PontuacaoSimples, 
    PontuacaoPorDificuldade, 
    PontuacaoComPenalidade,
    PontuacaoProgessiva
)
from models.jogador import Jogador
from observers.log_observer import LogObserver
from observers.placar_observer import PlacarObserver
from templates.quiz.quiz_console import QuizConsole
from templates.quiz.quiz_cronometrado import QuizCronometrado
from models.seletor_tema import SeletorTema
from models.repositorio_tema import TemaRepository, ValidadorTema

def obter_nome_jogador():
    """Obtém o nome do jogador"""
    while True:
        nome = input("\n👤 Digite seu nome: ").strip()
        if nome:
            return nome
        print("⚠️ Por favor, digite um nome válido.")

def escolher_tipo_quiz():
    """Permite escolher o tipo de quiz"""
    print("\n🎮 Escolha o tipo de quiz:")
    print("1. Quiz Normal")
    print("2. Quiz Cronometrado")
    
    while True:
        try:
            opcao = int(input("Digite sua escolha (1-2): "))
            if opcao in [1, 2]:
                return opcao
            else:
                print("⚠️ Opção inválida! Digite 1 ou 2.")
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

def escolher_estrategia_pontuacao():
    """Permite ao usuário escolher a estratégia de pontuação"""
    print("\n🎯 Escolha o sistema de pontuação:")
    print("1. Simples (1 ponto por acerto)")
    print("2. Por dificuldade (1/2/3 pontos)")
    print("3. Com penalidade (perde pontos por erros)")
    print("4. Progressiva (bônus por sequência de acertos)")

    estrategias = {
        1: PontuacaoSimples(),
        2: PontuacaoPorDificuldade(),
        3: PontuacaoComPenalidade(),
        4: PontuacaoProgessiva()
    }
    
    while True:
        try:
            opcao = int(input("Digite sua escolha (1-4): "))
            if opcao in estrategias:
                return estrategias[opcao]
            else:
                print("⚠️ Opção inválida! Digite um número de 1 a 4.")
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

def main():
    print("🧠 Bem-vindo ao Quiz Avançado!")
    
    try:
        tema_repository = TemaRepository()
        validador_tema = ValidadorTema()
        seletor_tema = SeletorTema(tema_repository, validador_tema)
        
        nome_jogador = obter_nome_jogador()
        jogador = Jogador(nome_jogador)

        placar_observer = PlacarObserver()
        log_observer = LogObserver()
        from observers.ranking_observer import RankingObserver
        ranking_observer = RankingObserver()
        jogador.adicionar_observer(placar_observer)
        jogador.adicionar_observer(log_observer)
        jogador.adicionar_observer(ranking_observer)
        print(f"\n🎭 Observers configurados:")
        print("📊 PlacarObserver - Feedback em tempo real")
        print("📝 LogObserver - Registro de todas as ações")
        print("🏅 RankingObserver - Ranking dos melhores jogadores")

        tema = seletor_tema.selecionar_tema_interativo()
        print(f"\n🎯 Tema selecionado: {tema}")

        tipo_quiz = escolher_tipo_quiz()
        estrategia_pontuacao = escolher_estrategia_pontuacao()

        perguntas_data = tema_repository.obter_perguntas_por_tema(tema)
        if not perguntas_data:
            temas_disponiveis = tema_repository.obter_temas_disponiveis()
            raise Exception(f"Nenhuma pergunta encontrada para '{tema}'. Temas disponíveis: {', '.join(temas_disponiveis)}")
        perguntas_filtradas = [
            PerguntaFactory.criar(p)
            for p in perguntas_data
        ]

        if tipo_quiz == 1:
            quiz = QuizConsole(jogador, perguntas_filtradas, estrategia_pontuacao)
        else:
            try:
                tempo = int(input("⏰ Digite o tempo limite por pergunta (segundos): ") or "30")
            except ValueError:
                tempo = 30
            quiz = QuizCronometrado(jogador, perguntas_filtradas, estrategia_pontuacao, tempo)
        
        # Prints removidos para deixar o jogo mais limpo
        
        print(f"\n🚀 Iniciando quiz...")
        pontuacao_final = quiz.executar_quiz()
        
        print(f"\n🎊 Obrigado por jogar, {nome_jogador}!")
        print(f"🏆 Pontuação final: {pontuacao_final}")
        print("📁 Verifique o arquivo 'quiz_logs.txt' para o histórico completo")

        # Notifica o observer para exibir o ranking final
        jogador.notificar_observers('exibir_ranking', {})
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("💡 Dica: Verifique se todos os arquivos estão no local correto")

if __name__ == "__main__":
    main()