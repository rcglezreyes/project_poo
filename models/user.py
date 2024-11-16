from datetime import datetime

from models.role import Role

import re

class User:
    user_id: int                  # ID único del usuario
    username: str                 # Nombre de usuario
    email: str                    # Correo electrónico
    password: str                 # Contraseña cifrada
    phone: str                    # Número de contacto
    role: Role                    # Rol del usuario
    registration_date: datetime   # Fecha de registro en la plataforma

    def __init__(self, user_id, username, email, password, phone, role, registration_date):
        self.__user_id = user_id
        self.__username = username
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__role = role
        self.__registration_date = registration_date
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        if re.match(r'[^@]+@[^@]+\.[^@]+', email) is None:
            raise ValueError('El correo electrónico debe ser válido.')
        else:
            self.__email = email
    
    
    def __str__(self):
        return f' \nUser ID: {self.user_id} \nUsername: {self.username} \nEmail: {self.email} \nPhone: {self.phone} \nRole: {self.role} \nRegistration Date: {self.registration_date}'