import requests
from bs4 import BeautifulSoup

from src.dao.kafka import Kafka
from src.app.container_controller import ContainerController
from src.config.config import Config


class LamodaParser:
    def __init__(
            self,
            kafka: Kafka,
            config: Config,
            container_controller: ContainerController
    ):
        self._kafka: Kafka = kafka
        self._config: Config = config
        self._container_controller = container_controller

    @property
    def config(self):
        return self._config

    @property
    def container_controller(self):
        return self._container_controller

    @property
    def kafka(self):
        return self._kafka

    def send_task(self, message):
        self.kafka.send_message(message)

    def get_task(self):
        return self.kafka.get_message()

    def parse_products(self, url, base_data):
        page_number = 1

        while True:
            url += str(page_number)

            request = requests.get(url)
            soup = BeautifulSoup(request.text)
            product_div_list = soup.findAll('div', class_='x-product-card__card')

            page_number += 1

            if len(product_div_list) == 0:
                break

            for product_div in product_div_list:
                data = {}
                price = product_div.find('span', class_='x-product-card-description__price-WEB8507_price_no_bold')
                data['price'] = price.text
                brand = product_div.find('div', class_='x-product-card-description__brand-name')
                data['brand'] = brand.text
                desc = product_div.find('div', class_='x-product-card-description__product-name')
                data['description'] = desc.text
                data = {**data, **base_data}

                self.container_controller.lamoda.create(data=data)

            if page_number == 2:
                break

    def lamoda_parse(self):
        self.parse_products(
            url=self.config.lamoda_urls.women_clothes_url,
            base_data={
                'sex': 'women',
                'type': 'clothes'
            }
        )
        self.parse_products(
            url=self.config.lamoda_urls.men_clothes_url,
            base_data={
                'sex': 'men',
                'type': 'clothes'
            }
        )
