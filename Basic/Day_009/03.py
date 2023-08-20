travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#to be added to the travel_log. 👇
def add_new_country(country_name, number_of_visits, cities_visited):
    new_country = {}
    new_country = {
        "country": country_name,
        "visits": number_of_visits,
        "cities": cities_visited
    }
    travel_log.append(new_country)
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
