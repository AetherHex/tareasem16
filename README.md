
# 🍽️ Restaurante App - Gestión de Usuarios (Semana 16)

## 📌 Propósito de la Actividad

Este proyecto corresponde a la **Semana 16** de la asignatura de **Programación Orientada a Objetos**.

El objetivo principal de esta entrega es aplicar de manera práctica el **manejo de eventos en Tkinter** dentro de un sistema modular.

A partir de la versión base construida en semanas anteriores, el sistema ha evolucionado para incorporar un módulo de **Gestión de Usuarios** con operaciones CRUD:

- 📝 **Registrar**
- 🔍 **Consultar**
- ✏️ **Actualizar**
- 🗑️ **Eliminar**

De esta manera, se demuestra cómo interactúan los eventos del teclado, la selección de elementos en tablas y los menús desplegables mediante el uso de *callbacks*.

---

## 🏗️ Evolución y Arquitectura del Proyecto

El proyecto mantiene una estricta **separación de responsabilidades** mediante una arquitectura modular.

La lógica de negocio y la persistencia de datos no se encuentran directamente dentro de la interfaz gráfica.

```text
restaurante_app/
├── datos/                  # Archivos de persistencia (usuarios.json, etc.)
├── modelos/                # Entidades del negocio (usuario.py, producto.py, etc.)
├── servicios/              # Reglas de negocio y lectura/escritura
│   └── restaurante_servicio.py
├── ui/                     # Vistas e interfaces
│   ├── login_view.py
│   └── main_view.py
├── assets/                 # Recursos visuales (logo e íconos PNG)
├── main.py                 # Punto de entrada y configuración DPI
└── README.md               # Documentación del proyecto
````

 ### 🔹 Separación de responsabilidades

 - 📦 **`modelos/`**: Contiene las entidades principales del sistema.
- ⚙️ **`servicios/`**: Gestiona las reglas de negocio y el acceso a los datos.
- 🖥️ **`ui/`**: Contiene las interfaces gráficas y el manejo de eventos.
- 💾 **`datos/`**: Almacena la información persistente del sistema.
- 🎨 **`assets/`**: Contiene imágenes, logos e íconos utilizados por la aplicación.
- 🚀 **`main.py`**: Es el punto de entrada de la aplicación.

---

 ## 👥 Gestión de Usuarios y Roles

 El modelo `Usuario` ha sido actualizado para incluir el atributo `rol`.

 El sistema reconoce tres roles básicos:

 | Rol | Descripción |
| --- | --- |
| 👑 **Administrador** | Tiene acceso total al sistema y es el único autorizado para visualizar y utilizar el módulo de gestión de usuarios. |
| 👨‍💼 **Empleado** | Tiene acceso restringido a operaciones básicas relacionadas con ventas y productos. |
| 👤 **Cliente** | Es el rol predeterminado para perfiles externos. |

### 🔐 Nota de seguridad

 La aplicación evita que un administrador pueda **eliminar su propia cuenta mientras mantiene la sesión activa**.

 Esto permite prevenir situaciones en las que el usuario actualmente autenticado quede sin una cuenta válida durante la ejecución del sistema.

---

 ## ⚡ Manejo de Eventos Implementados

 Durante esta semana se introdujo la captura de eventos en la interfaz gráfica (**UI**) sin contaminar la lógica de negocio.

 Se implementaron los siguientes eventos:

 ### 🖱️ `<<TreeviewSelect>>` — Selección de tabla

 Al seleccionar una fila del `Treeview`, se dispara un _callback_ que:

 1. Obtiene el ID del usuario seleccionado.
2. Consulta la información mediante `RestauranteServicio`.
3. Carga los datos correspondientes en el formulario.
4. Evita exponer contraseñas directamente en la tabla.

 Esto permite mantener la interfaz separada de la lógica de acceso a los datos.

---

 ### ⌨️ `<Return>` — Tecla Enter

 Permite ejecutar el registro de un nuevo usuario directamente desde el teclado, sin necesidad de hacer clic sobre el botón correspondiente.

``` python
self.bind("<Return>", self.registrar_usuario)
```

---

 ### ⎋ `<Escape>` — Tecla Esc

 Permite:

 - 🧹 Limpiar los campos del formulario.
- ❌ Deseleccionar elementos de la tabla.
- 🔄 Restablecer el estado inicial de la interfaz.

 De esta manera, el usuario puede reiniciar rápidamente el formulario utilizando únicamente el teclado.

---

 ### 🔽 `<<ComboboxSelected>>` — Cambio de selección

 Detecta cuándo el usuario selecciona un nuevo rol en el `Combobox`.

 El evento actualiza una etiqueta de estado ubicada en la parte inferior de la interfaz, proporcionando **retroalimentación visual** al usuario.

---

 ## 🔄 Diferencia entre `bind()` y `command=`

 En este proyecto se evidencia la diferencia entre ambos mecanismos de manejo de eventos en Tkinter.

 ### 🔘 `command=`

 Se utiliza principalmente para los botones de acción:

 - 📝 Registrar
- ✏️ Actualizar
- 🗑️ Eliminar

 Por ejemplo:

``` python
ttk.Button(
    ventana,
    text="Registrar",
    command=self.registrar_usuario
)
```

 `command=` asocia directamente la acción del botón con un método, **sin recibir un objeto `event` como argumento**.

---

 ### 🔗 `bind()`

 Se utiliza para capturar interacciones indirectas o eventos específicos de la interfaz, como:

 - ⌨️ Teclas de acceso rápido.
- 🖱️ Selección de elementos en un `Treeview`.
- 🔽 Cambios de selección en un `Combobox`.

 Por ejemplo:

``` python
self.bind("<Escape>", self.limpiar_formulario)
```

 En este caso, el _callback_ recibe un objeto `event` con información relacionada con la interacción.

 ### 📌 Resumen

 | Mecanismo | Uso principal | Recibe `event` |
| --- | --- | --- |
| `command=` | Botones y acciones directas | ❌ No |
| `bind()` | Teclado y eventos de widgets | ✅ Sí |

En todos los casos, se reutilizaron los métodos existentes para evitar la **duplicación de código** dentro de los _callbacks_.

---

 ## 💾 Persistencia de Datos

 Los datos de los usuarios se conservan en formato **JSON** dentro del archivo:

```
datos/usuarios.json
```

 Para respetar la arquitectura modular, la interfaz ubicada en:

```
ui/main_view.py
```

 **no lee ni escribe directamente** el archivo JSON.

 Todas las operaciones de:

 - 🔍 Consulta
- 📝 Registro
- ✏️ Actualización
- 🗑️ Eliminación

 pasan primero por `RestauranteServicio`, que se encarga de aplicar las validaciones correspondientes antes de solicitar la persistencia de los datos mediante `ArchivoServicio`.

 ### 🔄 Flujo de datos

```
┌─────────────────────────────┐
│     Interfaz gráfica (UI)   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    RestauranteServicio      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Validaciones y reglas       │
│        de negocio           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       ArchivoServicio       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    datos/usuarios.json      │
└─────────────────────────────┘
```

 Esta separación permite mantener el código organizado y facilita futuras modificaciones del sistema.

---

 ## 🚀 Cómo ejecutar el proyecto

 ### 1️⃣ Requisitos previos

 Es necesario tener instalado:

 - 🐍 **Python 3**
- 🖼️ **Pillow**

 Pillow se utiliza para el manejo avanzado y escalado de las imágenes e íconos ubicados en la carpeta `assets/`.

 Instala Pillow mediante:

``` python
pip install Pillow
```

 ### 2️⃣ Clonar o descargar el repositorio

 Clona el repositorio o descarga el proyecto en tu computadora.

 Asegúrate de conservar la estructura de carpetas indicada anteriormente.

 ### 3️⃣ Verificar los recursos

 Comprueba que los recursos visuales se encuentren dentro de:

```
assets/
```

 Entre ellos deben estar:

```
assets/
├── logo.png
├── ...
└── ...
```

 Los íconos utilizados por los botones también deben encontrarse dentro de esta carpeta.

 ### 4️⃣ Ejecutar la aplicación

 Desde la raíz del proyecto, donde se encuentra el archivo `main.py`, ejecuta:

``` bash
python main.py
```

---

 ## 🔑 Credenciales de prueba

 Para realizar las pruebas se pueden utilizar las credenciales almacenadas por defecto en:

```
datos/usuarios.json
```

 Por ejemplo:

``` json
Usuario: admin
Clave: 123
```

 > ⚠️ **Nota:** Estas credenciales son únicamente para pruebas y desarrollo. No se recomienda utilizar contraseñas simples en un entorno de producción.

---

 ## 📚 Tecnologías utilizadas

 - 🐍 **Python 3**
- 🖥️ **Tkinter**
- 🖼️ **Pillow**
- 📄 **JSON**
- 🧱 **Programación Orientada a Objetos**
- 🏗️ **Arquitectura modular**
- 🔄 **Manejo de eventos y callbacks**
- 📦 **Separación entre interfaz, servicios y persistencia**

---

 ## ✅ Conclusión

 La implementación de esta **Semana 16** permite reforzar el uso de **eventos en Tkinter**, demostrando cómo una interfaz gráfica puede responder a diferentes tipos de interacción del usuario sin mezclar responsabilidades con la lógica de negocio.

 La incorporación del módulo de **Gestión de Usuarios**, los **roles** y las operaciones **CRUD** permite ampliar el sistema desarrollado en semanas anteriores, manteniendo una estructura:

 - 🧩 Organizada
- ♻️ Reutilizable
- 📈 Escalable
- 🔐 Con separación de responsabilidades
- ⚡ Con manejo de eventos mediante _callbacks_
