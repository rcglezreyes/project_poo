from models.classes_poo.user import User
from models.classes_poo.payment_method import PaymentMethod
from models.classes_poo.client import Client
from models.classes_poo.administrator import Administrator
from models.classes_poo.product import Product
from models.classes_poo.physical_product import PhysicalProduct
from models.classes_poo.digital_product import DigitalProduct
from models.classes_poo.shopping_cart import ShoppingCart
from models.classes_poo.category import Category
from models.classes_poo.order import Order
from models.classes_abstraction_interfaces.digital_inventory_manager import DigitalInventoryManager
from models.classes_abstraction_interfaces.physical_inventory_manager import PhysicalInventoryManager
from models.classes_abstraction_interfaces.payment_process import PaymentProcess
from models.classes_abstraction_interfaces.card_payment import CardPayment
from models.classes_abstraction_interfaces.paypal_payment import PaypalPayment
from models.classes_pattern_singleton.system_configuration import SystemConfiguration
from models.classes_pattern_factory.entity_factory import EntityFactory
from models.classes_pattern_observer.user_interface import UserInterface
from models.classes_pattern_observer.inventory_manage_interface import InventoryManageInterface


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
# inventario_fisico.add_product("Silla", 10)
# inventario_fisico.update_stock("Silla", 15)
# inventario_fisico.delete_product("Silla")

#     # Gestionar inventario digital
# inventario_digital.add_product("Licencia de software", 100)
# inventario_digital.update_stock("Licencia de software", 120)
# inventario_digital.delete_product("Licencia de software")

# def globalPaymentProcessor(procesador: PaymentProcess, monto: float) -> None:
#     referencia = procesador.start_payment(monto)
#     print(f"Referencia generada: {referencia}")

#     if procesador.verify_payment(referencia):
#         resultado = procesador.confirm_payment(referencia)
#         print(resultado)
#     else:
#         print("El pago no pudo ser verificado.")
        
# # Procesar pago con tarjeta
# print("=== Pago con Tarjeta ===")
# procesador_tarjeta = CardPayment()
# globalPaymentProcessor(procesador_tarjeta, 150.75)

#     # Procesar pago con PayPal
# print("\n=== Pago con PayPal ===")
# procesador_paypal = PaypalPayment()
# globalPaymentProcessor(procesador_paypal, 200.50)

# config1 = SystemConfiguration(db_url="postgres://prod:5432/ecommerce", ui_config={"theme": "dark"})
# print("Configuración inicial:", config1.show_configuration())

# # Segunda instancia
# config2 = SystemConfiguration(db_url="postgres://test:5432/db_invoices", ui_config={"theme": "light"})
# print("Configuración al intentar otra instancia:", config2.show_configuration())

# # Verificar que ambas instancias son la misma
# print("¿Son la misma instancia?", config1 is config2)

# # Creando Products
# producto_digital = EntityFactory.create_entity(
#     "producto_digital", name="eBook de Python", price=9.99
# )
# producto_fisico = EntityFactory.create_entity(
#     "producto_fisico", name="Laptop", price=1200.00
# )

# # Creando Users
# usuario_cliente = EntityFactory.create_entity(
#     "usuario_cliente", username="juan.perez", email="juan@example.com"
# )
# usuario_administrador = EntityFactory.create_entity(
#     "usuario_administrador", username="ana.lopez", email="ana@example.com"
# )

# # Mostrar detalles
# print(producto_digital.__str__())
# print(producto_fisico.__str__())
# print(usuario_cliente.__str__())
# print(usuario_administrador.__str__())

pedido = Order(order_id=101, status='Pendiente')

# Crear observadores (se suscriben automáticamente)
interfaz_usuario = UserInterface(pedido)
gestion_inventario = InventoryManageInterface(pedido)

# Cambiar estado del pedido y notificar observadores
pedido.change_status("Procesando")
pedido.change_status("Enviado")

# Eliminar un observador al destruir el objeto
del interfaz_usuario

# Cambiar estado del pedido nuevamente
pedido.change_status("Entregado")




