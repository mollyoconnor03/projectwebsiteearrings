# dao/EarringDAO.py
from model.Earring import Earring


class EarringDAO:
    def __init__(self):
        self.earrings = [
            Earring(1, "Violet", "Heart Earrings", "Heart Shaped gold everyday earring made with 24k gold", "Gold", "images/product1.png", "€20"),
            Earring(2, "Darling", "Large Hoops", "8mm gold hoops perfect for any occasion", "Gold", "images/product2.png", "€22"),
            Earring(3, "Maisie", "Bow Studs", "Dainty bow shaped studs", "Gold", "images/product3.png", "€17"),
            Earring(4, "Siún", "Diamond hearts", "Diamond filled heart shaped studs", "Silver", "images/product4.png", "€50"),
            Earring(5, "Daisy", "Silver mini hoops", "4mm silver hoops, perfect for stacking with our other hoops", "Silver", "images/product5.png", "€30"),
            Earring(6, "Niamh", "Gold mini hoops", "4mm gold hoops, perfect for stacking with our other gold hoops", "Gold", "images/product6.png", "€28"),
            Earring(7, "Fiona", "Chunky hoops", "Small, thick gold hoops perfect for everyday looks.", "Gold", "images/product7.png", "€35"),
        ]

    def get_all_earrings(self):
        return self.earrings

    def get_earring_by_id(self, earring_id):
        for earring in self.earrings:
            if earring.earring_id == earring_id:
                return earring
        return None
