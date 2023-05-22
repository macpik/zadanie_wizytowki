from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self,name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.label_lenght = 0

    def __repr__(self):
        return f'{self.phone} {self.name}'
    
    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name}”.'
    
    @property
    def label_length(self):
        return self._label_lenght
    
    @label_length.setter
    def label_lenght(self, a):
        a = (len(self.name))
        self._label_lenght = a

class BusinessContact(BaseContact):
    def __init__(self, occupation, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.company_phone = company_phone
        self.label_lenght = 0
        
    def __repr__(self):
        return f'{self.company_phone} {self.name}'
    
    def contact(self):
        return f'Wybieram numer {self.company_phone} i dzwonię do {self.name}”.'
    
    @property
    def label_length(self):
        return self._label_lenght
    
    @label_length.setter
    def label_lenght(self, a):
        a = (len(self.name))
        self._label_lenght = a

def create_contacts(type,amount):
    for _ in range(amount):
        if type == "base":
            print(BaseContact(name=fake.name(), email=fake.email(), phone=fake.phone_number()))
        elif type == "business":
            print(BusinessContact(name=fake.name(), email=fake.email(), phone=fake.phone_number(), occupation=fake.job(), company=fake.company(), company_phone=fake.phone_number()))

base_contact = BaseContact(name=fake.name(), email=fake.email(), phone=fake.phone_number())
business_contact = BusinessContact(name=fake.name(), email=fake.email(), phone=fake.phone_number(), occupation=fake.job(), company=fake.company(), company_phone=fake.phone_number())

lindsey_medina = BaseContact(name="Lindsey", email="LindseyDMedina@rhyta.com", phone="8828882882")
bradley_cooper = BusinessContact(name="Bradley", email="bradleycooper@google.com", phone = "12312312414", occupation="saler", company="Google", company_phone="999333444")

print(bradley_cooper.contact())
print(lindsey_medina.contact())
print(bradley_cooper.label_lenght)
print(base_contact.contact())
print(business_contact.contact())
print(base_contact.label_lenght)
print(business_contact.label_lenght)
print(create_contacts("base",10))

