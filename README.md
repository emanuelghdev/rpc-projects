# Proyectos de ejemplo RPC

Este repositorio agrupa dos pequeños proyectos para practicar el diseño de sistemas distribuidos y concretamente el RPC (Remote Procedure Call).

1. **Calculadora Apache Thrift** (Python)  
2. **Sistema de donaciones replicado con RMI** (Java)

---

## 🧮 Calculadora Apache Thrift

Calculadora implementando un sistema cliente-servidor utilizando Apache Thrift.

### Operaciones disponibles

**Números**

- Suma
- Resta
- Multiplicación
- División

**Trignometría**

- Cálculo del coseno
- Cálculo de la tangente
- Conversión de grados a radianes
- Conversión de radianes a grados

**Vectores**

- Suma
- Resta
- Multiplicación escalar
- Multiplicación vectorial


**Matrices**

- Multiplicación
- Cálculo del determinante
- Cálculo de la traspuesta


### Requisitos

- Python 3.8+
- Apache Thrift (tool + librería Python)


### Instalación

```bash
# Instalar Thrift compiler
sudo apt-get install thrift-compiler   # Debian/Ubuntu
# o compilar desde la fuente: https://thrift.apache.org/

# Generar stubs Python
cd "Apache Thrift Calculator"
thrift --gen py calculadora.thrift

# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate
pip install thrift
```


### Ejecución

1. **Iniciar el servidor**

```bash
cd practica2_calculadora
source .venv/bin/activate
python servidor.py
Lanzar el cliente (en otra terminal)
```
2. **Lanzar el cliente** (en otra terminal)

```bash
cd practica2_calculadora
source .venv/bin/activate
python cliente.py
```

3. En el cliente, **utilizar la calculadora**.


### Instrucciones de uso

Una vez ejecutada esta orden veremos como se nos pide un input, pudiendo ser este “f” para mostrar la información completa del formato para el modo numérico de la calculadora o “v” para cambiar al modo vectorial de la calculadora o cualquier operación numérica disponible.

El formato de las **operaciones numéricas** es el siguiente ``<operando1> <operador> <operando2>`` para operaciones binarias, estando disponibles los operados suma (+), resta (-), multiplicación (*) y división (/) y ``<operador> <operando>`` para operaciones trigonométricas y de conversión, estando disponible los operadores seno (sen), coseno (cos), tangente (tan), conversión de grados a radianes (grad->rad) y conversión de radianes a grados (rad->grad).

Por ejemplo:

- 5 + 6
- 654.5 – 54
- 45 * 12
- 45 / 0 (Da un error controlado)
- sen 45
- cos 60
- tan 90
- grad->rad 45
- rad->grad 3

Si se quiere cambiar al **modo vectorial** de la calculadora solamente hace falta ingresar el carácter “v”, y estando en este modo veremos como se nos pide nuevamente un input, pudiendo ser este “f” para mostrar la información completa del formato para el modo vectorial de la calculadora o “b” para cambiar al modo numérico de la calculadora o cualquier operación vectorial y matricial disponible.

El formato de las operaciones vectoriales y matriciales es el siguiente ``<vector1> <operador> <vector>`` para operaciones con vectores y ``<matriz1> <operador> <matriz2>`` para las operaciones con matrices, estando disponibles los operados suma (+), resta (-) y multiplicación escalar y matricial (*). Además, para los vectores tenemos el operador “x” para la multiplicación vectorial. Por último, tenemos el formato ``<operador> <matriz>`` para calcular la matriz traspuesta y el determinante, estando disponible los operadores para la traspuesta (tras) y el determinante (det). El formato con el que pasar los vectores será mediante números separados por comas (,) sin espacios entre medias y de la misma manera para las matrices, separando las filas mediante puntos y comas (;) sin espacios entre medias.

Por ejemplo:

