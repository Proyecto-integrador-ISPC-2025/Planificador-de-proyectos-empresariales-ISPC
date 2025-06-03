# Planificador-de-proyectos-empresariales-ISPC
 1. Comprensión del Proyecto
Nombre del proyecto: Planificador de Proyectos Empresariales
Meta principal: Crear un programa de consola con menú interactivo para registrar, iniciar sesión y gestionar usuarios (administrador y estándar), junto con una base de datos que soporte esas funcionalidades.

2. Organización del Equipo y Tareas
A. Dividir roles
Recomiendo dividir el equipo en 3 áreas que pueden trabajar en paralelo:
| Área                    | Responsabilidades                                          |
| ----------------------- | ---------------------------------------------------------- |
| **Análisis y Modelado** | Diagrama de clases (POO), entidades y relaciones de la BD. |
| **Programación**        | Código del menú, registro, login, roles, funciones CRUD.   |
| **Base de datos**       | Diseño lógico (DER), modelo relacional y script SQL CRUD.  |

3. Paso a Paso con Herramientas
🔹 Paso 1: Modelado del Sistema (Clases y BD)
👉 Diagrama de Clases
Identificar clases como Usuario, Administrador, UsuarioEstandar, Sistema, etc.

Herramientas que podemos usar: draw.io, Lucidchart, Miro

👉 Modelo de Base de Datos
Entidades: usuarios, roles

Relaciones: uno a muchos (roles → usuarios)

Herramientas: draw.io, DbDiagram.io

Programación del Menú de Consola
Lenguaje: Python
Herramientas sugeridas:

IDE: Visual Studio Code

Repositorio: GitHub

Control de versiones: Git

🔹 Paso 3: Diseño del CRUD (Base de Datos)
Acciones:

INSERT para registrar usuarios.

SELECT para mostrar datos.

UPDATE para cambiar roles.

DELETE para eliminar usuarios.

📦 4. Repositorio y Versionado
Crear un repositorio en GitHub.

Cada integrante debe tener commits propios con comentarios descriptivos.

Ejemplo de mensajes:
"Implementada función de login con validación de rol"
"Diagrama de clases agregado al directorio /docs"

📚 5. Fuentes útiles
📖 Bibliografía y recursos sugeridos:
W3Schools SQL

Python Docs - Clases

Real Python

Git y GitHub para estudiantes

🗣️ 6. Defensa oral y entrega escrita
Cada estudiante debe preparar una parte del sistema para explicar (clases, funciones, estructura, base de datos).

Asegurarse de tener el documento “Estructura para el Proyecto ABP - 2025” completo.

Practicar el uso correcto de vocabulario técnico.