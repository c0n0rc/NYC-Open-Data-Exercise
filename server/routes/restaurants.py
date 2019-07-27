from flask import Blueprint
from flask import Response
from flask import request
from urllib.parse import urlparse

import models.restaurants

#
# Routes for the /restaurants endpoint with very basic validation.
#
# TODO: Further validate incoming requests using a predefined schema and jsonschema, etc..
#       Move validation to /server/handlers. 
#       Have default response route.
#

restaurants = Blueprint('restaurants', __name__)
API_VERSION = '/v1'

# Returns a list of restaurants. If 'cuisine' or 'grade' parameters are given, returns a filtered list. 
# Returns max of 10 restaurants in no particular order.
@restaurants.route(API_VERSION + '/restaurants', methods=['GET'])
def get_restaurants():
    status_code = 200
    status_mesg = 'Success'

    # Grab filter params
    cuisine_param = request.args.get('cuisine').lower() if request.args.get('cuisine') else None
    grade_param   = request.args.get('grade').upper() if request.args.get('grade') else None

    # If either params are present, return a filtered list
    if cuisine_param or grade_param:
        status_code, status_mesg = models.restaurants.filter_restaurants(cuisine_param, grade_param)
    # Else, return an unfiltered list
    else:
        status_code, status_mesg = models.restaurants.get_restaurants()

    # Format and return the response
    return Response(status_mesg, status=status_code)
