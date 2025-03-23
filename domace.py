import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca

    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    pass


# TODO: Implementirajte funkciju za upravljanje proizvodima.
customers = []
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    while True:
        print('\nIzbornik za upravljanje kupcima:')
        print('1. Dodajte novog kupca')
        print('2. Pregledajte sve kupce')
        print('3. Izlaz')

        choice = input('Unesite svoj izbor (1 - 3): ')
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
        if choice == '1':
            name = input('Unesite naziv novog kupca: ')
            email = input('Unesite e-mail novog kupca: ')
            customer_id = input('Unesite ID broj novog kupca: ')
            
            new_customer = {
                'name': name,
                'email': email,
                'vat_id': customer_id
            }
            
            customers.append(new_customer)
            print(f'Novi kupac {name} dodan!')
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
        elif choice == '2':   
            if customers:
                print('\nLista kupaca:')
                for x, customer in enumerate(customers, 1):
                    print(f'{x}. Ime: {customer['name']}, Email: {customer['email']}, ID broj: {customer['vat_id']}')
            else:
                print('Kupac nije pronađen!')

        elif choice == '3':
            print('Izlaz iz aplikacije')
            break
        
        else:
            print('Krivi odabir. Molimo unesite 1, 2, or 3.')
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    while True:
        print("\nUpravljanje kupcima")
        print("1. Dodajte novog kupca")
        print("2. Pregledajte sve kupce")
        print("3. Izlaz")

        choice = input('Unesite svoj izbor: ')
        if choice == '1':
            name = input('Unesite ime kupca: ')
            email = input('Unesite email adresu kupca: ')
            vat_id = input('Unesite VAT_ID kupca: ')
        
            customer = {
                'name': name,
                'email': email,
                'vat_id': vat_id
            }
            customers.append(customer)
            print('Kupac je uspješno dodan!')
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
