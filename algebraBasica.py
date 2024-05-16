import re

# Definición de tokens con prioridad
tokens = [
    ('COMENTARIO', r'\|\|.*?\|\|'),            # Comentarios delimitados por ||
    ('NUMERO_FLOTANTE', r'\b\d+\.\d+\b'),     # Números flotantes
    ('NUMERO_ENTERO', r'\b\d+\b'),            # Números enteros
    ('OPERADOR_ARITMETICO', r'[+\-*/]'),      # Operadores aritméticos
    ('OPERADOR_RELACIONAL', r'==|!=|<=|<|>=|>'), # Operadores relacionales
    ('OPERADOR_LOGICO', r'&&|\|\||!'),        # Operadores lógicos
    ('ASIGNACION', r'='),                     # Operador de asignación
    ('PARENTESIS', r'[()]'),                  # Paréntesis
    ('VARIABLE', r'\b[a-zA-Z]\b'),            # Variables (una sola letra)
    ('WHITESPACE', r'\s+'),                   # Espacios en blanco
]

# Función para analizar el código fuente
def analizar_lexico(codigo):
    tokens_encontrados = [] #lista de tokens encontrados
    pos = 0 #posición actual en el código
    longitud_codigo = len(codigo) #longitud del código guardada en una variable para no calcularla cada vez
    while pos < longitud_codigo: #mientras no se haya llegado al final del código
        match = None #inicializar match en None al menos que se encuentre un token

        # Ignorar espacios en blanco
        if re.match(tokens[-1][1], codigo[pos]): #si el token es un espacio en blanco
            pos += 1 #aumentar la posición en el código
            continue 

        for tipo, patron in tokens: #para cada tipo de token y su patrón
            regex = re.compile(patron) #compilar el patrón en una expresión regular
            match = regex.match(codigo, pos) #buscar el patrón en el código a partir de la posición actual
            if match: #si se encontró el patrón
                valor = match.group(0) #obtener el valor del token respecto al patrón
                if tipo != 'WHITESPACE' and tipo != 'COMENTARIO':  # Ignoramos espacios y comentarios
                    tokens_encontrados.append((tipo, valor)) #agregar el token a la lista de tokens encontrados
                pos = match.end(0) #actualizar la posición actual en el código
                break
        if not match: #si no se encontró un token
            print(f"Error: Caracter no reconocido en la posición {pos}: '{codigo[pos]}'") #imprimir un mensaje de error con el caracter no reconocido
            return None

    # Verificación de errores específicos
    balance_parentesis = 0 #inicializar el balance de paréntesis en 0
    for tipo, valor in tokens_encontrados: #para cada token en la lista de tokens encontrados
        if valor == '(': #si el token es un paréntesis de apertura
            balance_parentesis += 1 #aumentar el balance de paréntesis
        elif valor == ')': #si el token es un paréntesis de cierre
            balance_parentesis -= 1 #disminuir el balance de paréntesis
        if balance_parentesis < 0: #si el balance de parenteris es menor a 0 no hay paréntesis de apertura para cerrar
            print("Error: Paréntesis de cierre sin paréntesis de apertura.")
            return None

    if balance_parentesis != 0: #si el balance de paréntesis no es 0, hay paréntesis de apertura sin cerrar
        print("Error: Paréntesis de apertura sin paréntesis de cierre.")
        return None

    return tokens_encontrados #retornar la lista de tokens encontrados

# Solicitar al usuario que ingrese el código
print("Ingresa tu código. Presiona Enter dos veces para finalizar.")
codigo_fuente = "" #inicializamos el código fuente como una cadena vacía
while True: #mientras no se presione Enter dos veces
    linea = input() #leer una línea de código
    if not linea: #si la línea está vacía
        break #salir del ciclo
    codigo_fuente += linea + "\n" #agregar la línea al código fuente

# Llamar al analizador léxico
tokens_encontrados = analizar_lexico(codigo_fuente) #llamar a la función analizar_lexico con el código fuente ingresado por el usuario
if tokens_encontrados: #si hay tokens detectados
    for token in tokens_encontrados: #para cada token en la lista de tokens encontrados
        print(token) #imprimimos el token y su tipo
