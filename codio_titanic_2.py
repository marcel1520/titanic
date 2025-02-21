import json
from collections import Counter

with open("json_after.txt") as titanic_file:
    titanic_file_content = json.loads(titanic_file.read())
    sorted_content = (json.dumps(titanic_file_content, indent=4))
    #print(sorted_content)


'''
for country in titanic_file_content["data"]:
    countries_list.append(country["COUNTRY"])
set_countries = set(countries_list)
list_countries = sorted(list(set_countries))
for country in list_countries:
    print(country)
    
'''

def get_most_common(list_country):
    for country in titanic_file_content["data"]:
        list_country.append(country["COUNTRY"])
    user_prompt, top_num = input().split()
    top_num = int(top_num)
    counter = Counter(list_country)
    most_ships = counter.most_common(top_num)
    return most_ships

countries_list = []
most_common_get = get_most_common(countries_list)
print(most_common_get)