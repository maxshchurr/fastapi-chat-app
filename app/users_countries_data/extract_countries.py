import os


def extract() -> list:
    # get current path
    current_dir = os.path.dirname(__file__)

    # get relative file path
    file_path = os.path.join(current_dir, 'users_countries.txt')

    with open(file_path, 'r') as users_countries:
        users_countries_list = [country.strip() for country in users_countries.readlines()]

    return users_countries_list


COUNTRIES = extract()
