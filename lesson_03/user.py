class User:
    first_name = ""
    last_name = ""

    def __init__(self, User_first_name, User_last_name):
        self.first_name = User_first_name
        self.last_name = User_last_name

    def User_Name(self):
        print(self.first_name)

    def User_Surname(self):
        print(self.last_name)

    def User_FullName(self):
        print(self.first_name, self.last_name)
