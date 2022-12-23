# A unit converter

# A welcome message
print("Welcome to your unit converter")

# A set of all the lenght measurements
# meter
# kilometer
# centimeter
# milimeter
# micrometer
# nanometer
# mile
# yard
# foot
# inch
# lightyear

conversions = {
    "meter": {
        "kilometer": 914,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,
    },
    "kilometer": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,        
    },
    "centimeter": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
    "milimeter": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
    "micrometer": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,          
    },
    "nanometer": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
    "mile": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
    "yard": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
    "foot": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,          
    },
    "inch": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,          
    },
    "lightyear": {
        "meter": 0,
        "centimeter": 91,
        "milimeter": 0.9,
        "micrometer": 914,
        "nanometer": 914,
        "mile": 914,
        "yard": 914,
        "foot": 914,
        "inch": 914,
        "lightyear": 914,  
    },
}

# The first question will ask what type of unit, length, temperature etc
type = input("What would you like to conver? Lengh, temperature etc (lenght is only available at the moment) your answer in lowercase: ")

if type == 'length':

# The first question will ask what do they want to convert, they can choose from a list
    question = input("""What unit would you like to convert? 
    - Meter(s)
    - Kilometer(s)
    - Centimeter(s)
    - Milimeter(s)
    - Micrometer(s)
    - Nanometer(s)
    - Mile(s)
    - Yard(s)
    - Foot(s)
    - Inch(s)
    - Light Year(s)
    Please type in lower case and the word of the initial unit: """)

# The second question will ask what they want to conveter the initial input into
    question2 = input(f"""What would you like to convert {question} into? 
    - Meter(s)
    - Kilometer(s)
    - Centimeter(s)
    - Milimeter(s)
    - Micrometer(s)
    - Nanometer(s)
    - Mile(s)
    - Yard(s)
    - Foot(s)
    - Inch(s)
    - Light Year(s)
    Please type in lower case and the word of the initial unit: """)

    question3 = float(input(f"How many {question}(s) would you like to convert into {question2}(s)? "))
    
    convert = question3 * conversions[question][question2]

    print(f"{question3} {question}s converted to {question2}s is {convert} {question}s")
else:
    print("Only lenght is available")



