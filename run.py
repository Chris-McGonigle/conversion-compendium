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

            conversion_factors = {
                'kilometre-kilometre': '1', 'metre-kilometre': '0.001', 'centimetre-kilometre': '0.00001', 'millimetre-kilometre': '0.000001',
                'micrometre-kilometre': '0.000000001', 'nanometre-kilometre': '0.000000000001', 'mile-kilometre': '1.60934',
                'yard-kilometre': '0.000914397727272727', 'foot-kilometre': '0.000304799242424242', 'inch-kilometre': '2.53999368686869',
                'nautical mile-kilometre': '1.852',

                'kilometre-metre': '1000', 'metre-metre': '1', 'centimetre-metre': '0.01', 'millimetre-metre': '0.001', 'micrometre-metre': '0.000001',
                'nanometre-metre': '0.000000001', 'mile-metre': '1609.34', 'yard-metre': '0.914397727272727', 'foot-metre': '0.304799242424242',
                'inch-metre': '0.0253999368686869', 'nautical mile-metre': '1852',

                'kilometre-centimetre': '100000', 'metre-centimetre': '100', 'centimetre-centimetre': '1', 'millimetre-centimetre': '0.1',
                'micrometre-centimetre': '0.0001', 'nanometre-centimetre': '0.0000001', 'mile-centimetre': '160934',
                'yard-centimetre': '91.4397727272727', 'foot-centimetre': '30.4799242424242', 'inch-centimetre': '2.53999368686869',
                'nautical mile-centimetre': '185200',

                'kilometre-millimetre': '1000000', 'metre-millimetre': '1000', 'centimetre-millimetre': '10', 'millimetre-millimetre': 1,
                'micrometre-millimetre': '0.001', 'nanometre-millimetre': '0.000001', 'mile-millimetre': '1609340',
                'yard-millimetre': '914.397727272727', 'foot-millimetre': '304.799242424242', 'inch-millimetre': '25.3999368686869',
                'nautical mile-millimetre': '1852000',

                'kilometre-micrometre': '1000000000', 'metre-micrometre': '1000000', 'centimetre-micrometre': '10000', 'millimetre-micrometre': '1000',
                'micrometre-micrometre': '1', 'nanometre-micrometre': '0.001', 'mile-micrometre': '1609340000', 'yard-micrometre': '914397.727272727',
                'foot-micrometre': '304799.242424242', 'inch-micrometre': '25399.9368686869', 'nautical mile-micrometre': '1852000000',

                'kilometre-nanometre': '1000000000000', 'metre-nanometre': '1000000000', 'centimetre-nanometre': '10000000',
                'millimetre-nanometre': '1000000', 'micrometre-nanometre': '1000', 'nanometre-nanometre': 1, 'mile-nanometre': '1609340000000',
                'yard-nanometre': '914397727.272727', 'foot-nanometre': '304799242.424242', 'inch-nanometre': '25399936.8686869',
                'nautical mile-nanometre': '1852000000000',

                'kilometre-mile': '0.621371', 'metre-mile': '0.000621371', 'centimetre-mile': '0.00000621371', 'millimetre-mile': '0.000000621371',
                'micrometre-mile': '0.000000000621371', 'nanometre-mile': '0.000000000000621371', 'mile-mile': '1', 'yard-mile': '0.000568180230193182',
                'foot-mile': '0.000189393410064394', 'inch-mile': '1.57827841720328E-05', 'nautical mile-mile': '1.150779092',

                'kilometre-yard': '1093.61296', 'metre-yard': '1.09361296', 'centimetre-yard': '0.0109361296', 'millimetre-yard': '0.00109361296',
                'micrometre-yard': '0.00000109361296', 'nanometre-yard': '0.00000000109361296', 'mile-yard': '1760', 'yard-yard': '1',
                'foot-yard': '0.333332401713333', 'inch-yard': '0.0277777001427778', 'nautical mile-yard': '2025.37120192',

                'kilometre-foot': '3280.83888', 'metre-foot': '3.28083888', 'centimetre-foot': '0.0328083888', 'millimetre-foot': '0.00328083888',
                'micrometre-foot': '0.00000328083888', 'nanometre-foot': '0.00000000328083888', 'mile-foot': '5280', 'yard-foot': '3', 'foot-foot': '1',
                'inch-foot': '0.0833331004283333', 'nautical mile-foot': '6076.11360576',

                'kilometre-inch': '39370.06656', 'metre-inch': '39.37006656', 'centimetre-inch': '0.3937006656', 'millimetre-inch': '0.03937006656',
                'micrometre-inch': '0.00003937006656', 'nanometre-inch': '0.00000003937006656', 'mile-inch': '63360', 'yard-inch': '36',
                'foot-inch': '12', 'inch-inch': '1', 'nautical mile-inch': '72913.36326912',

                'kilometre-nautical mile': '0.539957', 'metre-nautical mile': '0.000539957', 'centimetre-nautical mile': '0.00000539957',
                'millimetre-nautical mile': '0.000000539957', 'micrometre-nautical mile': '0.000000000539957',
                'nanometre-nautical mile': '0.000000000000539957', 'mile-nautical mile': '0.86897439838',
                'yard-nautical mile': '0.000493735453625', 'foot-nautical mile': '0.000164578484541667',
                'inch-nautical mile': '1.37148737118056E-05', 'nautical mile-nautical mile': 1
            
        
            if (len_selection in conversion_factors):
                print(f"\n{len_value} {len_selection} converted equals:")
                print('{conv_value:.3f}'.format(conv_type=my_key, conv_value=len_value * conversion_factors[len_selection])))
            
            }



        elif confirm_type == ("no"):
            main_menu()


main_menu()
