#! /usr/bin/env python3
# coding: utf-8
import urllib.parse
import urllib.request
import urllib.error
import json

class OpenFoodFactsAPI:
    """
    Cette classe a pour objectif de récupérer les produits associée à une marque
    via l'API d'OpenFoodFacts et de compter le nombre de produits ayant une bonne
    note alimentaire.
    """
    def _get_product_from_api(self, brand):
        """
        Cette méthode a pour objectif de récupérer les 150 premiers produits liés
        à une marque via l'API OpenFoodFacts
        """

        payload = {
            'action' : 'process',
            'json' : '1',
            'tagtype_0' : 'brands',
            'tag_contains_0' : 'contains',
            'tag_0' : brand,
            'page_size' : '150',
            'page' : '1'
        }

        parameters = urllib.parse.urlencode(payload)
        url = "http://fr.openfoodfacts.org/cgi/search.pl"
        parameters = parameters.encode('utf-8')
        req = urllib.request.Request(url, parameters)

        try:
            response = urllib.request.urlopen(req)
            response_body = response.read().decode("utf-8")
            data = json.loads(response_body)
            return data
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)

    def count_product_numb(self, brand):
        """
        Cette méthode a pour objectif de dénombrer le nombre de produits ayant
        une bonne note alimentaire
        Il s'agit de la méthode à tester pour cette exercice
        """
        data = self._get_product_from_api(brand)
        healthy_product = 0
        for product in data["products"]:
            try:
                if product["nutrition_grade_fr"] == "a":
                    healthy_product += 1
            except:
                pass
        
        return healthy_product

if __name__ == "__main__":
    api = OpenFoodFactsAPI()
    healthy_product = api.count_product_numb("ferrero")
    print(healthy_product)