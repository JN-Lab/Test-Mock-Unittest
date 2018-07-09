import app
from unittest import TestCase
from unittest.mock import patch

class TestOpenFoodFactsAPI(TestCase):

    @patch('app.OpenFoodFactsAPI')
    def test_count_product_numb(self, mock_OpenFoodFactsAPI):

        mock_OpenFoodFactsAPI.get_product_from_api.return_value = {
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

        #mock_OpenFoodFactsAPI.get_product_from_api.assert_called()
        healthy_product = app.OpenFoodFactsAPI()
        self.assertEqual(healthy_product.count_product_numb("ferrero"), 2)