- 23,16,31 + 45,17,28
- 1,2,3;3,4,3 – 1,7,8;2,5,6
- 2,6,9;4,5,7;11,2,8 * 3,20,9;7,5,2;14,2,6
- 11,4,3 x 8,6,2
- det 42,51,36;22,13,81;47,9,33
- tras 32,8,16;92,54,21

---

## 📬 Ejemplos RMI

Colección de ejercicios progresivos de programación distribuida en Java, desarrollados con tecnología Java RMI (Remote Method Invocation).


### Ejemplos disponibles

**Ejemplo 1: Cliente-Servidor básico**

- Clases principales: ``Hola_I.java``, ``Hola.java``, ``Servidor1.java`` y ``Cliente1.java``

- Funcionalidad: Muestra cómo crear una interfaz remota sencilla.

- Objetivo: Comprender la base técnica del RMI.

- Diferencias clave: No hay argumentos ni estructuras de datos, únicamente posee una llamada remota a un método que devuelve un String.


**Ejemplo 2: Suma de dos números multihebra**

- Clases principales: ``Suma_I.java``, ``Suma.java``, ``Servidor2.java`` y ``Cliente2.java``

- Funcionalidad: El cliente solicita al servidor la suma de dos enteros.

- Objetivo:

    - Transmitir parámetros simples en métodos remotos.

    - Ver cómo el cliente envía datos, y el servidor devuelve un resultado específico.

- Diferencias clave: Este ejemplo aporta ya una lógica dinámica con parámetros.


**Ejemplo 3: Lista de elementos remota**

- Clases principales: ``Lista_I.java``, ``Lista.java``, ``Servidor3.java`` y ``Cliente3.java``

- Funcionalidad: Permite añadir cadenas a una lista compartida entre varios clientes, de forma que los clientes puedan ver los elementos actuales.

- Objetivo:

    - Gestionar una estructura de datos de forma remota.

    - Muestra cómo varios clientes comparten estado remoto.

- Diferencias clave: Añade persistencia temporal de datos en memoria.


**Ejemplo 4: Sistema de donaciones replicado**

- Clases principales: ``Donacion_I.java``, ``Donacion.java``, ``Entidad.java``, ``Servidor1.java``, ``Servidor2.java`` y ``Cliente.java``

- Funcionalidad:

    - El cliente puede registrar entidades donantes, realizar donaciones, consultar el total acumulado y ver un listado de entidades y montos.

    - Hay dos servidores (Servidor1, Servidor2) que mantienen réplicas coordinadas del sistema.

    - Las operaciones de donación se propagan entre las réplicas.

- Objetivo:

    - Simular un entorno con múltiples réplicas de servidor distribuidas.

    - Mantener consistencia entre réplicas de forma manual.

- Diferencias clave:

    - El sistema ya no tiene una única instancia del objeto remoto.

    - Hay lógica de replicación (los métodos se invocan entre servidores).

    - Se manejan estructuras como HashMap para almacenar entidades y montos.

    - Es tolerante a fallos parciales (puedes iniciar con una réplica y conectar con otra si está disponible).


### Requisitos

- Java 11+
- Un sistema RMI habilitado (no se necesita Maven/Gradle, basta javac y rmiregistry)


### Ejecución

1. **Acceder al directorio**

```bash
cd RMI
```

2. **Elegir cualquier el ejemplo e iniciar**

```bash
cd ejemplo4

# Ejecutar la macro
./macro.sh
```

### Comparativa general de los ejemplos

| Ejercicio            | Entradas        | Estructura usada         | Nº de servidores | Replicación | Nivel de complejidad  |
|----------------------|-----------------|--------------------------|------------------|-------------|-----------------------|
| Ejemplo 1            | Ninguna         | Ninguna                  | 1                | No          | Básico                |
| Ejemplo 2            | `int`, `int`    | Ninguna                  | 1                | No          | Bajo                  |
| Ejemplo 3            | `String`        | Lista (`ArrayList`)      | 1                | No          | Medio                 |
| Ejemplo 4            | `Entidad`, `int`| Diccionario (`Map`)      | 2 o más          | Sí          | Medio-Alto            |