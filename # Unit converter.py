# Unit converter

# Define a dictionary of unit conversions
conversions = {
    "inches": {
        "millimeters": 25.4,
        "centimeters": 2.54,
        "meters": 0.0254
    },
    "feet": {
        "millimeters": 304.8,
        "centimeters": 30.48,
        "meters": 0.3048
    },
    "yards": {
        "millimeters": 914.4,
        "centimeters": 91.44,
        "meters": 0.9144
    }
}

# Ask the user for the value and units to convert
value = float(input("Enter the value to convert: "))
units = input("Enter the units to convert (inches, feet, or yards): ")

# Ask the user for the units to convert to
convert_to = input("Enter the units to convert to (millimeters, centimeters, or meters): ")

# Convert the value
converted_value = value * conversions[units][convert_to]

# Print the converted value
print(f"{value} {units} is equal to {converted_value} {convert_to}.")
