import ply.lex as lex

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
delimitadores = {'(', ')', '{', '}', '[', ']', '"', "'", ';', '#', ',', '.', ''}

# Definición de tokens
tokens = (
    'PALABRA_CLAVE',
    'OPERADOR',
    'DELIMITADOR',
    'NUMERO',
    'TEXTO_LIBRE'
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
    r'[+\-*/<>=!%]+'
    if t.value in operadores:
        t.type = 'OPERADOR'
    return t

def t_DELIMITADOR(t):
    r'[()\[\]{}"\'#;,\.\']+'
    if t.value in delimitadores:
        t.type = 'DELIMITADOR'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Token no reconocido: '{t.value}'")
    t.lexer.skip(1)

# Construir el analizador léxico
analizador = lex.lex()

# Entrada de texto desde el usuario
texto = input("Ingresa información de una campaña publicitaria: ")

# Analizar el texto
analizador.input(texto)

# Obtener y mostrar los tokens
while True:
    token = analizador.token()
    if not token:
        break  # Se alcanzó el final del texto
    print(token)
