# Encabezados para las peticiones
headers = {
    "Content-Type": "application/json"
}

# Datos del usuario para creación
user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave. Hamburg, NY"
}

# Auth token obtenido de Postman
auth_token = "da2cd123-50f3-4a12-bcbd-380010063dc0"

# -----------------------------
# Variables para pruebas POSITIVAS
# -----------------------------

# Nombre con un solo caracter
one_letter = "a"

# Nombre con 511 caracteres
max_length_name = "a" * 511

# Nombre con caracteres especiales
special_characters = "№%@,"

# Nombre con espacios
spaces_name = " A Aaa "

# Nombre compuesto solo por números
numbers_name = "123"

# -----------------------------
# Variables para pruebas NEGATIVAS
# -----------------------------

# Nombre vacío
empty_name = ""

# Nombre con más de 511 caracteres (512)
too_long_name = "a" * 512

# Nombre con tipo de dato incorrecto (entero)
different_type = 123

# Kit sin campo "name"
missing_name_field = {}
