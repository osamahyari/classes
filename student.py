class Student:
    def __init__(self, fname, lname, phone, address, major):
        self.first_name = fname
        self.last_name = lname
        self.phone_number = phone
        self.address = address
        self.major = major
    def register(self):
        print('hi ' + self.first_name)