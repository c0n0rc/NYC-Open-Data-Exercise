### Overview

This project reads in data from an [NYC Open Data Set](https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv), runs it through an ETL pipeline, and stores the clean data in a sqlite3 database. With the database populated, users can make requests to an API endpoint that, given a Health Department grade and/or cuisine type, will return a list of 10 max establishments for a given cuisine which satisfy said Health Department rating.

---

### To Build

This project was developed in Python 3 in a Python virtual environment. To install a virtual environment, follow the instructions [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

To activate an environment and install the necessary packages, run:

```
source env/bin/activate
pip install -r requirements.txt
```

To get the server running, run:
```
python3 main.py
```

To run the IPython notebook, run:
```
jupyter notebook etl_notebook.ipynb
```

The notebook creates a cleaned .csv file. To populate a database with the clean file, run:
```
python3 bin/run_etl.py
```

### To Test


In the test directory, there is a simple script to test the API endpoint with a different parameters. To test, run:
```
python3 test.py
``` 

---

### Docs and Usage

The server accepts requests on port 3003. Below is a description of the API. 

#### localhost:3003/v1/restaurants

**Request Type:** `GET`

**Params:**

`cuisine` - A filter. Results returned will have this restaurant cuisine type. Optional.

`grade` - A filter. Results returned will have this Health Department grade or higher. Optional.


**Result:**
Returns a list of restaurants found in the database. If `cuisine` and/or `grade` are provided, returns a list of 
restaurants of a given `cuisine` type that have Health Department ratings of `grade` or higher. Max limit of 10 results. 
Order not quaranteed. 

**Example Usage**

`curl -k localhost:3003/v1/restaurants -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

```
{
  "data": [
    {
      "name": "MORRIS PARK BAKE SHOP",
      "address": "1007 MORRIS PARK AVE, BRONX, 10462",
      "phone": "7188924968",
      "cuisine_type": "bakery",
      "grade": "A"
    },
    {
      "name": "WENDY'S",
      "address": "469 FLATBUSH AVENUE, BROOKLYN, 11225",
      "phone": "7182875005",
      "cuisine_type": "hamburgers",
      "grade": "A"
    },
    {
      "name": "DJ REYNOLDS PUB AND RESTAURANT",
      "address": "351 WEST   57 STREET, MANHATTAN, 10019",
      "phone": "2122452912",
      "cuisine_type": "irish",
      "grade": "A"
    },
    {
      "name": "RIVIERA CATERERS",
      "address": "2780 STILLWELL AVENUE, BROOKLYN, 11224",
      "phone": "7183723031",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "BRUNOS ON THE BOULEVARD",
      "address": "8825 ASTORIA BOULEVARD, QUEENS, 11369",
      "phone": "7183350505",
      "cuisine_type": "american",
      "grade": "U"
    },
    {
      "name": "WILKEN'S FINE FOOD",
      "address": "7114 AVENUE U, BROOKLYN, 11234",
      "phone": "7184443838",
      "cuisine_type": "delicatessen",
      "grade": "A"
    },
    {
      "name": "TASTE THE TROPICS ICE CREAM",
      "address": "1839 NOSTRAND AVENUE, BROOKLYN, 11226",
      "phone": "7188560821",
      "cuisine_type": "ice cream, gelato, yogurt, ices",
      "grade": "A"
    },
    {
      "name": "WILD ASIA",
      "address": "2300 SOUTHERN BOULEVARD, BRONX, 10460",
      "phone": "7182207846",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "1 EAST 66TH STREET KITCHEN",
      "address": "1 EAST   66 STREET, MANHATTAN, 10065",
      "phone": "2128793900",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "NATHAN'S FAMOUS",
      "address": "1310 SURF AVENUE, BROOKLYN, 11224",
      "phone": "7183332202",
      "cuisine_type": "hotdogs",
      "grade": "A"
    }
  ]
}
```

**Example Usage**

`curl -k localhost:3003/v1/restaurants?cuisine=American -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

```
{
  "data": [
    {
      "name": "RIVIERA CATERERS",
      "address": "2780 STILLWELL AVENUE, BROOKLYN, 11224",
      "phone": "7183723031",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "BRUNOS ON THE BOULEVARD",
      "address": "8825 ASTORIA BOULEVARD, QUEENS, 11369",
      "phone": "7183350505",
      "cuisine_type": "american",
      "grade": "U"
    },
    {
      "name": "WILD ASIA",
      "address": "2300 SOUTHERN BOULEVARD, BRONX, 10460",
      "phone": "7182207846",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "1 EAST 66TH STREET KITCHEN",
      "address": "1 EAST   66 STREET, MANHATTAN, 10065",
      "phone": "2128793900",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "P & S DELI GROCERY",
      "address": "730 COLUMBUS AVENUE, MANHATTAN, 10025",
      "phone": "2129323030",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "ANGELIKA FILM CENTER",
      "address": "18 WEST HOUSTON STREET, MANHATTAN, 10012",
      "phone": "2129952570",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "CAFE METRO",
      "address": "625 8 AVENUE, MANHATTAN, 10018",
      "phone": "2127149342",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "BERKELEY",
      "address": "437 MADISON AVENUE, MANHATTAN, 10022",
      "phone": "2128328121",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "METROPOLITAN CLUB",
      "address": "1 EAST   60 STREET, MANHATTAN, 10022",
      "phone": "2128387400",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "21 CLUB",
      "address": "21 WEST   52 STREET, MANHATTAN, 10019",
      "phone": "2125827200",
      "cuisine_type": "american",
      "grade": "A"
    }
  ]
}
```

**Example Usage**

`curl -k localhost:3003/v1/restaurants?grade=C -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

```
{
  "data": [
    {
      "name": "MORRIS PARK BAKE SHOP",
      "address": "1007 MORRIS PARK AVE, BRONX, 10462",
      "phone": "7188924968",
      "cuisine_type": "bakery",
      "grade": "A"
    },
    {
      "name": "WENDY'S",
      "address": "469 FLATBUSH AVENUE, BROOKLYN, 11225",
      "phone": "7182875005",
      "cuisine_type": "hamburgers",
      "grade": "A"
    },
    {
      "name": "DJ REYNOLDS PUB AND RESTAURANT",
      "address": "351 WEST   57 STREET, MANHATTAN, 10019",
      "phone": "2122452912",
      "cuisine_type": "irish",
      "grade": "A"
    },
    {
      "name": "RIVIERA CATERERS",
      "address": "2780 STILLWELL AVENUE, BROOKLYN, 11224",
      "phone": "7183723031",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "WILKEN'S FINE FOOD",
      "address": "7114 AVENUE U, BROOKLYN, 11234",
      "phone": "7184443838",
      "cuisine_type": "delicatessen",
      "grade": "A"
    },
    {
      "name": "TASTE THE TROPICS ICE CREAM",
      "address": "1839 NOSTRAND AVENUE, BROOKLYN, 11226",
      "phone": "7188560821",
      "cuisine_type": "ice cream, gelato, yogurt, ices",
      "grade": "A"
    },
    {
      "name": "WILD ASIA",
      "address": "2300 SOUTHERN BOULEVARD, BRONX, 10460",
      "phone": "7182207846",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "1 EAST 66TH STREET KITCHEN",
      "address": "1 EAST   66 STREET, MANHATTAN, 10065",
      "phone": "2128793900",
      "cuisine_type": "american",
      "grade": "A"
    },
    {
      "name": "NATHAN'S FAMOUS",
      "address": "1310 SURF AVENUE, BROOKLYN, 11224",
      "phone": "7183332202",
      "cuisine_type": "hotdogs",
      "grade": "A"
    },
    {
      "name": "SEUDA FOODS",
      "address": "705 KINGS HIGHWAY, BROOKLYN, 11223",
      "phone": "7183751500",
      "cuisine_type": "jewish/kosher",
      "grade": "A"
    }
  ]
}
```

**Example Usage**

`curl -k "localhost:3003/v1/restaurants?cuisine=thai&grade=B" -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

```
{
  "data": [
    {
      "name": "JAIYA THAI ORIENTAL RESTAURANT",
      "address": "396 THIRD AVENUE, MANHATTAN, 10016",
      "phone": "2128891330",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "BENNIE'S THAI CAFE",
      "address": "88 FULTON STREET, MANHATTAN, 10038",
      "phone": "2125878930",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "ERAWAN THAI CUISINE",
      "address": "4231 BELL BOULEVARD, QUEENS, 11361",
      "phone": "7184282112",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "LOVELY DAY",
      "address": "196 ELIZABETH STREET, MANHATTAN, 10012",
      "phone": "2129253310",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "KUMA INN",
      "address": "113 LUDLOW STREET, MANHATTAN, 10002",
      "phone": "2123538866",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "TEEDA THAI CUISINE",
      "address": "218 COLUMBIA STREET, BROOKLYN, 11231",
      "phone": "7186432737",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "GALANGA THAI COOKING",
      "address": "149 WEST 4 STREET, MANHATTAN, 10012",
      "phone": "2122284367",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "LAND THAI KITCHEN",
      "address": "450 AMSTERDAM AVENUE, MANHATTAN, 10024",
      "phone": "2125018121",
      "cuisine_type": "thai",
      "grade": "B"
    },
    {
      "name": "LANTERN",
      "address": "101 MONTAGUE STREET, BROOKLYN, 11201",
      "phone": "7182372594",
      "cuisine_type": "thai",
      "grade": "A"
    },
    {
      "name": "THAI ELEPHANT RESTAURANT",
      "address": "2109 31 STREET, QUEENS, 11105",
      "phone": "7182048827",
      "cuisine_type": "thai",
      "grade": "A"
    }
  ]
}
```

---

### Notes on Performance

This project was built to quickly ingest data, clean it, and populate a simple database table. In the future, it would make sense to ingest the data in a different way, i.e. be capable of continuously ingesting streaming data. To facilitate different API capabilities, it could also be beneficial to break the "restaurants" table into a main reference table and multiple smaller tables - values like grades and cuisine types would be their own "state" tables. In addition, there would need to be table cleaning policies to make sure data isn't stale nor the table too large. 

---

### Notes on the ETL Pipeline and Schema

Performing major statistical analysis on this data set is not necessary. The pipeline cleans the data set, drops irrelevant values, and populates a sqlite3 database. The created table is general, i.e. a simple "restaurants" table. By being more general, it becomes easier to build out a comperehensive API without limiting the project. 


Each table entry contains basic establishment info as shown below. These fields are generally available for all restaurants.


For all entries, the following fields are defined:
- Name (DBA)
- Address (BORO, BUILDING, STREET, ZIPCODE)
- Phone (PHONE)
- Cuisine description (CUISINE DESCRIPTION)
- Inspection grade (GRADE)
- If establishment has been inspected (INSPECTION DATE)
- If establishment has been closed based on inspection (ACTION)

After reading and canonicalizing the data, the above columns are populated in the "restaurants" table (address is spread out over multiple columns). Nulls are permissible as long as the restaurant Name is itself not null. See etl_notebook.ipynb or /bin/run_etl.py for further explanation.

---

### Directory Structure

For this project, I felt that a separate /server/handlers folder was not necessary. Typically, handlers would be used to authorize the user, validate the incoming request, and potentially throttle requests. Here, I do very basic request validation in the /server/models file instead.

```
backend-app
│   README - You're reading it!
│   requirements.txt - Virtual environment requirements.
│
└───bin
│       run_etl.py - This is a python script that populates a sqlite3 database given a cleaned .csv file. 
│
└───data
│       DOHMH_New_York_City_Restaurant_Inspection_Results.csv - Our data set.
|       etl_notebook.ipynb - An ipython notebook functioning as the ETL pipeline. Outputs a cleaned .csv file. 
|       cleaned_data.csv - Cleaned .csv created by etl_notebook.ipynb.
│
└───env
│
│
└───server
│   |
│   |
│   └───models
│   |       restaurants.py - Interfaces with the "restaurants" database table. 
│   |
│   └───routes
|   |       restaurants.py - Defines /restaurant route(s).
│   |
│   └───util
|           restaurant_data.py - Defines accepted grade and cuisine types.
|
└───test
        test.py - Simple test script to test our endpoints.

```

---

### TODO

- Add comprehensive logging
- Add schema validation for incoming requests
- Some cuisine types are long, malformed, or not descriptive - create a better schema.
- Restaurant names (DBA) are all uppercase - could use prettier formatting. 
- Squash some commits. 
- Lint.

---

Author: Conor Cunningham (cc2697@cornell.edu)
