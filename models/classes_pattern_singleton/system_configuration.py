from models.classes_pattern_singleton.decorators import singleton

@singleton
class SystemConfiguration:
    def __init__(self, db_url=None, ui_config=None):
        self.db_url = db_url or "postgres://localhost:5432/ecommerce"
        self.ui_config = ui_config or {"theme": "light", "language": "es"}

    def show_configuration(self):
        return {
            "db_url": self.db_url,
            "ui_config": self.ui_config
        }
