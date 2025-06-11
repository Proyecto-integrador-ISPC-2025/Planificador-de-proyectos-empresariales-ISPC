Paradigma y Estructura

La aplicación se basa en el paradigma de Programación Orientada a Objetos. La estructura se ha simplificado a cuatro archivos Python que colaboran entre sí:
   
    • main.py: Punto de entrada que inicia la aplicación. 
    
    • sistema.py: El núcleo de la aplicación. Contiene la clase SistemaEnMemoria, que gestiona la lógica de los menús, la interacción con el usuario y el almacenamiento de los datos. 
    
    • usuario.py: Define la clase Usuario, que actúa como modelo para representar los datos de cada usuario. 
    
    
    • validaciones.py: Módulo con funciones de utilidad, como la validación de contraseñas. 

Gestión de Datos en Memoria
   
    • Almacenamiento: Los objetos de la clase Usuario se almacenan en una lista (list) dentro de la instancia de SistemaEnMemoria. 
    
    • Ciclo de Vida de los Datos: Los datos son efímeros. La lista de usuarios se inicializa cada vez que se ejecuta main.py (con un administrador por defecto) y cualquier cambio se pierde al cerrar la terminal. 
   
    • Operaciones CRUD: Las operaciones de Crear, Leer, Actualizar y Borrar se realizan directamente sobre la lista de objetos en memoria mediante bucles y métodos de lista de Python. 
