class Address:

    def __init__(
        self,
        Address_Index,
        Adress_City,
        Addres_Street,
        Address_House,
        Address_Flat,
    ):
        self.address_index = Address_Index
        self.address_city = Adress_City
        self.address_street = Addres_Street
        self.address_house = Address_House
        self.address_flat = Address_Flat

    def __str__(self):
        return f"{self.address_index}, {self.address_city}, {self.address_street}, {self.address_house} - {self.address_flat}"
