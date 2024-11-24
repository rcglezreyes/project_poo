from models.classes_pattern_observer.observer_cls import observer_cls

@observer_cls
class InventoryManageInterface:
    def __init__(self, subject):
        self.subject = subject

    def update(self, event):
        print(f"[Gestión de Inventario] Actualizando inventario debido a: {event}")
