from models.user import User
from models.payment_method import PaymentMethod
from models.client import Client
from models.administrator import Administrator

user = User(
    1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01'
)
payment_method = PaymentMethod(
    1, 'Credit Card', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
)
client = Client(
    1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01', '123 Main St', payment_method, ['Books', 'Electronics']   
)
print('\nCLIENT INFO: \n', client)

print('---------------------------------')

user = User(
    2, 'admin', 'admin@gmailcom', '1234', '435678256', 'administrator', '2021-01-01'
)
admin = Administrator(
    2, 'admin', 'admin@gmailcom', '1234', '435678256', 'administrator', '2021-01-01', ['50% off on all products']
)
print('\nADMIN INFO: \n', admin)

print('---------------------------------')
