from datetime import datetime

from models.classes_poo.role import Role

import re

class User:
    user_id: int                  # ID único del usuario
    username: str                 # Nombre de usuario
    email: str                    # Correo electrónico
    password: str                 # Contraseña cifrada
    phone: str                    # Número de contacto
    role: Role                    # Rol del usuario
    registration_date: datetime   # Fecha de registro en la plataforma

    def __init__(self, user_id=None, username=None, email=None, password=None, phone=None, role=None, registration_date=None):
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
            
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str) -> None:
        if re.match(r'\d{9}', phone) is None:
            raise ValueError('El número de contacto debe tener 9 dígitos.')
        else:
            self.__phone = phone
            
    @property
    def role(self) -> Role:
        return self.__role
    
    @role.setter
    def role(self, role: Role) -> None:
        self.__role = role
        
    @property
    def registration_date(self) -> datetime:
        return self.__registration_date
    
    @registration_date.setter
    def registration_date(self, registration_date: datetime) -> None:
        self.__registration_date = registration_date
        
    @property
    def user_id(self) -> int:
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id: int) -> None:
        self.__user_id = user_id
        
    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, username: str) -> None:
        self.__username = username
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, password: str) -> None:
        self.__password = password
    
    def __str__(self):
        return f' \nUser ID: {self.user_id} \nUsername: {self.username} \nEmail: {self.email} \nPhone: {self.phone} \nRole: {self.role} \nRegistration Date: {self.registration_date}'