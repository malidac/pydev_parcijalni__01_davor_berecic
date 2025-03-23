def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    while True:
        print("\nCustomer Management")
        print("1. Add New Customer")
        print("2. View All Customers")
        print("3. Exit")

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