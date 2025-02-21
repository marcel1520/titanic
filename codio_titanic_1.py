import json
from collections import Counter

'''reading the json file that holds the content'''
with open("json_after.txt", "r") as titanic_file:
    titanic_file_content = json.loads(titanic_file.read())
    sorted_content = (json.dumps(titanic_file_content, indent=4))


def opening_message(start_message):
    '''function for displaying the welcome message'''
    return input(start_message)


def choose_from_menu(empty_string):
    '''starting prompt for displaying the options menu'''
    return input(empty_string)


def display_options(print_message):
    '''function for displaying the options menu'''
    return print_message


def display_countries(data_dict, data_key, country_key):
    '''satisfying the first option of showing content from dictionary'''
    countries_list = []
    for country in data_dict[data_key]:
        countries_list.append(country[country_key])
    set_countries = set(countries_list)
    list_countries = list(sorted(set_countries))
    return list_countries


def get_most_common(list_country, top_num):
    '''satisfying the second option of showing most common content depending on user choice number'''
    counter = Counter(list_country)
    return counter.most_common(top_num)


def main():
    '''main function section 1 holds message strings, access data and list'''
    start_message = "Welcome to the Ships CLI! Enter 'help' to view available commands.\n\n"
    print_message = (
        "Available commands:\n"
        "help\n"
        "show_countries\n"
        "top_countries <num_countries>\n"
        "exit\n"
        )
    proceeding_message = "help"
    exiting_message = "exit"
    show_countries_message = "show_countries"
    show_top_countries_message = "top_countries"
    value_error_message = "Please provide number"
    invalid_command_message = "Please enter a valid command from the menu, type 'help' to view choices"
    empty_string = ""
    data_key = "data"
    country_key = "COUNTRY"
    list_country = []

    '''main function section 2 holding program flow'''
    message_opening = opening_message(start_message)
    if message_opening == proceeding_message:
        options_display = display_options(print_message)
        print(options_display)
        while True:
            from_menu_choose = choose_from_menu(empty_string)
            if from_menu_choose == show_countries_message:
                countries_display = display_countries(titanic_file_content, data_key, country_key)
                for country in countries_display:
                    print(country)
            elif from_menu_choose.startswith(show_top_countries_message):
                for country in titanic_file_content[data_key]:
                    list_country.append(country[country_key])
                try:
                    _, top_num = from_menu_choose.split()
                    top_num = int(top_num)
                    most_common_get = get_most_common(list_country, top_num)
                    for position in most_common_get:
                        print(" ".join(map(str, position)))
                except ValueError:
                    print(value_error_message)
            elif from_menu_choose == exiting_message:
                exit()
            else:
                print(invalid_command_message)
                print(print_message)


if __name__ == "__main__":
    main()