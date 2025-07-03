from templates.quiz.quiz_template import TemplateQuiz

class QuizConsole(TemplateQuiz):
    def preparar_pergunta(self, indice, pergunta):
        print(f"\n📋 Pergunta {indice + 1} - Dificuldade: {pergunta.dificuldade}")
        print(f"{pergunta.pergunta}")
        
        for j, opcao in enumerate(pergunta.opcoes):
            print(f"{j + 1}. {opcao['label']}")
    
    def obter_resposta(self, pergunta):
        if hasattr(pergunta, 'tipo') and getattr(pergunta, 'tipo', None) == 'multipla_escolha':
            entrada = input("Digite os números das respostas separadas por vírgula: ")
            try:
                indices = [int(x.strip()) - 1 for x in entrada.split(',') if x.strip()]
                return indices
            except ValueError:
                return []
        elif pergunta.__class__.__name__ == 'PerguntaMultiplaEscolha':
            entrada = input("Digite os números das respostas separadas por vírgula: ")
            try:
                indices = [int(x.strip()) - 1 for x in entrada.split(',') if x.strip()]
                return indices
            except ValueError:
                return []
        else:
            try:
                resposta = int(input("Digite o número da resposta: ")) - 1
                return resposta
            except ValueError:
                return -1
