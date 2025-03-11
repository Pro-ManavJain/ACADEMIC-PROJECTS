from forex_python.converter import CurrencyRates, CurrencyCodes
import sys

class CurrencyConverter:
    def __init__(self):
        self.c = CurrencyRates()
        self.codes = CurrencyCodes()

    def get_currency_name(self, code):
        try:
            name = self.codes.get_currency_name(code.upper())
            if name is None:
                print(f"Error: '{code}' is not a valid currency code.")
            return name
        except Exception:
            print(f"Error: Unable to fetch currency name for '{code}'.")
            return None

    def convert_currency(self, from_currency, to_currency, amount):
        try:
            converted_amount = self.c.convert(from_currency.upper(), to_currency.upper(), amount)
            return converted_amount
        except Exception:
            print("Error: Unable to fetch conversion rate. Please check your internet connection or try later.")
            return None

    def display_conversion(self, from_currency, to_currency, amount):
        print("\nPerforming conversion...")
        if not self.get_currency_name(from_currency) or not self.get_currency_name(to_currency):
            print("Conversion failed due to invalid currency code.")
            return

        converted = self.convert_currency(from_currency, to_currency, amount)
        if converted is not None:
            print(f"\n{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print("Conversion failed.")

def main():
    print("Welcome to the Real-Time Currency Converter!")
    converter = CurrencyConverter()

    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            from_currency = input("Enter the source currency: ").strip()
            to_currency = input("Enter the target currency: ").strip()
            try:
                amount = float(input("Enter the amount: "))
                if amount <= 0:
                    print("Amount must be greater than zero. Please try again.")
                    continue
                converter.display_conversion(from_currency, to_currency, amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == '2':
            print("Exiting the Currency Converter")
            sys.exit()

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
