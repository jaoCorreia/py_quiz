from typing import List
from models.repositorio_tema import ITemaRepository, IValidadorTema

class SeletorTema:    
    def __init__(self, tema_repository: ITemaRepository, validador: IValidadorTema):
        self._tema_repository = tema_repository
        self._validador = validador
    
    def selecionar_tema_interativo(self) -> str:
        temas_disponiveis = self._tema_repository.obter_temas_disponiveis()
        if not temas_disponiveis:
            raise Exception("Nenhum tema disponível!")
        self._exibir_temas_disponiveis(temas_disponiveis)
        while True:
            tema_escolhido = self._obter_entrada_usuario()
            if self._validador.validar_tema(tema_escolhido, temas_disponiveis):
                return tema_escolhido.lower()
            tema_sugerido = self._tratar_tema_invalido(tema_escolhido, temas_disponiveis)
            if tema_sugerido:
                return tema_sugerido
    
    def _exibir_temas_disponiveis(self, temas: List[str]) -> None:
        print(f"\n📚 Temas disponíveis ({len(temas)}):")        
        colunas = 3
        for i in range(0, len(temas), colunas):
            linha = temas[i:i+colunas]
            linha_formatada = "  ".join(f"📖 {tema.title():<15}" for tema in linha)
            print(f"  {linha_formatada}")
    
    def _obter_entrada_usuario(self) -> str:
        """Obtém entrada do usuário com validação básica"""
        while True:
            tema = input("\n🎯 Digite o tema desejado: ").strip()
            if tema:
                return tema
            print("⚠️ Por favor, digite um tema válido.")
    
    def _tratar_tema_invalido(self, tema: str, temas_disponiveis: List[str]) -> str:
        print(f"❌ Tema '{tema}' não encontrado!")
        sugestoes = self._validador.sugerir_temas_similares(tema, temas_disponiveis)
        if sugestoes:
            print("💡 Você quis dizer:")
            for i, sugestao in enumerate(sugestoes, 1):
                print(f"  {i}. {sugestao.title()}")
            try:
                escolha = input("\nDigite o número da sugestão ou 'n' para tentar novamente: ").strip()
                if escolha.isdigit() and 1 <= int(escolha) <= len(sugestoes):
                    tema_sugerido = sugestoes[int(escolha) - 1]
                    confirma = input(f"Confirma '{tema_sugerido.title()}'? (s/n): ").strip().lower()
                    if confirma in ['s', 'sim', 'y', 'yes']:
                        return tema_sugerido.lower()
            except (ValueError, IndexError):
                pass
        return None