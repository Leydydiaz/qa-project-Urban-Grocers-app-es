import unittest
from sender_stand_request import post_new_client_kit
from data import (
    one_letter,
    max_characters,
    special_characters,
    spaces_in_name,
    numbers_in_name,
    empty_name,
    exceeds_max_characters,
    missing_name_field,
    different_type_name
)

class TestCreateKitNameKit(unittest.TestCase):
    # Pruebas positivas

    def test_create_kit_name_one_character(self):
        kit_body = {"name": one_letter}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_max_characters(self):
        kit_body = {"name": max_characters}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_special_characters(self):
        kit_body = {"name": special_characters}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_spaces(self):
        kit_body = {"name": spaces_in_name}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    def test_create_kit_name_numbers(self):
        kit_body = {"name": numbers_in_name}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], kit_body["name"])

    # Pruebas negativas

    def test_create_kit_name_empty_string(self):
        kit_body = {"name": empty_name}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_exceeds_max_characters(self):
        kit_body = {"name": exceeds_max_characters}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_missing_parameter(self):
        kit_body = missing_name_field  # No "name" en el body
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

    def test_create_kit_name_different_type(self):
        kit_body = {"name": different_type_name}
        response = post_new_client_kit(kit_body)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
