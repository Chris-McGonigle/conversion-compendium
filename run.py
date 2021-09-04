def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("\nWelcome to Chris' Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 45)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = input("\nPlease enter your selection here:")

    if selection == ("1"):
        Temperature.convert_temp()


class Temperature:
    def convert_temp():
        """
        Function to convert temperatures. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Temperature. Is this correct?")

        confirm_type = input("\nY/N:").upper()

        if confirm_type == ("Y"):
            print("\nSelect starting unit in Celsius, Fahrenheit or Kelvin")
            temp_selection = input("Unit Type (C,F or K):").upper()
            temp_value = float(input("\nPlease enter the temperature to convert:"))
            if temp_selection == ("C"):
                print(f"\n{temp_value}{temp_selection} converted equals:")
                print(f"\n{Temperature.celsius2fahrenheit(temp_value)} Fahrenheit")
                print(f"\n{Temperature.celsius2kelvin(temp_value)} Kelvin")
                print("-" * 45)
                print("\nWould you like to convert another Temperature?")
                convert_again = input("\nY/N:").upper()
                if convert_again == ("Y"):
                    Temperature.convert_temp()
                else: main_menu()
            elif temp_selection == ("F"):
                print(f"\n{temp_value}{temp_selection} converted equals:")
                print(f"\n{Temperature.fahrenheit2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.fahrenheit2kelvin(temp_value)} Kelvin")
                print("-" * 45)
                print("\nWould you like to convert another Temperature?")
                convert_again = input("\nY/N:").upper()
                if convert_again == ("Y"):
                    Temperature.convert_temp()
                else: main_menu()
            elif temp_selection == ("K"):
                print(f"\n{temp_value}{temp_selection} converted equals:")
                print(f"\n{Temperature.kelvin2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.kelvin2fahrenheit(temp_value)} Fahrenheit")
                print("-" * 45)
                print("\nWould you like to convert another Temperature?")
                convert_again = input("\nY/N:").upper()
                if convert_again == ("Y"):
                    Temperature.convert_temp()
                else: main_menu()         


        elif confirm_type == ("N"):
            main_menu()

    def celsius2kelvin(temp_value):
        """
        Conversion formula for Celsius to Kelvin
        """
        c2k = temp_value + 273.15
        return float("{:.2f}".format(c2k))

    def celsius2fahrenheit(temp_value):
        """
        Conversion formula for Celsius to Fahrenheit
        """
        c2f = (temp_value * 9/5) + 32
        return float("{:.2f}".format(c2f))

    def fahrenheit2celsius(temp_value):
        """
        Conversion formula for Fahrenheit to Celsius
        """
        f2c = (temp_value - 32) * 5/9
        return float("{:.2f}".format(f2c))

    def fahrenheit2kelvin(temp_value):
        """
        Conversion formula for Fahrenheit to Kelvin
        """
        f2k = (temp_value + 459.67) / 1.8
        return float("{:.2f}".format(f2k))

    def kelvin2celsius(temp_value):
        """
        Conversion formula for Kelvin to Celsius
        """
        k2c = temp_value - 273.15
        return float("{:.2f}".format(k2c))

    def kelvin2fahrenheit(temp_value):
        """
        Conversion formula for Kelvin to Fahrenheit
        """
        k2f = (temp_value * 1.8) - 459.67
        return float("{:.2f}".format(k2f))    

main_menu()

