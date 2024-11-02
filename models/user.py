from datetime import datetime

from models.role import Role

class User:
    user_id: int                  # ID único del usuario
    username: str                 # Nombre de usuario
    email: str                    # Correo electrónico
    password: str                 # Contraseña cifrada
    phone: str                    # Número de contacto
    role: Role                    # Rol del usuario
    registration_date: datetime   # Fecha de registro en la plataforma

    def __init__(self, user_id, username, email, password, phone, role, registration_date):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role
        self.registration_date = registration_date
        
    def __str__(self):
        return f' \nUser ID: {self.user_id} \nUsername: {self.username} \nEmail: {self.email} \nPhone: {self.phone} \nRole: {self.role} \nRegistration Date: {self.registration_date}'