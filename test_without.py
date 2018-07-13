#! /usr/bin/env python3
# coding: utf-8

from app import OpenFoodFactsAPI
from unittest import TestCase

class TestOpenFoodFactsAPI(TestCase):
    
    def test_count_product_numb(self):
        """
        Mise en place d'un test en mockant la méthode _get_product_from_api()
        en utilisant uniquement la caractère dynamique de Python ainsi que ces règmes de portées
        """

        def fake_api_result(self):
            result = {
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
            return result

        healthy_product = OpenFoodFactsAPI()
        healthy_product._get_product_from_api = fake_api_result

        self.assertEqual(healthy_product.count_product_numb("ferrero"), 2)