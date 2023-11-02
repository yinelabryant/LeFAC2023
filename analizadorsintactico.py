import ply.lex as lex
import ply.yacc as yacc

# Lista de palabras clave de Spotify (con tildes y caracteres especiales)
palabras_clave_spotify = [
    "Música", "Listas", "Reproducción", "Descarga", "Artistas", "Explora", "Descubre",
    "Premium", "Gratis", "Streaming", "Canciones", "Audiencia", "Playlist", "Experiencia",
    "Personalizada", "Favoritas", "Géneros", "Sin anuncios", "Calidad", "Dispositivos",
    "Álbum", "Novedades", "Charts", "Descubrimiento", "Seguir", "Escuchar", "Compartir",
    "Recomendaciones", "Diversidad", "Conectividad", "Podcast", "Wrapped", "Pop",
    "Rock", "Indie", "Sad", "Reggaeton", "Librería",
    "Campaña", "Publicidad", "Anuncios", "Promoción", "Marketing",
    "Usuarios", "Reproducciones", "Éxito", "Personalización",
    "Tendencias", "Selección", "Promociones", "Tasas", "Conversiones", "Segmentación",
    "Engagement", "Interacción", "Estadísticas", "Exitosas", "Premium", "Spotify"
]

# Operadores y delimitadores
operadores = {"+", "-", "*", "/", "<", ">", "=", "<=", ">=", "==", "!=", "++", "--", "%"}
delimitadores = {'(', ')', '{', '}', '[', ']', '"', "'", ';', '#', ',', '.', '', ''}

# Definición de tokens
tokens = (
    'PALABRA_CLAVE',
    'OPERADOR',
    'DELIMITADOR',
    'NUMERO',
    'TEXTO_LIBRE',
    'DOS_PUNTOS'
)

# Reglas para tokens simples
def t_PALABRA_CLAVE(t):
    r'[A-Za-zÁ-Úá-ú]+'
    if t.value.lower() in [p.lower() for p in palabras_clave_spotify]:
        t.type = 'PALABRA_CLAVE'
    else:
        t.type = 'TEXTO_LIBRE'
    return t

def t_OPERADOR(t):
    r'[+\-*/<>=%]+'
    if t.value in operadores:
        t.type = 'OPERADOR'
    return t

def t_DELIMITADOR(t):
    r'[()\[\]{}"\'#;,\.\¿?!¡:]'
    if t.value in delimitadores:
        t.type = 'DELIMITADOR'
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DOS_PUNTOS(t):
    r':'
    t.type = 'DOS_PUNTOS'
    return t

# Ignorar espacios en blanco y tabulaciones

t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Token no reconocido: '{t.value}'")
    t.lexer.skip(1)

#------------------------------------COMIENZA LA FASE 2-----------------------------------

# Función de inicio
def p_start(p):
    """
    start : campaign
    """
    p[0] = p[1]

# Reglas para una campaña publicitaria
def p_campaign(p):
    """
    campaign : DELIMITADOR title DELIMITADOR body DELIMITADOR
             | DELIMITADOR title DELIMITADOR body DELIMITADOR DELIMITADOR
    """
    # Aquí puedes verificar el título y el cuerpo según las reglas definidas
    p[0] = "Campaña válida" 

# Reglas para el título
def p_title(p):
    """
    title : PALABRA_CLAVE
          | title PALABRA_CLAVE

    """
    # Lógica para verificar las reglas del título
    p[0] = "Título válido"  

# Reglas para el cuerpo
def p_body(p):
    """
    body : text
         | text body
    """
    # Lógica para verificar las reglas del cuerpo
    p[0] = "Cuerpo válido"  

# Reglas para el texto
def p_text(p):
    """
    text : PALABRA_CLAVE
         | TEXTO_LIBRE
         | NUMERO
    """
    # Lógica para verificar las reglas del texto
    p[0] = "Texto válido" 

# Manejo de errores sintácticos
def p_error(p):
    print(f"Error sintáctico en la entrada: {p}")


# Construir el analizador léxico
analizador_lexico = lex.lex()
# Construir el analizador sintáctico
analizador_sintactico = yacc.yacc()

# Entrada de texto desde el usuario
texto = input("Ingresa información de una campaña publicitaria: ")

# Analizar el texto léxicamente
analizador_lexico.input(texto)

# Obtener y mostrar los tokens
while True:
    token = analizador_lexico.token()
    if not token:
        break  # Se alcanzó el final del texto
    print(token)

# Analizar sintácticamente
resultado = analizador_sintactico.parse(texto)
print(resultado)
