# Quiz com Design Patterns

Este projeto é um quiz interativo em Python que demonstra o uso de diversos padrões de projeto (Design Patterns) clássicos. O sistema é modular, extensível e serve como referência prática para estudo de padrões.

## Padrões de Projeto Utilizados

### 1. Template Method

- **Onde:**
  - `templates/quiz/quiz_template.py` (classe `TemplateQuiz`)
  - Subclasses: `QuizConsole`, `QuizCronometrado`
- **Como:**
  - Define o fluxo principal do quiz (`executar_quiz`) e delega etapas específicas para métodos abstratos ou hooks, permitindo fácil extensão do comportamento.

### 2. Observer

- **Onde:**
  - `observers/observer.py` (interfaces `Observer` e `Subject`)
  - `models/jogador.py` (classe `Jogador` herda de `Subject`)
  - Observers: `observers/log_observer.py`, `observers/placar_observer.py`, `observers/ranking_observer.py`
- **Como:**
  - Observers são notificados de eventos do quiz (resposta, finalização, etc.), permitindo ações desacopladas como log, placar e ranking.

### 3. Singleton

- **Onde:**
  - `utils/logger.py` (classe `Logger`)
- **Como:**
  - Garante que apenas uma instância do logger seja usada em todo o sistema, centralizando o registro de logs.

### 4. Factory Method

- **Onde:**
  - `factories/pergunta_factory.py` (classe `PerguntaFactory`)
- **Como:**
  - Centraliza a criação de objetos `Pergunta` e `PerguntaMultiplaEscolha`, permitindo fácil extensão para novos tipos de perguntas.

### 5. Strategy

- **Onde:**
  - `strategies/estrategia_pontuacao.py` (interface `StrategyPontuacao` e subclasses)
- **Como:**
  - Permite trocar a lógica de pontuação do quiz em tempo de execução, escolhendo entre diferentes estratégias (simples, por dificuldade, penalidade, progressiva).

---

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```
3. Siga as instruções no terminal para jogar o quiz.

## Estrutura de Pastas

- `main.py` — Ponto de entrada do sistema
- `models/` — Modelos de domínio (Jogador, Pergunta, etc.)
- `templates/quiz/` — Template Method e variações do quiz
- `observers/` — Implementação do padrão Observer
- `factories/` — Factory para perguntas
- `strategies/` — Estratégias de pontuação
- `utils/` — Logger Singleton
- `data/` — Perguntas do quiz (JSON)

---

---

## Como jogar

1. Execute o comando:
   ```bash
   python main.py
   ```
2. Digite seu nome quando solicitado.
3. Escolha o tema do quiz (você pode digitar parte do nome e aceitar sugestões).
4. Escolha o tipo de quiz (normal ou cronometrado).
5. Escolha a estratégia de pontuação.
6. Responda às perguntas:
   - Para perguntas normais, digite o número da resposta.
   - Para perguntas de múltipla escolha, digite os números das respostas corretas separados por vírgula (ex: `1,3`).
7. Veja seu resultado e o ranking ao final.

---

Projeto para fins didáticos. Sinta-se à vontade para expandir e experimentar outros padrões!
