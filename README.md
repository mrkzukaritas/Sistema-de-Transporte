# 🚚 Sistema de Gestión de Envíos – Patrón Factory Method

Este proyecto implementa un **sistema de gestión de envíos** usando el **patrón de diseño Factory Method**, desarrollado en **Python**.

Permite gestionar distintos tipos de envíos (terrestre, marítimo y aéreo), aplicando el principio de **abstracción en la creación de objetos**, sin acoplar el código principal a las clases concretas.

Incluye un **CRUD completo** (crear, listar, actualizar, eliminar) y una **interfaz gráfica con Tkinter** para demostrar su funcionamiento.

---

## 🧩 Objetivo del proyecto

Implementar el **patrón Factory Method** en un contexto práctico:
- Simular diferentes tipos de transporte.
- Crear una capa de gestión de envíos.
- Separar las responsabilidades en módulos (principio de bajo acoplamiento).
- Proporcionar una interfaz gráfica intuitiva.

---

## 🏗️ Arquitectura del proyecto##
```
Sistema-de-Transporte/
│
├── main.py # Menú CRUD por consola
│
├── logistica/ # Implementación del patrón Factory Method
│ ├── transporte.py # Clases de transporte (Camion, Barco, Avion)
│ ├── logistica_base.py # Clase abstracta Logistica (Factory)
│ └── logistica_concretas.py # Clases concretas de Logistica
│
├── envios/ # Gestión de envíos (CRUD)
│ ├── envio.py # Clase modelo Envio
│ └── envio_manager.py # CRUD en memoria (usa Factory Method)
│
└── interfaz/ # Interfaz gráfica (Tkinter)
└── interfaz_envios.py
```
---

## ⚙️ Instalación y ejecución

### 🔹 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/Sistema-de-Transporte.git
cd Sistema-de-Transporte
```
### 🔹 2. Ejecutar Interfaz
```bash
python -m interfaz.interfaz_envios 
```
