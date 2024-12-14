# Sistema de e-Commerce

## Índice
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Funcionalidades Clave](#funcionalidades-clave)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Comandos](#comandos)
6. [Configurar MongoDB](#configurar-mongodb)
7. [Ejecutar la aplicación](#ejecutar-la-aplicación)
8. [Herencia](#herencia)
9. [Implementación de polimorfismo](#implementación-de-polimorfismo)
10. [Sobrecarga de Métodos](#sobrecarga-de-métodos)
11. [Sobreescritura de Métodos](#sobreescritura-de-métodos)
12. [Abstracción](#abstracción)
13. [Encapsulamiento](#encapsulamiento)
14. [Implementación de Interfaces y Clases Abstractas](#implementación-de-interfaces-y-clases-abstractas)
15. [Uso de Interfaces para Procesos de Pago](#uso-de-interfaces-para-procesos-de-pago)
16. [Singleton para Gestión de Configuración](#singleton-para-gestión-de-configuración)
17. [Factory para Creación de Productos o Usuarios](#factory-para-creación-de-productos-o-usuarios)
18. [Observer para Notificaciones](#observer-para-notificaciones)
19. [Manejo de Excepciones](#manejo-de-excepciones)
20. [Pruebas Unitarias](#pruebas-unitarias)

## Descripción del Proyecto

Este proyecto es una **aplicación de escritorio de e-Commerce** desarrollada en Python con una interfaz gráfica en **PyQt5**. La aplicación permite a los usuarios navegar por un catálogo de productos, gestionar su carrito de compras y realizar pedidos en línea. Además, cuenta con un sistema de gestión de usuarios donde se diferencian los roles de cliente y administrador. Los administradores pueden agregar, editar y eliminar productos, gestionar el inventario y verificar el estado de los pedidos.

### Funcionalidades Clave

- **Registro e Inicio de Sesión de Usuarios**: Incluye autenticación segura, con diferenciación de roles entre clientes y administradores.
- **Catálogo de Productos**: Visualización y búsqueda de productos, organizados por categorías.
- **Carrito de Compras**: Permite a los usuarios agregar y gestionar productos antes de realizar un pedido.
- **Gestión de Pedidos**: Controla el flujo de los pedidos desde la confirmación hasta la entrega.
- **Roles de Usuario**: Los administradores pueden gestionar productos, inventario y órdenes.

## Tecnologías Utilizadas

### Lenguaje de Programación
- **Python**: Lenguaje principal utilizado para el desarrollo de toda la aplicación.

### Interfaz Gráfica
- **PyQt5**: Biblioteca para la creación de una interfaz gráfica de usuario (GUI) robusta y de fácil uso.

### Base de Datos
- **MongoDB**: Base de datos NoSQL para almacenar información de productos, usuarios y pedidos. Su flexibilidad permite manejar datos no estructurados y facilita el escalado de la aplicación.

### Herramientas Adicionales
- **GitHub**: Control de versiones y colaboración en el proyecto.
- **Virtualenv**: Aislamiento del entorno de desarrollo en Python para la gestión de dependencias.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

```plaintext
ecommerce_system/
├── main.py                                     # Archivo principal para ejecutar la aplicación
├── config/                                     # Configuraciones de base de datos y parámetros generales
├── controllers/                                # Lógica de negocio para gestión de productos, usuarios, etc.
├── models/                                     # Clases y estructuras de datos (Producto, Usuario, Pedido)
│   ├── classes_abstraction_interfaces/         # Clases relacionadas con el tema de Abstracción e Interfaces
|   |   ├── card_payment.py                     # Clase Proceso de Pago por Tarjeta, implementa interfaz PaymentProcess (Proceso de Pago)
|   |   ├── digital_inventory_manager.py        # Clase Gestor de Inventario Digital, hereda clase abstracta InventoryManager (Gestor de Inventario)
|   |   ├── inventory_manager.py                # Clase abstracta InventoryManager (Gestor de Inventario)
|   |   ├── payment_process.py                  # Clase interfaz PaymentProcess (Proceso de Pago)
|   |   ├── paypal_payment.py                   # Clase Proceso de Pago por Paypal, implementa interfaz PaymentProcess (Proceso de Pago)
|   |   ├── physical_inventory_manager.py       # Clase Gestor de Inventario Físico, hereda clase abstracta InventoryManager (Gestor de Inventario)
|   ├── classes_exception/
|   |   ├── failed_paid_exception.py            # Clase Excepción para Pago Fallido
|   |   ├── insufficent_inventory_exception.py  # Clase Excepción para Inventario Insuficiente
|   |   ├── invalid_category_exception.py       # Clase Excepción para Categoría Inválida
|   |   ├── user_not_authorized_exception.py    # Clase Excepción para Usuario no Autorizado
│   ├── classes_pattern_factory/
|   |   ├── entity_factory.py                   # Clase Fábrica de Entidades (EntityFactory)
|   ├── classes_pattern_observer/
|   |   ├── inventory_manage_interface.py       # Clase Interfaz Gestion de Inventario (InventoryManageInterface)
|   |   ├── observer_cls.py                     # Función para decorador/anotador @observer_cls
|   |   ├── subject.py                          # Clase Subject para registrar el sujeto del observador, usando WeakSet de Python para esta tarea
|   |   ├── user_interface.py                   # Clase Interfaz Usuario (UserInterface)
│   ├── classes_pattern_singleton/
|   |   ├── decorators.py                       # Script para declaración de decoradores personalizados (se implementa la función singleton como decorador a usar)
|   |   ├── system_configuration.py             # Clase SystemConfiguration (Configuración de Sistema), definida usando el decorador/anotador @singleton
│   ├── classes_poo/
│   │   ├── administrator.py                    # Clase Administrator (hereda de User)
│   │   ├── category.py                         # Clase Category
│   │   ├── client.py                           # Clase Client (hereda de User)
|   │   ├── digital_product.py                  # Clase DigitalProduct (hereda de Product)
|   │   ├── order.py                            # Clase Order
|   │   ├── payment.py                          # Clase Payment
|   │   ├── physical_product.py                 # Clase PhysicalProduct (hereda de Product)
|   │   ├── product.py                          # Clase Product
|   │   ├── role.py                             # Clase Role
|   │   ├── shopping_cart.py                    # Clase Shopping Cart
|   │   └── user.py                             # Clase User
├── requirements.txt                            # Listado de dependencias del proyecto
├── tests/                                      # Archivos de tests unitarios
|   ├── .coverage                               # Archivo generado de cobertura al ejecutar comando
|   ├── test_category.py                        # Archivo de test para Categoría (Category)
|   ├── test_product.py                         # Archivo de test para Producto (Product and childs)
|   ├── test_shopping_cart.py                   # Archivo de test para Carro de Compra (Shopping Cart)
|   ├── test_user.py                            # Archivo de test para Usuario (User)
├── views/                                      # Interfaces gráficas de PyQt5
└── README.md                                   # Documentación del proyecto
```

### Comandos
- **Clonar el repositorio**: 
```
git clone https://github.com/usuario/ecommerce_system.git
```
- **Crear y activar un entorno virtual**: 
```
python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

- **Instalar las dependencias**: 
```
pip install -r requirements.txt
```

### Configurar MongoDB
- Asegurarse de tener MongoDB instalado y en ejecución.
- Crear una base de datos y colecciones necesarias (users, products, orders) para el sistema.
- Configurar la conexión a MongoDB en el archivo de configuración:
```
config/db_config.py
```

### Ejecutar la aplicación
```
python main.py
```

### Desafíos y Soluciones
- **Gestión de Datos entre Interfaces**:
Uno de los principales desafíos fue mantener la coherencia de los datos entre las diferentes interfaces de usuario en PyQt5. Para solucionarlo, se implementarán controladores específicos para manejar los eventos y las actualizaciones de los datos en tiempo real.
Integración de PyQt5 con MongoDB: Se optimizará la conexión y las consultas de MongoDB para mejorar el rendimiento en tiempo real. El uso de índices en campos frecuentes como product_id y user_id ayudará a mejorar la velocidad de las consultas.
Modularización y Estructuración: Se dividirá la lógica de negocio y la visualización en diferentes módulos para mejorar la mantenibilidad y escalabilidad del proyecto.

### Herencia
- **Clase Product**:
Se tiene la clase ```Product``` de la cual heredan: ```DigitalProduct``` y ```PhysicalProduct```.
El ejemplo de definición de las clases se observa:
```
class Product:
    product_id: int               # ID único del producto
    name: str                     # Nombre del producto
    description: str              # Descripción del producto
    price: float                  # Precio unitario
    stock: int                    # Cantidad disponible en inventario
    category: Category            # Categoría del producto
    image_url: str                # URL de la imagen del producto

    def __init__(self, product_id, name, description, price, stock, category, image_url):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.image_url = image_url

...

class DigitalProduct(Product):
    file_url: str    # URL
    format: str      # Formato
    size: float      # Tamano

    def __init__(self, product_id, name, description, price, stock, category, image_url, file_url, format, size):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.file_url = file_url
        self.format = format
        self.size = size

    ...

class PhysicalProduct(Product):
    weight: float    # Peso
    height: float    # Alto
    width: float     # Ancho
    depth: float     # Profundidad

    def __init__(self, product_id, name, description, price, stock, category, image_url, weight, height, width, depth):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.weight = weight
        self.height = height
        self.width = width
        self.depth = depth
```
Para explicar cómo Python implementa la herencia, en los ejemplos anteriores, luego que se declara la clase, se observa entre paréntesis el nombre de la clase padre ```Product```, así se especifica que estas clases hijas están heredando de esa clase. Luego en el constructor con el método ```super()```, se llama al constructor de la clase padre (en estos casos ```Product```) y luego se asignan los valores a los atributos de estas clases hijas, pasados como parámetros por el constructor, que en Python en constructor de cada clase se define como el método ```__init__(self)```, donde el ```self``` representa que se está haciendo referencia a la instancia actual de una clase. 

- **Clase User**:

Exactamente lo mismo sucede para las clases ```Administrator``` y ```Client``` que están heredando de ```User```:

```
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

...

class Administrator(User):
    list_promotions: list[str]    # Lista de promociones
    
    def __init__(self, user_id, username, email, password, phone, role, registration_date, list_promotions):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.list_promotions = list_promotions
    
    def manage_inventory(self):
        return 'Inventory managed'


...

class Client(User):
    address: str                            # Dirección de envío del cliente
    payment_methods: list[PaymentMethod]    # Lista de métodos de pago asociados al cliente
    preferences: list[str]                  # Lista de preferencias del cliente
    
    def __init__(self, user_id, username, email, password, phone, role, registration_date, address, payment_methods,preferences):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.address = address
        self.payment_methods = payment_methods
        self.preferences = preferences

```

### Implementación de polimorfismo
- **main.py**:
Se puede observar en el archivo ```main.py``` como se implementa el método:
```
def mostrar_detalles_producto(producto: Product)
      print(producto.mostrar_detalle())
```
Dicho método recibe como argumento un ```Product``` que puede ser genérico (de cualquiera de los tipos definidos), al invocar el método tal como ocurre en este archivo ```main.py```:
```
# Crear instancias con todos los argumentos
producto_fisico = PhysicalProduct(
    1, "Laptop", "Laptop física de alta calidad", 1000.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
)

producto_digital = DigitalProduct(
    2, "E-Book", "E-Book de programación en Python", 20.0, 100, "Libros", "https://example.com/ebook.jpg", "https://ebook.com/file", "PDF", 1.2
)

# Usar la función polimórfica
print()
print('-----MOSTRANDO EJEMPLO DE POLIMORFISMO Y SOBREESCRITURA DE METODOS-----')
mostrar_detalles_producto(producto_fisico)  # Llama a PhysicalProduct.mostrarDetalle()
print('---------------------------------')
mostrar_detalles_producto(producto_digital) # Llama a DigitalProduct.mostrarDetalle()
print()
```
Se puede observar como recibe cualquiera de estos dos tipos de productos y el resultado mostrado en consola sería:

```
-----MOSTRANDO EJEMPLO DE POLIMORFISMO Y SOBREESCRITURA DE METODOS-----
Producto Fisico: 
ID: 1 
Nombre: Laptop 
Precio: 1000.0 
Peso: 2.5kg 
Dimensiones: 30x20x5cm
---------------------------------
Producto Digital: 
ID: 2 
Nombre: E-Book 
Precio: 20.0 
URL del archivo: https://ebook.com/file 
Formato: PDF 
Tamaño: 1.2MB
```

Como se puede observar, en Python como lenguaje orientado a objetos, el polimorfismo tiene un comportamiento exactamente igual a cualquier otro lenguaje con este mismo paradigma.

### Sobrecarga de Métodos
- **Clase Product**:

La sobrecarga de métodos en Python se implementa usando el decorador ```@singledispatchmethod``` de la librería ```functools```, solo se tiene que importar:
```from functools import singledispatchmethod```.

Este decorador permite definir múltiples versiones de un método basándose en los tipos de los argumentos.
El método base se define como el comportamiento por defecto (cuando no hay coincidencia de tipos).

El método base ```agregar_producto```, si no se encuentra una versión registrada para los argumentos proporcionados, lanza un error ```NotImplementedError```.

```
class ShoppingCart:
    ...
        
    @singledispatchmethod
    def agregar_producto(self, producto):
        """Método base (default) para agregar productos."""
        raise NotImplementedError("Tipo no soportado para agregarProducto.")

    @agregar_producto.register
    def _(self, producto: Product):
        """Agregar un producto por objeto Producto."""
        self.products.append(producto)
        print(f"Producto '{producto.name}' agregado al carrito.")

    @agregar_producto.register
    def _(self, product_id: int, name: str):
        """Agregar un producto por ID y nombre."""
        producto = Product(product_id, name, 0.0)  
        self.products.append(producto)
        print(f"Producto con ID {product_id} y nombre '{name}' agregado al carrito.")

    @agregar_producto.register
    def _(self, name: str, price: float):
        """Agregar un producto por nombre y precio."""
        producto = Product(len(self.products) + 1, name, price)
        self.products.append(producto)
        print(f"Producto '{name}' con precio {price} agregado al carrito.")
```
Se usa la palabra reservada ```register``` para registrar el método como un comportamiento del método original ```agregar_producto``` y carece de nombre, solo se denota con el guión bajo (```_```) para indicar que usará el mismo nombre, pero cada definición con diferentes argumentos.

Su implementación en el archivo ```main.py```:

```
print('-----MOSTRANDO EJEMPLO DE SOBRECARGA DE METODOS-----')
payment_method = PaymentMethod(
    1, 'Credit Card', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
)
client = Client(
    1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01', '123 Main St', payment_method, ['Books', 'Electronics']   
)
carrito = ShoppingCart(1, client, [], 0.0)

# Sobrecarga en acción
carrito.agregar_producto(producto_fisico)  # Agregar por objeto
carrito.agregar_producto(3, "Producto Temporal")  # Agregar por ID y nombre
carrito.agregar_producto("Producto Genérico", 50.0)  # Agregar por nombre y precio
print()

# Ver contenido del carrito
for producto in carrito.products:
    print(producto.mostrar_detalle())
    print()
```

Se puede observar la salida en el archivo ```main.py```:

```
-----MOSTRANDO EJEMPLO DE SOBRECARGA DE METODOS-----
Producto 'Laptop' agregado al carrito.
Producto con ID 3 y nombre 'Producto Temporal' agregado al carrito.
Producto 'Producto Genérico' con precio 50.0 agregado al carrito.

Producto Fisico: 
ID: 1 
Nombre: Laptop 
Precio: 1000.0 
Peso: 2.5kg 
Dimensiones: 30x20x5cm

ID: 3 
Nombre: Producto Temporal 
Precio: None

ID: 3 
Nombre: Producto Genérico 
Precio: None
```

### Sobreescritura de Métodos
- **Clase Product, DigitalProduct y PhysicalProduct**:
Argumentando lo que se planteó en el epígrafe de __Implementación de polimorfismo__, se define el método:
```
def mostrar_detalles_producto(producto: Product)
      print(producto.mostrar_detalle())
```
Que el mismo de acuerdo al tipo de producto, llamará su método redefinido específicamente para la clase de esta instancia, como se puede observar para cada una de las clases:

Clase Padre:

```
class Product:
    ...
    def mostrar_detalle(self) -> str:
        """Método concreto en la clase base."""
        return f"ID: {self.product_id} \nNombre: {self.name} \nPrecio: {self.price}"
```
Clases Hijas:
```
class DigitalProduct(Product):
    ...
    def mostrar_detalle(self) -> str:
        """Extiende el método de la clase base con detalles específicos."""
        return f"Producto Digital: \n{super().mostrar_detalle()} \nURL del archivo: {self.file_url} \nFormato: {self.format} \nTamaño: {self.size}MB"
```

```
class PhysicalProduct(Product):
    ...
    def mostrar_detalle(self) -> str:
        """Extiende el método de la clase base con detalles específicos."""
        return f"Producto Fisico: \n{super().mostrar_detalle()} \nPeso: {self.weight}kg \nDimensiones: {self.height}x{self.width}x{self.depth}cm"
```
Y el resultado se pudo ver en el epígrafe de __Implementación de polimorfismo__, donde solo recibiendo el producto, automáticamente el lenguaje reconoce qué método invocar de la respectiva clase de la instancia.

### Abstracción
- **Clase Product, DigitalProduct y PhysicalProduct**:

Las clases abstractas en Python son clases que actúan como plantillas para otras clases. No pueden ser instanciadas directamente y están destinadas a ser heredadas. Se utilizan para definir métodos que deben ser implementados obligatoriamente por las clases derivadas.

Python proporciona soporte para clases abstractas a través del módulo ```abc (Abstract Base Classes)```, que incluye el decorador ```@abstractmethod``` y la clase base ```ABC```.

Un ejemplo de error:
```
-----MOSTRANDO EJEMPLO DE SOBRECARGA DE METODOS-----
Producto 'Laptop' agregado al carrito.
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 61, in <module>
    carrito.agregar_producto(3, "Producto Temporal")  # Agregar por ID y nombre
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/functools.py", line 946, in _method
    return method.__get__(obj, cls)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/shopping_cart.py", line 32, in _
    producto = Product(product_id, name, 0.0)  
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class Product without an implementation for abstract method 'calcular_precio'
```

No se puede instanciar la clase ```Product``` porque es abstracta:

```
from abc import ABC, abstractmethod

class Product(ABC):
    ...
    @abstractmethod
    def calcular_precio(self) -> float:
        """Método abstracto que debe ser implementado por las subclases."""
        pass
```

En este caso se definió el método ```calcular_precio(self) -> float``` como abstracto. Se redifinió en cada una de las clases hijas:
```
class DigitalProduct(Product):
    ...
    def calcular_precio(self) -> float:
        return self.price * 1.07
```
```
class PhysicalProduct(Product):
    ...
    def calcular_precio(self) -> float:
        return self.price * 1.19
```

A continuación se mostrará el resultado de dos tipos de productos diferentes, con el mismo atributo ```price```, y el valor de ```calcular_precio()``` es diferente:

```
# Usar la función polimórfica calcular_precio
producto_fisico = PhysicalProduct(
    1, "Laptop", "Laptop física de alta calidad", 20.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
)

producto_digital = DigitalProduct(
    2, "E-Book", "E-Book de programación en Python", 20.0, 100, "Libros", "https://example.com/ebook.jpg", "https://ebook.com/file", "PDF", 1.2
)
print()
print('-----CALCULANDO PRECIO PRODUCTO FISICO-----')
print(producto_fisico.calcular_precio())
print('---------------------------------')
print('-----CALCULANDO PRECIO PRODUCTO DIGITAL-----')
print(producto_digital.calcular_precio())
```

El resultado para dos tipos de productos diferentes con el mismo ```price```:
```
-----CALCULANDO PRECIO PRODUCTO FISICO-----
23.8
---------------------------------
-----CALCULANDO PRECIO PRODUCTO DIGITAL-----
21.4
(venv) rcglezreyes@MacBookAir project_poo % 
```

## Encapsulamiento
En Python, el encapsulamiento se implementa mediante convenciones de nombres y modificadores de acceso.
Niveles de Acceso en Python
Python no tiene modificadores de acceso explícitos como private, protected, y public que encontramos en otros lenguajes como Java o C++. Sin embargo, se utilizan convenciones de nombres para simular estos niveles:

**Público (public):**

Atributos y métodos accesibles desde cualquier parte del código.
No se utiliza ningún prefijo especial.
Ejemplo: ```self.nombre```.

**Protegido (protected):**

Atributos y métodos que no deberían ser accedidos directamente fuera de la clase o de sus subclases.
Usan un guion bajo ```(_)``` como prefijo.
Ejemplo: ```self._nombre```.

**Privado (private):**

Atributos y métodos no accesibles directamente desde fuera de la clase.
Usan dos guiones bajos ```(__)``` como prefijo.
Ejemplo: ```self.__nombre```.

El uso de la anotación ```@property``` permite crear atributos controlados, que parecen públicos pero están protegidos mediante métodos ```getter``` y ```setter```.

**Clase Product:**
```
class Product(ABC):
    ...
    def __init__(self, product_id=None, name=None, description=None, price=None, stock=None, category=None, image_url=None):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__image_url = image_url
    
    @property
    def product_id(self) -> int:
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id: int) -> None:
        self.__product_id = product_id
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, price: float) -> None:
        if price < 0:
            raise ValueError('El precio no puede ser negativo.')
        else:
            self.__price = price
    ...
```
Se definen los atributos como privados con doble guion bajo, y se implementan getters y setters para los atributos. En el caso del ```price``` se incluye una validación si el valor es negativo. El ejemplo:

```
producto_fisico = PhysicalProduct(
    1, "Laptop", "Laptop física de alta calidad", 20.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
)

producto_digital = DigitalProduct(
    2, "E-Book", "E-Book de programación en Python", 20.0, 100, "Libros", "https://example.com/ebook.jpg", "https://ebook.com/file", "PDF", 1.2
)

# # Usar la función polimórfica calcular_precio
# print()
# print('-----CALCULANDO PRECIO PRODUCTO FISICO-----')
# print(producto_fisico.calcular_precio())
# print('---------------------------------')
# print('-----CALCULANDO PRECIO PRODUCTO DIGITAL-----')
# print(producto_digital.calcular_precio())

print("----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES----")
print()
print("----PRODUCTO FISICO----")
print()
producto_fisico.price = 10.0
print(producto_fisico.price)
print()
print("----PRODUCTO DIGITAL----")
print()
producto_digital.price = -78.34
print(producto_digital.price)
```
El resultado:
```
----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES----

----PRODUCTO FISICO----

10.0

----PRODUCTO DIGITAL----

Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 95, in <module>
    producto_digital.price = -78.34
    ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/product.py", line 39, in price
    raise ValueError('El precio no puede ser negativo.')
ValueError: El precio no puede ser negativo.
```

**Clase User:**

Para esta clase se implementará en el ```setter``` del ```email``` una validación usando expresión regular:

```
import re

class User:
    ...
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
```

La implementación:

```
payment_method = PaymentMethod(
     1, 'Credit Card', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
)
client = Client(
    1, 'user', 'user@gmailcom', '1234', '1234567890', 'client', '2021-01-01', '123 Main St', payment_method, ['Books', 'Electronics']   
)

print("----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES DE USUARIOS/CLIENTES----")

client.email = 'estonoesunemail.com'

print(client.email)
```

El resultado:
```
----MOSTRANDO GETTERS, SETTERS Y VALIDACIONES DE USUARIOS/CLIENTES----
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 106, in <module>
    client.email = 'estonoesunemail.com'
    ^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/user.py", line 32, in email
    raise ValueError('El correo electrónico debe ser válido.')
ValueError: El correo electrónico debe ser válido.
```

## Implementación de Interfaces y Clases Abstractas
En Python, usar el módulo abc permite definir clases abstractas y métodos abstractos. Para una clase  abstracta, todos sus metodos deben llevan el decorador ```@abstractmethod``` de la libreria ABC (```from abc import ABC, abstractmethod```):

```
from abc import ABC, abstractmethod

class InventoryManager(ABC):
    @abstractmethod
    def add_product(self, product, quantity):
        """Añadir un producto al inventario"""
        pass

    @abstractmethod
    def delete_product(self, product):
        """Eliminar un producto del inventario"""
        pass

    @abstractmethod
    def update_stock(self, product, quantity):
        """Actualizar el stock de un producto"""
        pass
```

En este caso: 
Clase abstracta (```InventoryManager```):
Define los métodos obligatorios que las clases concretas deben implementar.
Utiliza el decorador @abstractmethod para garantizar que cualquier clase hija implemente estos métodos.

Clases concretas (```PhysicalInventoryManager``` y ```DigitalInventoryManager```):

Proporcionan implementaciones específicas para cada tipo de inventario.
Utilizan diccionarios (```self.inventory```) para gestionar los productos y sus cantidades.

```
class PhysicalInventoryManager(InventoryManager):
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        ...

    def delete_product(self, product):
        ...

    def update_stock(self, product, quantity):
        ...
```

```
class DigitalInventoryManager(InventoryManager):
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        ...

    def delete_product(self, product):
        ...

    def update_stock(self, product, quantity):
        ...
```
Veamos un ejemplo:
```
nventario_fisico = PhysicalInventoryManager()
inventario_digital = DigitalInventoryManager()

    # Gestionar inventario físico
inventario_fisico.add_product("Silla", 10)
inventario_fisico.update_stock("Silla", 15)
inventario_fisico.delete_product("Silla")

    # Gestionar inventario digital
inventario_digital.add_product("Licencia de software", 100)
inventario_digital.update_stock("Licencia de software", 120)
inventario_digital.delete_product("Licencia de software")
```
Resultado:
```
Producto físico añadido: Silla (10)
Stock actualizado para Silla: 15
Producto físico eliminado: Silla
Producto digital añadido: Licencia de software (100)
Stock actualizado para Licencia de software: 120
Producto digital eliminado: Licencia de software
(venv) rcglezreyes@MacBookAir project_poo % 
```
Ahora probemos no implementando un método a ver quê respuesta se obtiene:
En la clase ```PhysicalInventoryManager``` comentamos el último método:
```
# def update_stock(self, product, quantity):
#     if product in self.inventory:
#         self.inventory[product] = quantity
#         print(f"Stock actualizado para {product}: {quantity}")
#     else:
#         print(f"Producto {product} no encontrado en el inventario físico.")
```
El resultado:
```
zreyes/Documents/maestria/OOP/project_poo/main.py
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 112, in <module>
    inventario_fisico = PhysicalInventoryManager()
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class PhysicalInventoryManager without an implementation for abstract method 'update_stock'
(venv) rcglezreyes@MacBookAir project_poo % 
```
Cada clase Concreta debe implementar exactamente todos los métodos definidos como abstractos en la clase Abstracta

## Uso de Interfaces para Procesos de Pago

El módulo ```typing``` de Python, proporciona ```Protocol```, que permite definir interfaces sin necesidad de clases abstractas, como lo hacen otros lenguajes como Java con la palabra reservada ```interface```. El ejemplo:
```
from typing import Protocol

class PaymentProcess(Protocol):
    def start_payment(self, monto: float) -> str:
        """Inicia el proceso de pago."""
        ...

    def verify_payment(self, referencia: str) -> bool:
        """Verifica el estado del pago."""
        ...

    def confirm_payment(self, referencia: str) -> str:
        """Confirma que el pago se ha completado."""
        ...
```
En este caso, sí se incluyen realmente los 3 puntos suspensivos para denotar que ese método será implementado en alguna clase que usará la clase original como referencia, en otra palabras, la implementará.

Las clases que implementan las interface, lo que hacen es referenciarla como argumento, como si hereraran de ella, pero el intérprete de Python sabe cuando se trata de herencia y cuando se trata de implementación de interface, con el simple hecho del origen y definición de la clase:

```
from models.payment_process import PaymentProcess

class CardPayment(PaymentProcess):
    def start_payment(self, amount: float) -> str:
        print(f"Iniciando pago con tarjeta por ${amount:.2f}")
        return "ref-tarjeta-123"

    def verify_payment(self, reference: str) -> bool:
        print(f"Verificando pago con referencia {reference}")
        return True

    def confirm_payment(self, reference: str) -> str:
        print(f"Confirmando pago con tarjeta con referencia {reference}")
        return "Pago con tarjeta confirmado"
```

```
from models.payment_process import PaymentProcess

class PaypalPayment(PaymentProcess):
    def start_payment(self, amount: float) -> str:
        print(f"Iniciando pago con PayPal por ${amount:.2f}")
        return "ref-tarjeta-123"

    def verify_payment(self, reference: str) -> bool:
        print(f"Verificando pago en PayPal con referencia {reference}")
        return True

    def confirm_payment(self, reference: str) -> str:
        print(f"Confirmando pago en PayPal con referencia {reference}")
        return "Pago con tarjeta confirmado"
```

Vemos un ejemplo y el resultado:

```
def globalPaymentProcessor(procesador: PaymentProcess, monto: float) -> None:
    referencia = procesador.start_payment(monto)
    print(f"Referencia generada: {referencia}")

    if procesador.verify_payment(referencia):
        resultado = procesador.confirm_payment(referencia)
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
```
En este caso se recibe una interface en el método para procesar, y hay dos instancias que implementan esa interface que han sido definidas, veremos los resultados si se corresponden con sus respectivas implementaciones:

```
reyes/Documents/maestria/OOP/project_poo/main.py
=== Pago con Tarjeta ===
Iniciando pago con tarjeta por $150.75
Referencia generada: ref-tarjeta-123
Verificando pago con referencia ref-tarjeta-123
Confirmando pago con tarjeta con referencia ref-tarjeta-123
Pago con tarjeta confirmado

=== Pago con PayPal ===
Iniciando pago con PayPal por $200.50
Referencia generada: ref-tarjeta-123
Verificando pago en PayPal con referencia ref-tarjeta-123
Confirmando pago en PayPal con referencia ref-tarjeta-123
Pago con tarjeta confirmado
(venv) rcglezreyes@MacBookAir project_poo % 
```

Como se observa, ha sido de esta forma, usando su método reimplementado específico para cada clase. Aqui se mezcla el principio de Polimorfismo pues el método ```globalPaymentProcessor``` toma como parámetro cualquier objeto que implemente la interfaz ```PaymentProcess```, permitiendo procesar pagos de diferentes maneras sin modificar el código base.

## Singleton para Gestión de Configuración

Una manera de implementar el patrón ```Singleton``` en Python es mediante un decorador. Decorador ```singleton```:
```
def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance

```
Es una simple función que recible un parámetro de tipo class (```cls```)

Declaramos la clase ```SystemConfiguration``` importando el decorador ```@singleton```:
```
from decorators import singleton

@singleton
class SystemConfiguration:
    def __init__(self, db_url=None, ui_config=None):
        ...

    def show_configuration(self):
        ...
```

Ahora demostraremos que sigue este patrón ```singleton```. Declaramos su uso en el main:

```
config1 = SystemConfiguration(db_url="postgres://prod:5432/ecommerce", ui_config={"theme": "dark"})
print("Configuración inicial:", config1.show_configuration())

# Segunda instancia
config2 = SystemConfiguration(db_url="postgres://test:5432/ecommerce", ui_config={"theme": "light"})
print("Configuración al intentar otra instancia:", config2.show_configuration())

# Verificar que ambas instancias son la misma
print("¿Son la misma instancia?", config1 is config2)
```

El resultado:
```
(venv) rcglezreyes@MacBookAir project_poo % /Users/rcglezreyes/Documents/maestria/OOP/project_poo/venv/bin/python /Users/rcgle
zreyes/Documents/maestria/OOP/project_poo/main.py
Configuración inicial: {'db_url': 'postgres://prod:5432/ecommerce', 'ui_config': {'theme': 'dark'}}
Configuración al intentar otra instancia: {'db_url': 'postgres://prod:5432/ecommerce', 'ui_config': {'theme': 'dark'}}
¿Son la misma instancia? True
(venv) rcglezreyes@MacBookAir project_poo % 
```

Probemos otro valor para ```config2```:
```
config2 = SystemConfiguration(db_url="postgres://test:5432/dd_invoices", ui_config={"theme": "light"})
```
El resultado:
```
Configuración inicial: {'db_url': 'postgres://prod:5432/ecommerce', 'ui_config': {'theme': 'dark'}}
**Configuración al intentar otra instancia: {'db_url': 'postgres://prod:5432/ecommerce', 'ui_config': {'theme': 'dark'}}**
¿Son la misma instancia? True
```
No reasigna el nuevo valor de ```db_url```, lo que demuestra que sigue el patron único (```singleton```)

## Factory para Creación de Productos o Usuarios

El patrón ```Factory``` es ideal para abstraer la creación de objetos. A continuación un ejemplo de una clase ```EntityFactory``` que sigue este patrón y puede crear instancias de ```Product``` o ```User```, según el tipo especificado:

```
from models.classes_poo.digital_product import DigitalProduct
from models.classes_poo.physical_product import PhysicalProduct
from models.classes_poo.client import Client
from models.classes_poo.administrator import Administrator

class EntityFactory:
    @staticmethod
    def create_entity(type, **kwargs):
        if type == "producto_digital":
            return DigitalProduct(name=kwargs["name"], price=kwargs["price"])
        elif type == "producto_fisico":
            return PhysicalProduct(name=kwargs["name"], price=kwargs["price"])
        elif type == "usuario_cliente":
            return Client(username=kwargs["username"], email=kwargs["email"])
        elif type == "usuario_administrador":
            return Administrator(username=kwargs["username"], email=kwargs["email"])
        else:
            raise ValueError(f"Tipo de entidad no reconocido: {type}")
```
Probamos en el ```main.py```:
```
# Creando Products
producto_digital = EntityFactory.create_entity(
    "producto_digital", name="eBook de Python", price=9.99
)
producto_fisico = EntityFactory.create_entity(
    "producto_fisico", name="Laptop", price=1200.00
)

# Creando Users
usuario_cliente = EntityFactory.create_entity(
    "usuario_cliente", username="juan.perez", email="juan@example.com"
)
usuario_administrador = EntityFactory.create_entity(
    "usuario_administrador", username="ana.lopez", email="ana@example.com"
)

# Mostrar detalles
print(producto_digital.__str__())
print(producto_fisico.__str__())
print(usuario_cliente.__str__())
print(usuario_administrador.__str__())
```

El resultado:
```
(venv) rcglezreyes@MacBookAir project_poo % /Users/rcglezreyes/Documents/maestria/OOP/project_poo/venv/bin/python /Users/rcglezrey
es/Documents/maestria/OOP/project_poo/main.py
 
ID: None 
Nombre: eBook de Python 
Descripcion: None 
Precio: 9.99, Stock: None, Categoria: None, Imagen URL: None 
File URL: None 
Format: None 
Size: None
 
ID: None 
Nombre: Laptop 
Descripcion: None 
Precio: 1200.0, Stock: None, Categoria: None, Imagen URL: None 
Weight: None 
Height: None 
Width: None 
Depth: None
 
User ID: None 
Username: juan.perez 
Email: juan@example.com 
Phone: None 
Role: None 
Registration Date: None 
Address: None 
Payment methods:[None] 
Preferences: None
 
User ID: None 
Username: ana.lopez 
Email: ana@example.com 
Phone: None 
Role: None 
Registration Date: None 
List of promotions: None
(venv) rcglezreyes@MacBookAir project_poo % 
```
**Conclusión:**

Clases base:

```Product``` y ```User``` son clases abstractas con métodos que deben implementarse en las subclases.

Clases derivadas:

```DigitalProduct``` y ```PhysicalProduct``` heredan de ```Product``` y definen el método ```__str__```.

```Client``` y ```Administrator``` heredan de ```User``` y definen el método ```__str__```.

Fábrica (```EntityFactory```):

Proporciona un único punto de acceso para crear objetos. Usa un parámetro ```type``` para decidir qué clase instanciar y los argumentos necesarios (```kwargs```).

Ventajas:

Abstracción: No se necesita preocupar por las clases concretas al crear objetos.
Escalabilidad: Si se necesita agregar nuevos tipos (```type```), solo se añaden casos en la fábrica.

## Observer para Notificaciones

Para implementar el patrón Observer utilizando herramientas integradas de Python, puedes usar el módulo weakref, que incluye una clase llamada WeakKeyDictionary, ideal para mantener referencias débiles a observadores sin evitar que el recolector de basura elimine objetos no utilizados. También se puede usar un decorador para facilitar la suscripción de métodos como observadores.

Creamos la clase ```Subject``` que registre la cola de eventos en su set protegido ```_observers```:
```
from weakref import WeakSet

class Subject:
    def __init__(self):
        self._observers = WeakSet()

    def add_observer(self, observer):
        self._observers.add(observer)

    def delete_observer(self, observer):
        self._observers.discard(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)
```

Creamos el anotador/decorador con un ```subject```:
```
from weakref import WeakSet

class Subject:
    def __init__(self):
        self._observers = WeakSet()

    def add_observer(self, observer):
        self._observers.add(observer)

    def delete_observer(self, observer):
        self._observers.discard(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)
```

Creamos las interfaces que notificarán las actividades de cambio de evento registradas con el anotador:
```
@observer_cls
class InventoryManageInterface:
    def __init__(self, subject):
        self.subject = subject

    def update(self, event):
        print(f"[Gestión de Inventario] Actualizando inventario debido a: {event}")
```

```
@observer_cls
class UserInterface:
    def __init__(self, subject):
        self.subject = subject

    def update(self, event):
        print(f"[Interfaz de Usuario] Notificación recibida: {event}")
```

Tomamos la clase ```Order``` y la ponemos a heredar/implementar de ```Subject``` para que incluya la gestión de cambios de eventos que tiene esta clase y definimos un método en ella llamado ```change_status```:
```
class Order(Subject):
    ...
        
    def change_status(self, nuevo_estado):
        self.status = nuevo_estado
        print(f"Pedido {self.order_id} cambió su estado a {self.status}")
        self.notify_observers(f"Pedido {self.order_id} cambió su estado a {self.status}")
```

Incluimos la prueba en el ```main.py```:

```
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
```

Y el resultado final:
```
(venv) rcglezreyes@MacBookAir project_poo % /Users/rcglezreyes/Documents/maestria/OOP/project_poo/venv/bin/python /Users/rcg
lezreyes/Documents/maestria/OOP/project_poo/main.py
Pedido 101 cambió su estado a Procesando
[Gestión de Inventario] Actualizando inventario debido a: Pedido 101 cambió su estado a Procesando
[Interfaz de Usuario] Notificación recibida: Pedido 101 cambió su estado a Procesando
Pedido 101 cambió su estado a Enviado
[Gestión de Inventario] Actualizando inventario debido a: Pedido 101 cambió su estado a Enviado
[Interfaz de Usuario] Notificación recibida: Pedido 101 cambió su estado a Enviado
Pedido 101 cambió su estado a Entregado
[Gestión de Inventario] Actualizando inventario debido a: Pedido 101 cambió su estado a Entregado
(venv) rcglezreyes@MacBookAir project_poo % 
```

**A modo de conclusión:**

Clase ```Subject```:
Gestiona los observadores usando ```WeakSet``` para evitar mantener referencias fuertes a los objetos observadores. Esto permite que los observadores sean eliminados automáticamente por el recolector de basura.

Decorador ```@observer_cls```:
Añade lógica a las clases decoradas para suscribirse automáticamente al sujeto y eliminarse al ser destruidas.

Observadores concretos (```UserInterface```, ```InventoryManageInterface```):
Decorados con @observador_clase para simplificar su integración con el patrón ```Observer```.

Ventajas del decorador:
Simplifica la lógica de registro de observadores.
Automatiza el manejo de alta y baja de observadores en el sujeto.

Este enfoque aprovecha las herramientas de Python para implementar un sistema de notificaciones robusto, limpio y extensible.


## Manejo de Excepciones

En Python, el manejo de excepciones es un mecanismo que permite controlar errores que ocurren durante la ejecución de un programa, como dividir entre cero o intentar acceder a un archivo inexistente. Esto se logra mediante el uso de bloques de código específicos para capturar y responder a las excepciones.

Conceptos Básicos
1. Excepción: Un evento que interrumpe el flujo normal del programa cuando ocurre un error.
2. Raising (lanzar): Cuando el programa detecta un error, lanza una excepción usando la palabra clave ```raise```.
3. Catching (capturar): El error lanzado puede ser manejado con un bloque ```try-except```.

Para este proyecto se crearon las clases que heredan de ```Exception``` de Python, las mismas están definidas en la carpeta ```models/classes_exception```:

```
class FailedPaidException(Exception):
    """Se lanza cuando ocurre un error en el procesamiento del pago."""
    def __init__(self, mensaje="El pago no pudo ser procesado."):
        super().__init__(mensaje)
```
```
class InsufficentInventoryException(Exception):
    """Se lanza cuando no hay suficiente inventario para completar la compra."""
    def __init__(self, mensaje="Inventario insuficiente para el producto solicitado."):
        super().__init__(mensaje)
```
```
class InvalidCategoryException(Exception):
    """Excepción personalizada para errores en la categoría."""
    def __init__(self, mensaje="Categoría no válida."):
        super().__init__(mensaje)
```
```
class UserNotAuthorizedException(Exception):
    """Se lanza cuando un usuario no autorizado intenta realizar una acción restringida."""
    def __init__(self, mensaje="Usuario no autorizado para realizar esta acción."):
        super().__init__(mensaje)
```

Luego se incluyen las mismas en el resto de clases donde es necesario el uso para la validación y rigurosidad del funcionamiento del sistema:

```
from models.classes_exception.failed_paid_exception import FailedPaidException

class Order(Subject):
    ...
        
    def process_pay(self, product, quantity):
        if self.payment_method.method_name != "tarjeta":
            raise FailedPaidException("El método de pago no es válido. Solo se aceptan tarjetas.")
        product.reduce_stock(quantity)       
        return "Pago procesado exitosamente."

```
```
from models.classes_exception.insufficent_inventory_exception import InsufficentInventoryException
from abc import ABC, abstractmethod

class Product(ABC):
    ...
    
    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise InsufficentInventoryException(
                f"Solo hay {self.stock} unidades disponibles del producto '{self.name}'."
            )
        self.stock -= quantity
```
```
from models.classes_exception.invalid_category_exception import InvalidCategoryException

class Category:
    category_id: int              # ID único de la categoría
    name: str                     # Nombre de la categoría (ej., "Electrónica", "Ropa")
    type_list: list[str]          # Lista de tipos dentro de la categoría (ej., ["Smartphones", "Laptops"])

    def __init__(self, category_id, name, type_list):
        try:
            # Validación de `category_id`
            if not isinstance(category_id, int) or category_id <= 0:
                raise InvalidCategoryException("El category_id debe ser un entero positivo.")
            
            # Validación de `name`
            if not isinstance(name, str) or not name.strip():
                raise InvalidCategoryException("El nombre de la categoría debe ser una cadena no vacía.")
            
            # Validación de `type_list`
            if not isinstance(type_list, list) or not all(isinstance(tipo, str) for tipo in type_list):
                raise InvalidCategoryException("type_list debe ser una lista de cadenas.")
            
            # Asignación de atributos
            self.category_id = category_id
            self.name = name
            self.type_list = type_list

        except InvalidCategoryException as e:
            print(f"Error al crear la categoría: {e}")
            raise

        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            raise
```
```
from models.classes_exception.user_not_authorized_exception import UserNotAuthorizedException

class User:
    ...
    def check_authorization(self):
        if not self.authorized:
            raise UserNotAuthorizedException("El usuario no está autorizado para esta operación.")
        print('Usuario autorizado')
```
Ahora se mostrará el uso de las mismas en la ejecución del proyecto:

Para la ```class Order```:
```
producto_digital = EntityFactory.create_entity(
    "producto_digital", name="eBook de Python", price=9.99
)
payment_method = PaymentMethod(
     1, 'PayPal', {'number' : '1234567890', 'expitation_date' : '2021-01-01'}
)
pedido = Order(order_id=101, status='Pendiente', payment_method=payment_method)
pedido.process_pay(product=producto_digital, quantity=4)
```
Y el resultado:
```
(venv) rcglezreyes@MacBookAir project_poo % /Users/rcglezreyes/Documents/maestria/OOP/project_poo/venv/bin/python /Users/rcglezrey
es/Documents/maestria/OOP/project_poo/main.py
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 193, in <module>
    pedido.process_pay(product=producto_digital, quantity=4)
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/classes_poo/order.py", line 37, in process_pay
    raise FailedPaidException("El método de pago no es válido. Solo se aceptan tarjetas.")
models.classes_exception.failed_paid_exception.FailedPaidException: El método de pago no es válido. Solo se aceptan tarjetas.
(venv) rcglezreyes@MacBookAir project_poo % 
```
En este caso, definimos un método de pago de nombre "PayPal" y en el caso de la excepción, sólo se acepta método de pago de tipo "tarjeta"

Para la clase ```Product```:
```
producto_fisico = PhysicalProduct(
    1, "Laptop", "Laptop física de alta calidad", 20.0, 5, "Electrónica", "https://example.com/laptop.jpg", 2.5, 30, 20, 5
)
producto_fisico.reduce_stock(6)
```
Y el resultado:
```
(venv) rcglezreyes@MacBookAir project_poo % /Users/rcglezreyes/Documents/maestria/OOP/project_poo/venv/bin/python /Users/rcglezrey
es/Documents/maestria/OOP/project_poo/main.py
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 198, in <module>
    producto_fisico.reduce_stock(6)
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/classes_poo/product.py", line 110, in reduce_stock
    raise InsufficentInventoryException(
models.classes_exception.insufficent_inventory_exception.InsufficentInventoryException: Solo hay 5 unidades disponibles del producto 'Laptop'.
(venv) rcglezreyes@MacBookAir project_poo % 
```
En este caso el mensaje está muy bien explicado, pues se creó el Producto con 5 unidades y se está intentando reducir el stock en 6.

Para la clase ```Category``` (dentro del archivo ```models/classes_poo/category.py```), en la misma intentamos el uso de el bloque ```try-catch``` con múltiples excepciones incluidas:

1. Probando con la instancia: ```category = Category('new_cat_01', 'Categoria Especial', ['Especial1', 'Especial2'])```
Resultado:
```
Error al crear la categoría: El category_id debe ser un entero positivo.
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 201, in <module>
    category = Category('new_cat_01', 'Categoria Especial', ['Especial1', 'Especial2'])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/classes_poo/category.py", line 12, in __init__
    raise InvalidCategoryException("El category_id debe ser un entero positivo.")
models.classes_exception.invalid_category_exception.InvalidCategoryException: El category_id debe ser un entero positivo.
```
2. Probando con la instancia: ```category = Category(category_id=5, name='', type_list=[])```
Resultado:
```
Error al crear la categoría: El nombre de la categoría debe ser una cadena no vacía.
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 201, in <module>
    category = Category(category_id=5, name='', type_list=[])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/classes_poo/category.py", line 16, in __init__
    raise InvalidCategoryException("El nombre de la categoría debe ser una cadena no vacía.")
models.classes_exception.invalid_category_exception.InvalidCategoryException: El nombre de la categoría debe ser una cadena no vacía.
```
3. Probando con la instancia: ```category = Category(category_id=5, name='Categoria Especial', type_list=[5, 6])```
Resultado:
```
Error al crear la categoría: type_list debe ser una lista de cadenas.
Traceback (most recent call last):
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/main.py", line 201, in <module>
    category = Category(category_id=5, name='Categoria Especial', type_list=[5, 6])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rcglezreyes/Documents/maestria/OOP/project_poo/models/classes_poo/category.py", line 20, in __init__
    raise InvalidCategoryException("type_list debe ser una lista de cadenas.")
models.classes_exception.invalid_category_exception.InvalidCategoryException: type_list debe ser una lista de cadenas.
```

## Pruebas Unitarias

En Python las pruebas unitarias son un enfoque para probar partes individuales (unidades) de un programa, como funciones, métodos o clases, para asegurarse de que funcionen correctamente de forma aislada.

Librería Usada: ```unittest```
Python incluye la librería estándar unittest para realizar pruebas unitarias. Esta librería proporciona herramientas para:

1. Crear casos de prueba (test cases).
2. Configurar y limpiar el entorno antes y después de cada prueba (```setUp``` y ```tearDown```).
3. Comparar resultados esperados y reales mediante aserciones como ```assertEqual```, ```assertTrue```, etc.

Carpeta ```tests/```

Las pruebas unitarias suelen estar en una carpeta llamada ```tests/```, separada del código fuente.
La carpeta puede incluir un archivo ```__init__.py``` (aunque opcional en versiones recientes de Python) para ser reconocida como un paquete.

En el caso de nuestro proyecto, incluimos 4 archivos (```test_category.py```, ```test_product.py```, ```test_shopping_cart.py``` y ```test_user.py```) dentro de la carpeta ```/tests```, para probar las pruebas unitarias usando la librería ```unittest```:

Para correr los tests por separado:
1. ```test_category.py```: comando: ```python -m unittest tests/test_category.py```
Resultado: 
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
2. ```test_product.py```: comando: ```python -m unittest tests/test_product.py```
Resultado: 
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```
3. ```test_shopping_cart.py```: comando: ```python -m unittest tests/test_shopping_cart.py```
Resultado: 
```
Producto 'Laptop' agregado al carrito.
..Producto 'Laptop' agregado al carrito.
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
4. ```test_user.py```: comando: ```python -m unittest tests/test_user.py```
Resultado: 
```
.Usuario autorizado
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

**Cobertura**

Para la cobertura de los tests en Python, necesitamos tener la librería ```coverage``` que no viene por defecto con el intérprete. Para ello, ejecutamos el comando:
```
pip install coverage
```
Luego de tener instalada nuestra librería, ejecutamos los comandos:
```
coverage run -m unittest discover -s tests
coverage report
```
Donde se le dice que muestre el reporte de cobertura de todos los archivos de tipo ```test``` que están en la carpeta ```tests``` en la raíz del proyecto. 
El resultado:
```
coverage report
.......Producto 'Laptop' agregado al carrito.
..Producto 'Laptop' agregado al carrito.
..Usuario autorizado
...
----------------------------------------------------------------------
Ran 14 tests in 0.008s

OK
Name                                                          Stmts   Miss  Cover
---------------------------------------------------------------------------------
models/classes_exception/insufficent_inventory_exception.py       3      0   100%
models/classes_exception/invalid_category_exception.py            3      1    67%
models/classes_exception/user_not_authorized_exception.py         3      0   100%
models/classes_poo/category.py                                   22      9    59%
models/classes_poo/client.py                                     32      8    75%
models/classes_poo/digital_product.py                            35     10    71%
models/classes_poo/payment_method.py                             10      4    60%
models/classes_poo/product.py                                    83     14    83%
models/classes_poo/role.py                                        8      3    62%
models/classes_poo/shopping_cart.py                              54     12    78%
models/classes_poo/user.py                                       80     16    80%
tests/test_category.py                                           19      1    95%
tests/test_product.py                                            34      1    97%
tests/test_shopping_cart.py                                      32      1    97%
tests/test_user.py                                               27      1    96%
---------------------------------------------------------------------------------
TOTAL                                                           445     81    82%
(venv) rcglezreyes@MacBookAir project_poo % 
```
Lo que indica que tenemos un ```82%``` de cobertura de todo njuestro código en casos de prueba.
