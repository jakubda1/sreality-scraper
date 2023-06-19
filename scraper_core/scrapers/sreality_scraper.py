from typing import Dict, Any, AnyStr
import time
import urllib.parse
import requests  # pip install requests
from scraper_core.models import Reality

PROPERTY_TYPES = {
    "ALL": {},
    "HOUSE": {
        "category_main_cb": 2,
        "category_type_cb": 1,
    },
    "FLAT": {
        "category_main_cb": 1,
        "category_type_cb": 1,
    },
    "PARCEL": {
        "category_main_cb": 3,
        "category_type_cb": 1,
    },
}

def try_except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred during accessing data: {str(e)}")
    return wrapper

class SRealityAPI:
    def __init__(self):
        self.fetched_data = None

    @try_except_decorator
    def get_image(self, estate: Dict) -> AnyStr:
        return estate.get("_links").get("images")[0].get("href")

    @try_except_decorator
    def get_name(self, estate: Dict) -> AnyStr:
        return estate.get("name")

    def fetch_data(self, params: Dict[str, Any], page: int = 1, per_page: int = 500) -> Dict:
        params["page"] = page
        params["per_page"] = per_page
        params["tms"] = int(time.time() * 1000)
        url = f"https://www.sreality.cz/api/cs/v2/estates?{urllib.parse.urlencode(params)}"

        print("fetching", url)
        response = requests.get(url)
        response.raise_for_status()
        self.fetched_data = response.json()

    def process_reality_to_fill_into_db(self, estate):
        title = self.get_name(estate)
        img_url = self.get_image(estate)
        return {"title": title, "image_url": img_url}

    def fill_in_db(self):
        if self.fetched_data is None:
            raise RuntimeError("There is need to fetch data beforehand filling to database.")

        for estate in self.fetched_data["_embedded"]["estates"]:
            print(estate)
            data = self.process_reality_to_fill_into_db(estate)
            r = Reality(**data)
            r.save()


if __name__ == '__main__':
    srapi = SRealityAPI()
    srapi.fetch_data(PROPERTY_TYPES['FLAT'])
    srapi.fill_in_db()