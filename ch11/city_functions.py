def city_country(city, country, population=0):
    address = city.title() + ', ' + country.title()
    if population:
        address += ' - ' + str(population)
    return address