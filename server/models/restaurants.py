
from util import restaurant_data

#
# Models for the /restaurants endpoint. Interface with the "restaurants" database table.
#

# Return a list of restaurants. 
# Max of 50 restaurants in no particular order.
def get_restaurants():
    return 200, 'TODO'


# Return a filtered list of restaurants based on cuisine type and Health Department rating.
# Expects both cuisine type and Health Department rating params.
# Returns a max of 50 filtered restaurants in no particular order.
def filter_restaurants(cuisine, grade):
    # Perform basic validation on the given params
    # TODO: Move validation to /server/handlers/restaurants.py
    if cuisine:
      if cuisine not in restaurant_data.cuisine_types:
        return 422, 'Error: grade param is invalid.'

    if grade:
      if grade not in restaurant_data.grade_types:
        return 422, 'Error: grade param is invalid.'

    return 200, 'TODO'

    # c.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password))
