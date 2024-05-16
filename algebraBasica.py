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
    tokens_encontrados = []
    pos = 0
    longitud_codigo = len(codigo)
    while pos < longitud_codigo:
        match = None

        # Ignorar espacios en blanco
        if re.match(tokens[-1][1], codigo[pos]):
            pos += 1
            continue

        for tipo, patron in tokens:
            regex = re.compile(patron)
            match = regex.match(codigo, pos)
            if match:
                valor = match.group(0)
                if tipo != 'WHITESPACE' and tipo != 'COMENTARIO':  # Ignoramos espacios y comentarios
                    tokens_encontrados.append((tipo, valor))
                pos = match.end(0)
                break
        if not match:
            print(f"Error: Caracter no reconocido en la posición {pos}: '{codigo[pos]}'")
            return None

    # Verificación de errores específicos
    balance_parentesis = 0
    for tipo, valor in tokens_encontrados:
        if valor == '(':
            balance_parentesis += 1
        elif valor == ')':
            balance_parentesis -= 1
        if balance_parentesis < 0:
            print("Error: Paréntesis de cierre sin paréntesis de apertura.")
            return None

    if balance_parentesis != 0:
        print("Error: Paréntesis de apertura sin paréntesis de cierre.")
        return None

    return tokens_encontrados

# Solicitar al usuario que ingrese el código
print("Ingresa tu código. Presiona Enter dos veces para finalizar.")
codigo_fuente = ""
while True:
    linea = input()
    if not linea:
        break
    codigo_fuente += linea + "\n"

# Llamar al analizador léxico
tokens_encontrados = analizar_lexico(codigo_fuente)
if tokens_encontrados:
    for token in tokens_encontrados:
        print(token)
