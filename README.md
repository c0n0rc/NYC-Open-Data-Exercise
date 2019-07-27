### Overview

This project entails reading in data from an [NYC Open Data Set](https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv), running it through an ETL pipeline, and storing the clean data in a sqlite3 database. With the database populated, users can make requests to an API endpoint that, given a Health Department grade and cuisine type, will return a list of 10 max establishments for a given cuisine which satisfy said Health Department rating.

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

To run the ETL pipeline (only run once):
```
python3 bin/run_etl.py
```

### To Test

To run the IPython notebook to test the ETL pipeline, run:
```
jupyter notebook etl_notebook.ipynb
```

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

TODO

**Example Usage**

`curl -k localhost:3003/v1/restaurants?cuisine=American -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

TODO

**Example Usage**

`curl -k localhost:3003/v1/restaurants?grade=C -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

TODO

**Example Usage**

`curl -k localhost:3003/v1/restaurants?cuisine=thai&grade=B -H "Accept: application/json" -H "Content-Type: application/json"`

**Example response:**

TODO

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

---

Author: Conor Cunningham (cc2697@cornell.edu)
