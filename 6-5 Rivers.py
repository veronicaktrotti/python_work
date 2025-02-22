# Data dictionary
rivers_countries = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'vistula': 'poland'
}

def print_data(dictionary):
    # Loop to print a sentence about each river
    for river, country in dictionary.items():
        print(f"The {river.capitalize()} runs through {country.capitalize()}.")

    # Printing the included rivers and countries
    print("InRivers included in the dictionary:")
    for river in dictionary.keys():
        print(f"{river.capitalize()}")

    print("InCountries included in the dictionary:")
    for country in dictionary.values():
        print(f"{country.capitalize()}")

print_data(rivers_countries)