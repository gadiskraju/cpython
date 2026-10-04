def print_menu():
    print("\n=== Python Unit Converter ===")
    print("1. Length (Meters, Kilometers, Miles, Feet)")
    print("2. Weight (Kilograms, Grams, Pounds, Ounces)")
    print("3. Temperature (Celsius, Fahrenheit, Kelvin)")
    print("0. Exit")

def convert_length():
    # Base unit: Meter
    factors = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.34,
        "feet": 0.3048
    }
    
    print("\nAvailable Length Units:", ", ".join(factors.keys()))
    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()
    
    if from_unit not in factors or to_unit not in factors:
        print("❌ Invalid units selected.")
        return
        
    try:
        value = float(input(f"Enter value in {from_unit}: "))
        # Convert to base unit (meters), then to target unit
        value_in_meters = value * factors[from_unit]
        result = value_in_meters / factors[to_unit]
        print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    except ValueError:
        print("❌ Please enter a valid number.")

def convert_weight():
    # Base unit: Kilogram
    factors = {
        "kilograms": 1.0,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    }
    
    print("\nAvailable Weight Units:", ", ".join(factors.keys()))
    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()
    
    if from_unit not in factors or to_unit not in factors:
        print("❌ Invalid units selected.")
        return
        
    try:
        value = float(input(f"Enter value in {from_unit}: "))
        # Convert to base unit (kilograms), then to target unit
        value_in_kg = value * factors[from_unit]
        result = value_in_kg / factors[to_unit]
        print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    except ValueError:
        print("❌ Please enter a valid number.")

def convert_temperature():
    # Temperature requires formulas instead of straight multiplication factors
    print("\nAvailable Temperature Units: celsius, fahrenheit, kelvin")
    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()
    
    try:
        value = float(input(f"Enter value in {from_unit}: "))
        
        # First convert everything to Celsius
        if from_unit == "celsius":
            celsius = value
        elif from_unit == "fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "kelvin":
            celsius = value - 273.15
        else:
            print("❌ Invalid source unit.")
            return

        # Convert Celsius to the target unit
        if to_unit == "celsius":
            result = celsius
        elif to_unit == "fahrenheit":
            result = (celsius * 9/5) + 32
        elif to_unit == "kelvin":
            result = celsius + 273.15
        else:
            print("❌ Invalid target unit.")
            return
            
        print(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        print_menu()
        choice = input("\nSelect a category (0-3): ").strip()
        
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
