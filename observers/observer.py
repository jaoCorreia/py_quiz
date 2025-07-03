from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, evento, dados):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def adicionar_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remover_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notificar_observers(self, evento, dados):
        for observer in self._observers:
            observer.update(evento, dados)
