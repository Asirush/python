def add_country(countries_list: set, country_name: str) -> set:
    try:
        countries_list.update(country_name)
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
        matching_countries = [country for country in countries if search in country]
        return matching_countries
    except ValueError:
        return False

def check_country_exists(countries: set, country: str) -> bool:
    return country in countries

if "__main__" == __name__:
    countries = set()