import os

def add_country(countries_list: set, country_name: str) -> set:
    try:
        countries_list.add(country_name)
        return countries_list
    except ValueError:
        return False
    
def delete_country(countries_list: set, country_name: str) -> set:
    try:
        countries_list.remove(country_name)
        return countries_list
    except ValueError:
        return False
    
def search_element(countries_list: set, search: str) -> set:
    try:
        matching_countries = [country for country in countries_list if search in country]
        return matching_countries
    except ValueError:
        return False

def check_country_exists(countries: set, country: str) -> bool:
    return country in countries

def main_menu(countries: set):
    while(True):
        print("Select action:")
        print("1. List countries")
        print("2. Add country")
        print("3. Delete country")
        print("4. Search")
        print("5. Check country existence")
        print("6. Exit")
        match int(input()):
            case 1: 
                os.system('clear')
                print(countries)
            case 2: 
                os.system('clear')
                print("Enter country name")
                countname = input() 
                print("Enter capital name")
                capname = input()
                name = (countname, capname)
                print(add_country(countries, name))
            case 3: 
                os.system('clear')
                print("Enter country name")
                countname = input() 
                name = (countname, capname)
                print(delete_country(countries, name))
            case 4:
                os.system('clear')
                print("Enter searching data")
                countname = input() 
                name = (countname, capname)
                print(search_element(countries, name))
            case 5:
                os.system('clear')
                print("Enter country name")
                countname = input() 
                name = (countname, capname)
                print(check_country_exists(countries, name))
            case 6:
                break

if "__main__" == __name__:
    countries = set()
    main_menu(countries)