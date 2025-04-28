import unittest
from sender_stand_request import post_new_client_kit

class TestCreateKitNameKit(unittest.TestCase):
    # Pruebas POSITIVAS
    def test_create_kit_name_one_character(self):
        kit_body = {"name": "a"}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_max_511_characters(self):
        kit_body = {"name": "a" * 511}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_special_characters(self):
        kit_body = {"name": "№%@,"}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_spaces(self):
        kit_body = {"name": " A Aaa "}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_numbers(self):
        kit_body = {"name": "123"}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    # Pruebas NEGATIVAS
    def test_create_kit_name_empty_string(self):
        kit_body = {"name": ""}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_exceeds_max_512_characters(self):
        kit_body = {"name": "a" * 512}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_missing_parameter(self):
        kit_body = {}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_wrong_type_integer(self):
        kit_body = {"name": 123}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
