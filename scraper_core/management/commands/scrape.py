from django.core.management.base import BaseCommand, CommandError
from scraper_core.scrapers.sreality_scraper import SRealityAPI, PROPERTY_TYPES

class Command(BaseCommand):
    help = 'Fetches data and fills in database'

    def handle(self, *args, **kwargs):
        srapi = SRealityAPI()
        srapi.fetch_data(PROPERTY_TYPES['FLAT'])
        srapi.fill_in_db()
        self.stdout.write(self.style.SUCCESS('Successfully fetched data and filled database'))