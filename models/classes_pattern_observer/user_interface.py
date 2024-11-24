from models.classes_pattern_observer.observer_cls import observer_cls

@observer_cls
class UserInterface:
    def __init__(self, subject):
        self.subject = subject

    def update(self, event):
        print(f"[Interfaz de Usuario] Notificación recibida: {event}")


