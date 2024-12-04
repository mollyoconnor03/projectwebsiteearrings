# service/EarringService.py
from dao.EarringDAO import EarringDAO


class EarringService:
    def __init__(self):
        self.earring_dao = EarringDAO()

    def get_all_earrings(self):
        return self.earring_dao.get_all_earrings()

    def get_earring_details(self, earring_id):
        return self.earring_dao.get_earring_by_id(earring_id)
