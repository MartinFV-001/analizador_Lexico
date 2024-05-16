# analizador_Lexico
Este es un analizador lexico para un programa de algebra basica con posibilidades a aumento en la complejidad de algebra, nos permite identificar los tokens al igual que tiene un manejo de errores basico mostrando
la posicion de tu error y el por que de este mismo
##Tabla de tokens
**1. COMENTARIO (\|\|.*?\|\|)**
Acción: Los comentarios delimitados por || serán ignorados por el analizador léxico y no se incluirán en la lista de tokens reconocidos.
**2. NUMERO_FLOTANTE (\b\d+\.\d+\b)**
Acción: Reconoce números con parte decimal. Ejemplos incluyen 3.14, 0.001. Estos se tratarán como valores numéricos de tipo flotante.
**3. NUMERO_ENTERO (\b\d+\b)**
Acción: Reconoce números enteros. Ejemplos incluyen 1, 12345. Estos se tratarán como valores numéricos de tipo entero.
**4. OPERADOR_ARITMETICO ([+\-*/])**
Acción: Reconoce operadores aritméticos como +, -, *, /. Estos operadores se utilizarán para realizar operaciones matemáticas en las expresiones.
**5. OPERADOR_RELACIONAL (==|!=|<=|<|>=|>)**
Acción: Reconoce operadores relacionales como ==, !=, <=, <, >=, >. Estos operadores se utilizarán para comparar valores.
**6. OPERADOR_LOGICO (&&|\|\||!)**
Acción: Reconoce operadores lógicos como &&, ||, !. Estos operadores se utilizarán para realizar operaciones lógicas en las expresiones.
**7. PARENTESIS ([()])**
Acción: Reconoce paréntesis ( y ). Estos se utilizarán para agrupar expresiones y definir el orden de las operaciones.
**8. VARIABLE (\b[a-zA-Z]\b)**
Acción: Reconoce variables representadas por una sola letra (por ejemplo, x, y, z). Las variables se utilizarán para almacenar valores y ser referenciadas en las expresiones.
**9. WHITESPACE (\s+)**
Acción: Reconoce espacios en blanco, tabulaciones y saltos de línea. Estos serán ignorados por el analizador léxico y no se incluirán en la lista de tokens reconocidos.
