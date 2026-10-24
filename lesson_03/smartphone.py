class SmartPhone:

    def __init__(
        self,
        SmartPhone_Phone_Brand,
        SmartPhone_Phone_Model,
        SmartPhone_Abonent_Number,
    ):
        self.phone_brand = SmartPhone_Phone_Brand
        self.phone_model = SmartPhone_Phone_Model
        self.abonent_number = SmartPhone_Abonent_Number

    def __str__(self):
        return f"{self.phone_brand}, {self.phone_model}, {self.abonent_number}"
