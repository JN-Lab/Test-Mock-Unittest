#! /usr/bin/env python3
# coding: utf-8
import urllib.parse
import urllib.request
import urllib.error
import json

class OpenFoodFactsAPI:

    def get_product_from_api(self, brand):
        """
        Get the first 150 products from Openfoodfacts API linked to a brand name
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
        Count all healthy products
        """
        data = self.get_product_from_api(brand)
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