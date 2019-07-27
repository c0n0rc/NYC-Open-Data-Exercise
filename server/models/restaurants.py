import json
import sqlite3
from sqlite3 import Error
from util import restaurant_data

#
# Models for the /restaurants endpoint. Interface with the "restaurants" database table.
#

# Return a list of restaurants. 
# Max of 10 restaurants returned in no particule order.
def get_restaurants():
    # Connect to our db. 
    # TODO: Make this a utility function.
    try:
        conn = sqlite3.connect("restaurants.db")
    except Error as e:
        print(e)
        return 500, 'Internal error connecting to the database.'

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM restaurants LIMIT 10')
    rows = cursor.fetchall()
    conn.close()

    # Reformat results to JSON output.
    data = []

    for row in rows:
        entry = {
            'name': row[0],
            'address': str(row[2]) + ' ' + row[3] + ', ' + row[1] + ', ' + str(row[4]), 
            'phone': str(row[5]),
            'cuisine_type': row[6],
            'grade': row[7]
        }
        data.append(entry)

    response = { 'data' : data }
    json_response = json.dumps(response)

    return 200, json_response

# Return a list of restaurants filtered by grade. 
# If grade given is B, then all grades >= B are fair to return.
# Max of 10 restaurants returned in no particule order.
def filter_by_grade(grade):
    # Connect to our db. 
    try:
        conn = sqlite3.connect("restaurants.db")
    except Error as e:
        print(e)
        return 500, 'Internal error connecting to the database.'

    cursor = conn.cursor()

    # Ex: if the grade given is C, return A, B, and C. Otherwise just return grade.
    grade_range = ['A', 'B', 'C']

    if grade in grade_range:
        # Get list of acceptable grades
        grades = grade_range[:grade_range.index(grade) + 1]

        # Ref: https://stackoverflow.com/questions/5766230/select-from-sqlite-table-where-rowid-in-list-using-python-sqlite3-db-api-2-0
        sql_query = f"SELECT * FROM restaurants WHERE GRADE IN ({','.join(['?'] * len(grades))}) LIMIT 10"
        cursor.execute(sql_query, grades,)
    
    else:
        cursor.execute('SELECT * FROM restaurants WHERE GRADE = ? LIMIT 10', (grade,))
    
    rows = cursor.fetchall()
    conn.close()
    
    # Reformat results to JSON output.
    data = []

    for row in rows:
        entry = {
            'name': row[0],
            'address': str(row[2]) + ' ' + row[3] + ', ' + row[1] + ', ' + str(row[4]), 
            'phone': str(row[5]),
            'cuisine_type': row[6],
            'grade': row[7]
        }
        data.append(entry)

    response = { 'data' : data }
    json_response = json.dumps(response)

    return 200, json_response

# Return a list of restaurants filtered by cuisine type. 
# Max of 10 restaurants returned in no particule order.
def filter_by_cuisine(cuisine):
    # Connect to our db. 
    try:
        conn = sqlite3.connect("restaurants.db")
    except Error as e:
        print(e)
        return 500, 'Internal error connecting to the database.'

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM restaurants WHERE CUISINE_DESCRIPTION = ? LIMIT 10', (cuisine,))
    rows = cursor.fetchall()
    conn.close()

    # Reformat results to JSON output.
    data = []

    for row in rows:
        entry = {
            'name': row[0],
            'address': str(row[2]) + ' ' + row[3] + ', ' + row[1] + ', ' + str(row[4]), 
            'phone': str(row[5]),
            'cuisine_type': row[6],
            'grade': row[7]
        }
        data.append(entry)

    response = { 'data' : data }
    json_response = json.dumps(response)

    return 200, json_response

# Return a list of restaurants filtered by both cuisine type and grade. 
# If grade given is B, then all grades >= B are fair to return.
# Max of 10 restaurants returned in no particule order.
def filter_by_cuisine_and_grade(cuisine, grade):
    # Connect to our db. 
    try:
        conn = sqlite3.connect("restaurants.db")
    except Error as e:
        print(e)
        return 500, 'Internal error connecting to the database.'

    cursor = conn.cursor()

    # Ex: if the grade given is C, return A, B, and C. Otherwise just return grade.
    grade_range = ['A', 'B', 'C']

    if grade in grade_range:
        # Get list of acceptable grades
        grades = grade_range[:grade_range.index(grade) + 1]

        # Ref: https://stackoverflow.com/questions/5766230/select-from-sqlite-table-where-rowid-in-list-using-python-sqlite3-db-api-2-0
        sql_query  = f"SELECT * FROM restaurants WHERE CUISINE_DESCRIPTION = ? and GRADE IN ({','.join(['?'] * len(grades))}) LIMIT 10"
        sql_params = [cuisine] + grades 
        cursor.execute(sql_query, sql_params)
    
    else:
        cursor.execute('SELECT * FROM restaurants WHERE CUISINE_DESCRIPTION = ? and GRADE = ? LIMIT 10', (cuisine, grade,))
    
    rows = cursor.fetchall()
    conn.close()

    # Reformat results to JSON output.
    # TODO: Make this a utility function.
    data = []

    for row in rows:
        entry = {
            'name': row[0],
            'address': str(row[2]) + ' ' + row[3] + ', ' + row[1] + ', ' + str(row[4]), 
            'phone': str(row[5]),
            'cuisine_type': row[6],
            'grade': row[7]
        }
        data.append(entry)

    response = { 'data' : data }
    json_response = json.dumps(response)

    return 200, json_response

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
