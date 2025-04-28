# data.py

# Información básica de un usuario
user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave. Hamburg, NY"
}

# Cabeceras (headers) para la solicitud HTTP
headers = {
    "Content-Type": "application/json"
}

# Variables para pruebas POSITIVAS
one_letter = "a"
max_characters = "A" * 511  # 511 caracteres
special_characters = "№%@,"
spaces_in_name = " A Aaa "
numbers_in_name = "123"

# Variables para pruebas NEGATIVAS
empty_name = ""
exceeds_max_characters = "A" * 512  # 512 caracteres
missing_name_field = {}  # kit_body sin el campo name
different_type_name = 123  # name no como string, sino número
