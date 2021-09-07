import pyinputplus as pyip


def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("\nWelcome to Chris's Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 45)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = pyip.inputNum("\nPlease enter your selection here:", lessThan=5)

    if selection == (1):
        Temperature.convert_temp()
    elif selection == (2):
        Length.convert_length()


class Temperature:
    def convert_temp():
        """
        Function to convert temperatures. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Temperature. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting unit\n")
            temp_selection = pyip.inputMenu(["Celsius", "Fahrenheit", "Kelvin"], numbered=True)
            temp_value = pyip.inputNum("\nPlease enter the temperature to convert:")
            if temp_selection == ("Celsius"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.celsius2fahrenheit(temp_value)} Fahrenheit")
                print(f"\n{Temperature.celsius2kelvin(temp_value)} Kelvin")
                Temperature.run_again()
            elif temp_selection == ("Fahrenheit"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.fahrenheit2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.fahrenheit2kelvin(temp_value)} Kelvin")
                Temperature.run_again()
            elif temp_selection == ("Kelvin"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.kelvin2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.kelvin2fahrenheit(temp_value)} Fahrenheit")
                Temperature.run_again()
        elif confirm_type == ("no"):
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

    def run_again():
        """
        Refactored function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Temperature?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Temperature.convert_temp()
        else:
            main_menu()


class Length:
    def convert_length():
        """
        Function to convert length. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Length. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting unit\n")
            len_selection = pyip.inputMenu(["Nanometre", "Micrometre", "Millimetre", "Centimetre", "Metre", "Kilometre", "Inch", "Foot", "Yard", "Mile", "Nautical Mile"], numbered=True)
            len_value = pyip.inputNum("\nPlease enter the length to convert:")

            length_conversion_factors = {
                'kilometre': {'metre': 0.001, 'centimetre': 0.00001, 'millimetre': 0.000001,
                'micrometre': 0.000000001, 'nanometre': 0.000000000001, 'mile': 1.60934,
                'yard': 0.000914397727272727, 'foot': 0.000304799242424242, 'inch': 2.53999368686869,
                'nautical mile': 1.852},

                'metre': {'kilometre': 1000, 'centimetre': 0.01, 'millimetre': 0.001, 'micrometre': 0.000001,
                'nanometre': 0.000000001, 'mile': 1609.34, 'yard': 0.914397727272727, 'foot': 0.304799242424242,
                'inch': 0.0253999368686869, 'nautical mile': 1852},

                'centimetre': {'kilometre': 100000, 'metre': 100, 'millimetre': 0.1,
                'micrometre': 0.0001, 'nanometre': 0.0000001, 'mile': 160934,
                'yard': 91.4397727272727, 'foot': 30.4799242424242, 'inch': 2.53999368686869,
                'nautical mile': 185200},

                'millimetre': {'kilometre': 1000000, 'metre': 1000, 'centimetre': 10, 
                'micrometre': 0.001, 'nanometre': 0.000001, 'mile': 1609340,
                'yard': 914.397727272727, 'foot': 304.799242424242, 'inch': 25.3999368686869,
                'nautical mile': 1852000},

                'micrometre': {'kilometre': 1000000000, 'metre': 1000000, 'centimetre': 10000, 'millimetre': '1000',
                'nanometre': 0.001, 'mile': 1609340000, 'yard': 914397.727272727,
                'foot': 304799.242424242, 'inch': 25399.9368686869, 'nautical mile': 1852000000},

                'nanometre': {'kilometre': 1000000000000, 'metre': 1000000000, 'centimetre': 10000000,
                'millimetre': 1000000, 'micrometre': 1000, 'mile': 1609340000000,
                'yard': 914397727.272727, 'foot': 304799242.424242, 'inch': 25399936.8686869,
                'nautical mile': 1852000000000},

                'mile': {'kilometre': 0.621371, 'metre': 0.000621371, 'centimetre': 0.00000621371, 'millimetre': 0.000000621371,
                'micrometre': 0.000000000621371, 'nanometre': 0.000000000000621371, 'yard': 0.000568180230193182,
                'foot': 0.000189393410064394, 'inch': 1.57827841720328E-05, 'nautical mile': 1.150779092},

                'yard': {'kilometre': 1093.61296, 'metre': 1.09361296, 'centimetre': 0.0109361296, 'millimetre': 0.00109361296,
                'micrometre': 0.00000109361296, 'nanometre': 0.00000000109361296, 'mile': 1760, 'foot': 0.333332401713333, 'inch': 0.0277777001427778, 'nautical mile': 2025.37120192},

                'foot': {'kilometre': 3280.83888, 'metre': 3.28083888, 'centimetre': '0.0328083888', 'millimetre': '0.00328083888',
                'micrometre': 0.00000328083888, 'nanometre': 0.00000000328083888, 'mile': '5280', 'yard': '3',
                'inch': 0.0833331004283333, 'nautical mile': 6076.11360576},

                'inch': {'kilometre': 39370.06656, 'metre': 39.37006656, 'centimetre': 0.3937006656, 'millimetre': 0.03937006656,
                'micrometre': 0.00003937006656, 'nanometre': 0.00000003937006656, 'mile': 63360, 'yard': 36,
                'foot': 12, 'nautical mile': 72913.36326912},

                'nautical mile': {'kilometre': 0.539957, 'metre': 0.000539957, 'centimetre': 0.00000539957,
                'millimetre': 0.000000539957, 'micrometre': 0.000000000539957, 'nanometre': 0.000000000000539957, 'mile-nautical mile': 0.86897439838,
                'yard': 0.000493735453625, 'foot': 0.000164578484541667,
                'inch': 1.37148737118056E-05, },
            }
            length_key = len_selection.lower()

            print(f"\n{len_value} {len_selection}s converted equals:")

            if length_key in length_conversion_factors:
                for value in length_conversion_factors[length_key]:
                    conv_value = len_value / float(length_conversion_factors[length_key][value])
                    print(f"\n{conv_value} {value}s")
            Length.run_again()        
                    
        elif confirm_type == ("no"):
            main_menu()

    def run_again():
        """
        Function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Length?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Length.convert_length()
        else:
            main_menu()

main_menu()
