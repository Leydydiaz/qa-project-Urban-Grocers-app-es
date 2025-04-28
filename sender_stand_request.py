import requests
import data
import configuration

# Crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=configuration.headers
    )

# Crear el cuerpo (body) de un kit, usando solo el nombre
def get_kit_body(name):
    kit_body = {
        "name": name
    }
    return kit_body

# Crear un nuevo kit
def post_new_kit(kit_body, auth_token):
    headers = configuration.headers.copy()  # Copiamos para no modificar el original
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )
