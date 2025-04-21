import requests
import json

configuracion_de_la_api = {
    "url_base": "https://cnt-4aeed52c-a504-4818-9fbc-9a12aca129dc.containerhub.tripleten-services.com",
    "endpoint_kits": "/api/v1/kits",
    "auth_token": "da2cd123-50f3-4a12-bcbd-380010063dc0"
}

url_base = configuracion_de_la_api["url_base"]
endpoint_kits = configuracion_de_la_api["endpoint_kits"]
auth_token = configuracion_de_la_api["auth_token"]

Función_para_crear_un_kit = ()
def crear_kit(kit_body):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(url_base + endpoint_kits, headers=headers, json=kit_body)
    return response

Pruebas = ()
def test_1_caracter():
    kit_body = {"name": "a"}
    response = crear_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_511_caracteres():
    kit_body = {"name": "a" * 511}
    response = crear_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_0_caracteres():
    kit_body = {"name": ""}
    response = crear_kit(kit_body)
    assert response.status_code == 400

def test_512_caracteres():
    kit_body = {"name": "a" * 512}
    response = crear_kit(kit_body)
    assert response.status_code == 400

def test_caracteres_especiales():
    kit_body = {"name": "№%@,"}
    response = crear_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_espacios():
    kit_body = {"name": " A Aaa "}
    response = crear_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_numeros():
    kit_body = {"name": "123"}
    response = crear_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_sin_parametro():
    kit_body = {}
    response = crear_kit(kit_body)
    assert response.status_code == 400

def test_tipo_parametro_diferente():
    kit_body = {"name": 123}
    response = crear_kit(kit_body)
    assert response.status_code == 400

configuracion_de_la_API = ()
test_1_caracter()
test_511_caracteres()
test_0_caracteres()
test_512_caracteres()
test_caracteres_especiales()
test_espacios()
test_numeros()
test_sin_parametro()
test_tipo_parametro_diferente()
