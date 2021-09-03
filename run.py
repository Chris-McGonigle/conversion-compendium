def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("\nWelcome to Chris' Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 69)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = input("\nPlease enter your selection here:")

    if selection == ("1"):
        Temperature.convert_temp()
    elif selection == ("2"):
        convert_length()
    elif selection == ("3"):
        convert_volume()
    elif selection == ("4"):
        convert_currrency()


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
            self.temp_selection = input("Unit Type (C,F or K):").upper()
            self.temp_value = float(input("\nPlease enter the temperature to convert:"))
            results_temp()

        elif confirm_type == ("N"):
            main_menu()

    def results_temp():
        """
        Function to return the results of the temperature conversion to the terminal
        """

        if (temp_selection == "C"):
            print(f"\n {temp_value} in Celsius converts to:")



main_menu()
