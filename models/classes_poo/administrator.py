from models.classes_poo.user import User

class Administrator(User):
    list_promotions: list[str]    # Lista de promociones
    
    def __init__(self, user_id=None, username=None, email=None, password=None, phone=None, role=None, registration_date=None, list_promotions=None):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.list_promotions = list_promotions
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nList of promotions: {self.list_promotions}'
    
    def manage_inventory(self):
        return 'Inventory managed'