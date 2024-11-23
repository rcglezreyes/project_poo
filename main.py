from models.user import User
from models.payment_method import PaymentMethod
from models.client import Client
from models.administrator import Administrator
from models.product import Product
from models.physical_product import PhysicalProduct
from models.digital_product import DigitalProduct
from models.shopping_cart import ShoppingCart
from models.category import Category
from models.digital_inventory_manager import DigitalInventoryManager
from models.physical_inventory_manager import PhysicalInventoryManager
from models.payment_process import PaymentProcess
from models.card_payment import CardPayment
from models.paypal_payment import PaypalPayment


# # def mostrar_detalles_producto(producto: Product):
# #     print(producto.mostrar_detalle())

# # # user = User(
# # #     1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01'
# # # )

# # # print('\nCLIENT INFO: \n', client)

# # # print('---------------------------------')

# # # user = User(
# # #     2, 'admin', 'admin@gmailcom', '1234', '435678256', 'administrator', '2021-01-01'
# # # )
# # # admin = Administrator(
# # #     2, 'admin', 'admin@gmailcom', '1234', '435678256', 'administrator', '2021-01-01', ['50% off on all products']
# # # )
# # # print('\nADMIN INFO: \n', admin)

# # # print('---------------------------------')

# # # Crear instancias con todos los argumentos
# # producto_fisico = PhysicalProduct(
# #     1, "Laptop", "Laptop física de alta calidad", 1000.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
# # )

# # producto_digital = DigitalProduct(
# #     2, "E-Book", "E-Book de programación en Python", 20.0, 100, "Libros", "https://example.com/ebook.jpg", "https://ebook.com/file", "PDF", 1.2
# # )

# # # Usar la función polimórfica
# # print()
# # print('-----MOSTRANDO EJEMPLO DE POLIMORFISMO Y SOBREESCRITURA DE METODOS-----')
# # mostrar_detalles_producto(producto_fisico)  # Llama a PhysicalProduct.mostrarDetalle()
# # print('---------------------------------')
# # mostrar_detalles_producto(producto_digital) # Llama a DigitalProduct.mostrarDetalle()
# # print()
# # print()
# # print('-----MOSTRANDO EJEMPLO DE SOBRECARGA DE METODOS-----')
# # payment_method = PaymentMethod(
# #     1, 'Credit Card', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
# # )
# # client = Client(
# #     1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01', '123 Main St', payment_method, ['Books', 'Electronics']   
# # )
# # carrito = ShoppingCart(1, client, [], 0.0)

# # # Sobrecarga en acción
# # carrito.agregar_producto(producto_fisico)  # Agregar por objeto
# # carrito.agregar_producto(3, "Producto Temporal")  # Agregar por ID y nombre
# # carrito.agregar_producto("Producto Genérico", 50.0)  # Agregar por nombre y precio
# # print()

# # # Ver contenido del carrito
# # for producto in carrito.products:
# #     print(producto.mostrar_detalle())
# #     print()
    
# producto_fisico = PhysicalProduct(
#     1, "Laptop", "Laptop física de alta calidad", 20.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
# )

# producto_digital = DigitalProduct(
#     2, "E-Book", "E-Book de programación en Python", 20.0, 100, "Libros", "https://example.com/ebook.jpg", "https://ebook.com/file", "PDF", 1.2
# )

# # # Usar la función polimórfica calcular_precio
# # print()
# # print('-----CALCULANDO PRECIO PRODUCTO FISICO-----')
# # print(producto_fisico.calcular_precio())
# # print('---------------------------------')
# # print('-----CALCULANDO PRECIO PRODUCTO DIGITAL-----')
# # print(producto_digital.calcular_precio())

# print("----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES----")
# print()
# print("----PRODUCTO FISICO----")
# print()
# producto_fisico.price = 10.0
# print(producto_fisico.price)
# print()
# print("----PRODUCTO DIGITAL----")
# print()
# producto_digital.price = -78.34
# print(producto_digital.price)
# payment_method = PaymentMethod(
#      1, 'Credit Card', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
# )
# client = Client(
#     1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01', '123 Main St', payment_method, ['Books', 'Electronics']   
# )

# print("----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES DE USUARIOS/CLIENTES----")

# client.email = 'estonoesunemail.com'

# print(client.email)

# inventario_fisico = PhysicalInventoryManager()
# inventario_digital = DigitalInventoryManager()

#     # Gestionar inventario físico
# inventario_fisico.addProduct("Silla", 10)
# inventario_fisico.updateStock("Silla", 15)
# inventario_fisico.deleteProduct("Silla")

#     # Gestionar inventario digital
# inventario_digital.addProduct("Licencia de software", 100)
# inventario_digital.updateStock("Licencia de software", 120)
# inventario_digital.deleteProduct("Licencia de software")

def globalPaymentProcessor(procesador: PaymentProcess, monto: float) -> None:
    referencia = procesador.startPayment(monto)
    print(f"Referencia generada: {referencia}")

    if procesador.verifyPayment(referencia):
        resultado = procesador.confirmPayment(referencia)
        print(resultado)
    else:
        print("El pago no pudo ser verificado.")
        
# Procesar pago con tarjeta
print("=== Pago con Tarjeta ===")
procesador_tarjeta = CardPayment()
globalPaymentProcessor(procesador_tarjeta, 150.75)

    # Procesar pago con PayPal
print("\n=== Pago con PayPal ===")
procesador_paypal = PaypalPayment()
globalPaymentProcessor(procesador_paypal, 200.50)






