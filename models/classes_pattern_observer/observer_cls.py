def observer_cls(cls):
    """
    Decorador para registrar automáticamente métodos de clases como observadores.
    """
    class AnnotatedObserver(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if hasattr(self, "subject") and hasattr(self, "update"):
                self.subject.add_observer(self)

        def __del__(self):
            if hasattr(self, "subject"):
                self.subject.delete_observer(self)
    return AnnotatedObserver
