from weakref import WeakSet

class Subject:
    def __init__(self):
        self._observers = WeakSet()

    def add_observer(self, observer):
        self._observers.add(observer)

    def delete_observer(self, observer):
        self._observers.discard(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)
