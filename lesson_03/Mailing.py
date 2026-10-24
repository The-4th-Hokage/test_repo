class Mailing:

    def __init__(self, Mailing_To_Address, Mailing_From_Address, Mailing_Cost:float, Mailing_Track):
        self.to_address = Mailing_To_Address
        self.from_address = Mailing_From_Address
        self.mailing_cost = Mailing_Cost
        self.mailing_track = Mailing_Track