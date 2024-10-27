# Sistema de e-Commerce

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
├── app.py                    # Archivo principal para ejecutar la aplicación
├── config/                   # Configuraciones de base de datos y parámetros generales
├── controllers/              # Lógica de negocio para gestión de productos, usuarios, etc.
├── models/                   # Clases y estructuras de datos (Producto, Usuario, Pedido)
│   ├── client.py             # Clase Client (hereda de User)
│   ├── user.py               # Clase User y roles de usuario
│   └── product.py            # Clase Product
├── requirements.txt          # Listado de dependencias del proyecto
├── views/                    # Interfaces gráficas de PyQt5
│   ├── main_window.py        # Ventana principal
│   ├── product_view.py       # Visualización de productos y categorías
│   ├── cart_view.py          # Visualización del carrito de compras
│   └── order_view.py         # Visualización de órdenes y estado
└── README.md                 # Documentación del proyecto
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
python app.py
```

### Desafíos y Soluciones
- **Gestión de Datos entre Interfaces**:
Uno de los principales desafíos fue mantener la coherencia de los datos entre las diferentes interfaces de usuario en PyQt5. Para solucionarlo, se implementarán controladores específicos para manejar los eventos y las actualizaciones de los datos en tiempo real.
Integración de PyQt5 con MongoDB: Se optimizará la conexión y las consultas de MongoDB para mejorar el rendimiento en tiempo real. El uso de índices en campos frecuentes como product_id y user_id ayudará a mejorar la velocidad de las consultas.
Modularización y Estructuración: Se dividirá la lógica de negocio y la visualización en diferentes módulos para mejorar la mantenibilidad y escalabilidad del proyecto.