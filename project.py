import json
import os

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Customer(ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone})"

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        return Customer(data["customer_id"], data["name"], data["email"], data["phone"])

class CRMSystem:
    def __init__(self, data_file="customers.json"):
        self.data_file = data_file
        self.customers = self.load_data()

    def load_data(self):
        """Load customer data from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return [Customer.from_dict(data) for data in json.load(file)]
        return []

    def save_data(self):
        """Save all customers to the JSON file."""
        with open(self.data_file, "w") as file:
            json.dump([customer.to_dict() for customer in self.customers], file, indent=4)

    def add_customer(self, name, email, phone):
        """Add a new customer."""
        customer_id = len(self.customers) + 1  # Simple customer ID generation
        new_customer = Customer(customer_id, name, email, phone)
        self.customers.append(new_customer)
        self.save_data()
        print(f"Customer {name} added successfully.")

    def view_customers(self):
        """View all customers."""
        if not self.customers:
            print("No customers in the database.")
        else:
            for customer in self.customers:
                print(customer)

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        """Update an existing customer's information."""
        customer = self.get_customer_by_id(customer_id)
        if customer:
            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone
            self.save_data()
            print(f"Customer {customer_id} updated successfully.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def delete_customer(self, customer_id):
        """Delete a customer by ID."""
        customer = self.get_customer_by_id(customer_id)
        if customer:
            self.customers.remove(customer)
            self.save_data()
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def get_customer_by_id(self, customer_id):
        """Get a customer by ID."""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

# Main program
def main():
    crm = CRMSystem()

    while True:
        print("\nCRM System:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            crm.add_customer(name, email, phone)
        elif choice == '2':
            crm.view_customers()
        elif choice == '3':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            crm.update_customer(customer_id, name or None, email or None, phone or None)
        elif choice == '4':
            customer_id = int(input("Enter customer ID to delete: "))
            crm.delete_customer(customer_id)
        elif choice == '5':
            print("Exiting CRM system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
