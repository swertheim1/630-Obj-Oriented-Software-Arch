class Person:

    def __init__(self, f_name, l_name, address, city, state, zip, phone, email, country_region='USA'):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.state_province = state
        self.zip = zip
        self.phone = phone
        self.email_address = email
        self.country_region = country_region

    def __str__(self):
        return f"Name: {self.f_name} {self.l_name}\n" \
               f"Address: {self.address}\n" \
               f"City: {self.city}\n" \
               f"State/Province: {self.state_province}\n" \
               f"Zip: {self.zip}\n" \
               f"Phone: {self.phone}\n" \
               f"Email: {self.email_address}\n" \
               f"Country: {self.country_region}"

    # getters
    def get_name(self):
        return self.f_name + " " + self.l_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state_province(self):
        return self.state_province

    def get_zip(self):
        return self.zip

    def  get_country(self):
        return self.country_region

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email_address

    # Setters
    def set_first_name(self, f_name):
        self.f_name = f_name

    def set_last_name(self, l_name):
        self.l_name = l_name

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state_province(self, state):
        self.state_province = state

    def set_zip(self, zip):
        self.zip = zip

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email_address = email

    def set_country(self, country):
        self.country_region = country


if __name__ == "__main__":
    person = Person('FName', 'LName', 'address', 'city', 'state', 'zip', 'phone', 'email')
    print(person)

    print('*********************')
    print(person.get_name())
    print(person.get_address())
    print(person.get_city())
    print(person.get_state_province())
    print(person.get_zip())
    print(person.get_phone())
    print(person.get_email())
    print(person.get_country())
    print('*********************')
    person.country_region = 'UK'
    person.set_first_name('new_f_name')
    person.set_last_name('new_l_name')
    person.set_address('new_address')
    person.set_city('new_city')
    person.set_state_province('new_state')
    person.set_zip('new_zip')
    person.set_phone('new_phone')
    person.set_email('new_email')
    print(person)