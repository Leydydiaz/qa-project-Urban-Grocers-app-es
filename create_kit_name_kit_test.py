import unittest
import data
import sender_stand_request

class TestCreateKitNameKit(unittest.TestCase):

    # Pruebas POSITIVAS
    def test_create_kit_name_one_character(self):
        kit_body = sender_stand_request.get_kit_body(data.one_letter)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data.one_letter)

    def test_create_kit_name_max_characters(self):
        kit_body = sender_stand_request.get_kit_body(data.max_characters)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data.max_characters)

    def test_create_kit_name_special_characters(self):
        kit_body = sender_stand_request.get_kit_body(data.special_characters)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data.special_characters)

    def test_create_kit_name_spaces(self):
        kit_body = sender_stand_request.get_kit_body(data.spaces_in_name)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data.spaces_in_name)

    def test_create_kit_name_numbers(self):
        kit_body = sender_stand_request.get_kit_body(data.numbers_in_name)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data.numbers_in_name)

    # Pruebas NEGATIVAS
    def test_create_kit_name_empty_string(self):
        kit_body = sender_stand_request.get_kit_body(data.empty_name)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_exceeds_max_characters(self):
        kit_body = sender_stand_request.get_kit_body(data.exceeds_max_characters)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_missing_field(self):
        response = sender_stand_request.post_new_kit(data.missing_name_field, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_different_type(self):
        kit_body = sender_stand_request.get_kit_body(data.different_type_name)
        response = sender_stand_request.post_new_kit(kit_body, auth_token=data.user_body["firstName"])
        self.assertEqual(response.status_code, 400)

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
