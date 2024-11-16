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
├── main.py                          # Archivo principal para ejecutar la aplicación
├── config/                          # Configuraciones de base de datos y parámetros generales
├── controllers/                     # Lógica de negocio para gestión de productos, usuarios, etc.
├── models/                          # Clases y estructuras de datos (Producto, Usuario, Pedido)
│   ├── administrator.py             # Clase Administrator (hereda de User)
│   ├── category.py                  # Clase Category
│   ├── client.py                    # Clase Client (hereda de User)
│   ├── digital_product.py           # Clase DigitalProduct (hereda de Product)
│   ├── order.py                     # Clase Order
│   ├── payment.py                   # Clase Payment
│   ├── physical_product.py          # Clase PhysicalProduct (hereda de Product)
│   ├── product.py                   # Clase Product
│   ├── role.py                      # Clase Role
│   ├── shopping_cart.py             # Clase Shopping Cart
│   └── user.py                      # Clase User
├── requirements.txt                 # Listado de dependencias del proyecto
├── views/                           # Interfaces gráficas de PyQt5
└── README.md                        # Documentación del proyecto
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

