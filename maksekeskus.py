import requests
from pprint import pprint

from requests.auth import HTTPBasicAuth


class Maksekeskus:
    def __init__(self, shop_id, publishable_key=None, secret_key=None, test_env=False):
        self.shop_id = shop_id
        self.publishable_key = publishable_key
        self.secret_key = secret_key
        self.test_env = test_env

        if self.test_env:
            self.env_urls = {
                'api_url': 'https://api-test.maksekeskus.ee',
                'checkoutjs_url': 'https://payment-test.maksekeskus.ee/checkout/dist/',
                'gateway_url': 'https://payment-test.maksekeskus.ee/pay/1/signed.html',
                'merchant_url': 'https://merchant-test.maksekeskus.ee/',
                'statics_url': 'https://static-test.maksekeskus.ee/'
            }
        else:
            self.env_urls = {
                'api_url': 'https://api.maksekeskus.ee',
                'checkoutjs_url': 'https://payment.maksekeskus.ee/checkout/dist/',
                'gateway_url': 'https://payment.maksekeskus.ee/pay/1/signed.html',
                'merchant_url': 'https://merchant.maksekeskus.ee/',
                'statics_url': 'https://static.maksekeskus.ee/'
            }

    def compose_url(self, endpoint):
        return self.env_urls['api_url'] + endpoint

    def get_shop(self):
        return requests.get(self.compose_url('/v1/shop'), auth=HTTPBasicAuth(self.shop_id, self.secret_key))

    def get_payment_methods(self, request_params):
        return requests.get(self.compose_url('/v1/methods'), request_params, auth=HTTPBasicAuth(self.shop_id, self.secret_key))

    def create_transaction(self, json):
        return requests.post(self.compose_url('/v1/transactions'), json=json, auth=HTTPBasicAuth(self.shop_id, self.secret_key))


