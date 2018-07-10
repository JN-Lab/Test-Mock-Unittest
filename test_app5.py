from app import OpenFoodFactsAPI
from unittest import TestCase
from unittest.mock import Mock

class TestOpenFoodFactsAPI(TestCase):
    def test_count_product_numb(self):

        api_response = {
            "count": 6,
            "skip": 0,
            "page_size": "150",
            "page": 1,
            "products": [
                {
                    "product_name_fr" : "Ferrero boite de 30",
                    "nutrition_grade_fr": "a",
                },
                {
                    "product_name_fr" : "Ferrero Light sans sucre et sans goût",
                    "nutrition_grade_fr": "b",
                },
                {
                    "product_name_fr" : "Ferrero Rocher",
                    "nutrition_grade_fr": "e",
                },
                {
                    "product_name_fr" : "Ferrero couscous",
                    "nutrition_grade_fr": "a",
                },
                {
                    "product_name_fr" : "Ferrero chocolat praliné",
                    "nutrition_grade_fr": "d",
                },
                {
                    "product_name_fr" : "Ferrero à la fraise",
                    "nutrition_grade_fr": "c",
                },
                ]
        }

        healthy_product = OpenFoodFactsAPI()
        healthy_product.get_product_from_api = Mock()
        healthy_product.get_product_from_api.return_value = api_response

        self.assertEqual(healthy_product.count_product_numb("ferrero"), 2)