import pickle


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_disk(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_disk(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, query):
        results = []
        query = query.lower()
        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        return results

    @staticmethod
    def validate_name(name):
        if not name.isalpha() or not name.istitle():
            raise ValueError("Некоректне ім'я. Ім'я має містити лише літери та починатися з великої літери.")

    @staticmethod
    def validate_phone_number(phone_number):
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValueError("Некоректний номер телефону. Номер має містити рівно 10 цифр.")


address_book = AddressBook()

address_book.load_from_disk('address_book.pkl')

while True:
    print("1. Додати контакт")
    print("2. Пошук контакту")
    print("3. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == '1':
        while True:
            name = input("Введіть ім'я: ")
            try:
                AddressBook.validate_name(name)
                break
            except ValueError as e:
                print(str(e))

        while True:
            phone_number = input("Введіть номер телефону: ")
            try:
                AddressBook.validate_phone_number(phone_number)
                break
            except ValueError as e:
                print(str(e))

        contact = Contact(name, phone_number)
        address_book.add_contact(contact)
        print("Контакт додано!")

    elif choice == '2':
        query = input("Введіть запит для пошуку: ")
        results = address_book.search_contacts(query)
        if results:
            print("Результати пошуку:")
            for result in results:
                print(f"Ім'я: {result.name}, Телефон: {result.phone_number}")
        else:
            print("Контакти не знайдені.")

    elif choice == '3':
        address_book.save_to_disk('address_book.pkl')
        print("Дані збережено. Вихід з програми.")
        break

    else:
        print("Невідома опція. Будь ласка, виберіть інше.")