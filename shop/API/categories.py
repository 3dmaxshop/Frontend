import httpx
import orjson

from shop.api.schemas import Category


class CategoriesApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[Category]:
        response = httpx.get(f'{self.url}/api/v1/categories/')
        response.raise_for_status()

        return [Category(**category) for category in response.json()]

    def get_by_uid(self, uid) -> Category:
        response = httpx.get(f'{self.url}/api/v1/categories/{uid}')
        response.raise_for_status()

        return Category(**response.json())

    def delete(self, uid):
        response = httpx.delete(f'{self.url}/api/v1/categories/{uid}')
        response.raise_for_status()

    def change(self, categories: Category):
        dict_categories = categories.dict()
        json_categories = orjson.dumps(dict_categories)
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.put(f'{self.url}/api/v1/categories/', content=json_categories, headers=headers)
        response.raise_for_status()

    def add(self, categories: Category):
        dict_categories = categories.dict()
        json_categories = orjson.dumps(dict_categories)
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.post(f'{self.url}/api/v1/categories/', content=json_categories, headers=headers)
        response.raise_for_status()
