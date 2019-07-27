import sqlite3
from util import restaurant_data

#
# Models for the /restaurants endpoint. Interface with the "restaurants" database table.
#

# Return a list of restaurants. 
# Max of 10 restaurants returned in no particule order.
def get_restaurants():
    # Connect to our db. 
    conn = sqlite3.connect("restaurants.db")

    return 200, 'TODO'

# Return a list of restaurants filtered by grade. 
# If grade given is B, then all grades below B are fair to return.
# Max of 10 restaurants returned in no particule order.
def filter_by_grade(grade):
    # Connect to our db. 
    conn = sqlite3.connect("restaurants.db")

    return 200, 'TODO'

# Return a list of restaurants filtered by cuisine type. 
# Max of 10 restaurants returned in no particule order.
def filter_by_cuisine(cuisine):
    # Connect to our db. 
    conn = sqlite3.connect("restaurants.db")

    return 200, 'TODO'

# Return a list of restaurants filtered by both cuisine type and grade. 
# If grade given is B, then all grades below B are fair to return.
# Max of 10 restaurants returned in no particule order.
def filter_by_cuisine_and_grade(cuisine, grade):
    # Connect to our db. 
    conn = sqlite3.connect("restaurants.db")

    return 200, 'TODO'
    # c.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password))

# Return a filtered list of restaurants based on cuisine type and/ot Health Department rating.
# Expects cuisine type and/or Health Department rating params.
# Returns a max of 10 filtered restaurants in no particular order.
def filter_restaurants(cuisine, grade):
    # Perform basic validation on the given params
    # TODO: Move validation to /server/handlers/restaurants.py

    # We should never pass this...
    if not cuisine and not grade:
        return 500, 'Error: internal server error.'

    # Quick validation
    if cuisine:
      if cuisine not in restaurant_data.cuisine_types:
        return 422, 'Error: grade param is invalid.'

    if grade:
      if grade not in restaurant_data.grade_types:
        return 422, 'Error: grade param is invalid.'

    # Filter by cuisine
    if cuisine and not grade:
        return filter_by_cuisine(cuisine)
    
    # Filter by grade
    if grade and not cuisine:
        return filter_by_grade(grade)

    # Filter by both
    return filter_by_cuisine_and_grade(cuisine, grade)
