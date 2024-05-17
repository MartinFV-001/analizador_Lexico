# Analizador Léxico

Este es un analizador léxico para un programa de álgebra básica con posibilidad de aumentar en complejidad. Nos permite identificar los tokens y maneja errores básicos, mostrando la posición del error y el motivo del mismo.

## Tabla de Tokens

---

### 1. COMENTARIO
**Expresión regular:** `'\|\|.*?\|\|'`  
**Acción:** Los comentarios delimitados por `||` serán ignorados por el analizador léxico y no se incluirán en la lista de tokens reconocidos.

---

### 2. NUMERO FLOTANTE
**Expresión regular:** `'\b\d+\.\d+\b'`  
**Acción:** Reconoce números con parte decimal. Ejemplos incluyen 3.14, 0.001. Estos se tratarán como valores numéricos de tipo flotante.

---

### 3. NUMERO ENTERO
**Expresión regular:** `'\b\d+\b'`  
**Acción:** Reconoce números enteros. Ejemplos incluyen 1, 12345. Estos se tratarán como valores numéricos de tipo entero.

---

### 4. OPERADOR ARITMETICO
**Expresión regular:** `'[+\-*/]'`  
**Acción:** Reconoce operadores aritméticos como +, -, *, /. Estos operadores se utilizarán para realizar operaciones matemáticas en las expresiones.

---

### 5. OPERADOR RELACIONAL
**Expresión regular:** `'==|!=|<=|<|>=|>'`  
**Acción:** Reconoce operadores relacionales como ==, !=, <=, <, >=, >. Estos operadores se utilizarán para comparar valores.

---

### 6. OPERADOR LOGICO
**Expresión regular:** `'&&|\|\||!'`  
**Acción:** Reconoce operadores lógicos como &&, ||, !. Estos operadores se utilizarán para realizar operaciones lógicas en las expresiones.

---

### 7. PARENTESIS
**Expresión regular:** `'[()]'`  
**Acción:** Reconoce paréntesis ( y ). Estos se utilizarán para agrupar expresiones y definir el orden de las operaciones.

---

### 8. VARIABLE
**Expresión regular:** `'\b[a-zA-Z]\b'`  
**Acción:** Reconoce variables representadas por una sola letra (por ejemplo, x, y, z). Las variables se utilizarán para almacenar valores y ser referenciadas en las expresiones.

---

### 9. WHITESPACE
**Expresión regular:** `'\s+'`  
**Acción:** Reconoce espacios en blanco, tabulaciones y saltos de línea. Estos serán ignorados por el analizador léxico y no se incluirán en la lista de tokens reconocidos.

---

Esta estructura asegura que cada token y su correspondiente acción sean claramente identificables, mejorando la legibilidad y organización del documento.
