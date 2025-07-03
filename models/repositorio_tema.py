from abc import ABC, abstractmethod
from typing import List, Dict, Any
import json
import os

class ITemaRepository(ABC):
    """Interface para repositório de temas"""
    @abstractmethod
    def obter_temas_disponiveis(self) -> List[str]:
        pass
    
    @abstractmethod
    def obter_perguntas_por_tema(self, tema: str) -> List[Dict[str, Any]]:
        pass

class IValidadorTema(ABC):
    """Interface para validação de temas"""
    @abstractmethod
    def validar_tema(self, tema: str, temas_disponiveis: List[str]) -> bool:
        pass
    
    @abstractmethod
    def sugerir_temas_similares(self, tema: str, temas_disponiveis: List[str]) -> List[str]:
        pass

class TemaRepository(ITemaRepository):
    """Repositório concreto para temas"""
    
    def __init__(self, caminho_arquivo: str = None):
        if caminho_arquivo is None:
            self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "perguntas.json")
        else:
            self.caminho = caminho_arquivo
    
    def obter_temas_disponiveis(self) -> List[str]:
        """Obtém todos os temas disponíveis dinamicamente"""
        try:
            with open(self.caminho, encoding="utf-8") as f:
                todas_perguntas = json.load(f)
            
            temas = set(pergunta["tema"].lower() for pergunta in todas_perguntas)
            return sorted(list(temas))
        
        except FileNotFoundError:
            print(f"⚠️ Arquivo {self.caminho} não encontrado!")
            return []
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler arquivo JSON!")
            return []
    
    def obter_perguntas_por_tema(self, tema: str) -> List[Dict[str, Any]]:
        """Obtém perguntas filtradas por tema"""
        try:
            with open(self.caminho, encoding="utf-8") as f:
                todas_perguntas = json.load(f)
            
            return [p for p in todas_perguntas if p["tema"].lower() == tema.lower()]
        
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class ValidadorTema(IValidadorTema):
    """Validador concreto para temas"""
    
    def validar_tema(self, tema: str, temas_disponiveis: List[str]) -> bool:
        """Valida se o tema existe"""
        return tema.lower() in [t.lower() for t in temas_disponiveis]
    
    def sugerir_temas_similares(self, tema: str, temas_disponiveis: List[str]) -> List[str]:
        """Sugere temas similares usando distância de edição simples"""
        tema_lower = tema.lower()
        sugestoes = []
        
        for tema_disponivel in temas_disponiveis:
            tema_disp_lower = tema_disponivel.lower()
            
            if tema_lower in tema_disp_lower or tema_disp_lower in tema_lower:
                sugestoes.append(tema_disponivel)
            
            elif tema_disp_lower.startswith(tema_lower[:3]) and len(tema_lower) >= 3:
                sugestoes.append(tema_disponivel)
        
        return sugestoes[:3]  