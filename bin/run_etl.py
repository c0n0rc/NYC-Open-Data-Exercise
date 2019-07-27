import sqlite3
import pandas as pd

#
# Script to populate a sqlite3 database given a cleaned .csv file. 
# Creates a "restaurant" table.
#

# Connect to the db.
conn = sqlite3.connect("restaurants.db")

print('Connecting to the database.')

print('Reading the clearn .csv file...')

# TODO: Use sys for path
df = pd.read_csv('data/cleaned_data.csv')

print(df)

print('Populating the data table...')

# Schema ex: DBA, BORO, BUILDING, STREET, ZIPCODE, PHONE, CUISINE DESCRIPTION, GRADE, CLOSED, INSPECTED
# Data ex: MORRIS PARK BAKE SHOP, BRONX, 1007, MORRIS PARK AVE, 10462.0, 7188924968, bakery, A, False, True
conn.execute('''CREATE TABLE restaurants (DBA text, BORO text, BUILDING integer, STREET text, ZIPCODE integer, PHONE integer, CUISINE_DESCRIPTION text, GRADE text, CLOSED text, INSPECTED text)''')

# Populate using a dataframe.
# TODO: Is this one transaction?
df.to_sql('restaurants', conn, if_exists = 'replace')

conn.commit()

print('Connection committed.')

conn.close()

print('Connection closed.')
