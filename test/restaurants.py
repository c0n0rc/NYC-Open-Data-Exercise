import json
import requests

#
# Sanity tests for the /restaurants endpoint.
#
# TODO: Use a more comprehensive testing framework. 
#       Modularize these tests.
#       Build out component tests.
#

hostname = 'http://localhost'
port = ':3003'
API_VERSION = '/v1'
passed = True

if __name__ == '__main__':

  print('Testing the /v1/restaurants endpoint...')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants'
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code
  
  expected_data = json.dumps({"data": [{"name": "MORRIS PARK BAKE SHOP", "address": "1007 MORRIS PARK AVE, BRONX, 10462", "phone": "7188924968", "cuisine_type": "bakery", "grade": "A"}, {"name": "WENDY\'S", "address": "469 FLATBUSH AVENUE, BROOKLYN, 11225", "phone": "7182875005", "cuisine_type": "hamburgers", "grade": "A"}, {"name": "DJ REYNOLDS PUB AND RESTAURANT", "address": "351 WEST   57 STREET, MANHATTAN, 10019", "phone": "2122452912", "cuisine_type": "irish", "grade": "A"}, {"name": "RIVIERA CATERERS", "address": "2780 STILLWELL AVENUE, BROOKLYN, 11224", "phone": "7183723031", "cuisine_type": "american", "grade": "A"}, {"name": "BRUNOS ON THE BOULEVARD", "address": "8825 ASTORIA BOULEVARD, QUEENS, 11369", "phone": "7183350505", "cuisine_type": "american", "grade": "U"}, {"name": "WILKEN\'S FINE FOOD", "address": "7114 AVENUE U, BROOKLYN, 11234", "phone": "7184443838", "cuisine_type": "delicatessen", "grade": "A"}, {"name": "TASTE THE TROPICS ICE CREAM", "address": "1839 NOSTRAND AVENUE, BROOKLYN, 11226", "phone": "7188560821", "cuisine_type": "ice cream, gelato, yogurt, ices", "grade": "A"}, {"name": "WILD ASIA", "address": "2300 SOUTHERN BOULEVARD, BRONX, 10460", "phone": "7182207846", "cuisine_type": "american", "grade": "A"}, {"name": "1 EAST 66TH STREET KITCHEN", "address": "1 EAST   66 STREET, MANHATTAN, 10065", "phone": "2128793900", "cuisine_type": "american", "grade": "A"}, {"name": "NATHAN\'S FAMOUS", "address": "1310 SURF AVENUE, BROOKLYN, 11224", "phone": "7183332202", "cuisine_type": "hotdogs", "grade": "A"}]})

  passed = True if resp_data == expected_data and resp_status == 200 else False

  print(f'Endpoint is available: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'thai'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code

  expected_data = json.dumps({"data": [{"name": "PONGSRI THAI RESTAURANT", "address": "244 WEST   48 STREET, MANHATTAN, 10036", "phone": "2125823392", "cuisine_type": "thai", "grade": "U"}, {"name": "JAIYA THAI ORIENTAL RESTAURANT", "address": "396 THIRD AVENUE, MANHATTAN, 10016", "phone": "2128891330", "cuisine_type": "thai", "grade": "A"}, {"name": "BENNIE'S THAI CAFE", "address": "88 FULTON STREET, MANHATTAN, 10038", "phone": "2125878930", "cuisine_type": "thai", "grade": "A"}, {"name": "ERAWAN THAI CUISINE", "address": "4231 BELL BOULEVARD, QUEENS, 11361", "phone": "7184282112", "cuisine_type": "thai", "grade": "A"}, {"name": "JOYA", "address": "215 COURT STREET, BROOKLYN, 11201", "phone": "7182223484", "cuisine_type": "thai", "grade": "U"}, {"name": "OTT THAI CUISINE", "address": "970 MANHATTAN AVENUE, BROOKLYN, 11222", "phone": "7186092416", "cuisine_type": "thai", "grade": "U"}, {"name": "LOVELY DAY", "address": "196 ELIZABETH STREET, MANHATTAN, 10012", "phone": "2129253310", "cuisine_type": "thai", "grade": "A"}, {"name": "KUMA INN", "address": "113 LUDLOW STREET, MANHATTAN, 10002", "phone": "2123538866", "cuisine_type": "thai", "grade": "A"}, {"name": "TEEDA THAI CUISINE", "address": "218 COLUMBIA STREET, BROOKLYN, 11231", "phone": "7186432737", "cuisine_type": "thai", "grade": "A"}, {"name": "GALANGA THAI COOKING", "address": "149 WEST 4 STREET, MANHATTAN, 10012", "phone": "2122284367", "cuisine_type": "thai", "grade": "A"}]})

  passed = True if resp_data == expected_data and resp_status == 200 else False

  print(f'Endpoint filters by cuisine (lowercase): {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'IRISH'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code

  expected_data = json.dumps({"data": [{"name": "DJ REYNOLDS PUB AND RESTAURANT", "address": "351 WEST   57 STREET, MANHATTAN, 10019", "phone": "2122452912", "cuisine_type": "irish", "grade": "A"}, {"name": "MCSORLEY'S OLD ALE HOUSE", "address": "15 EAST    7 STREET, MANHATTAN, 10003", "phone": "2122542570", "cuisine_type": "irish", "grade": "A"}, {"name": "DORRIAN'S RED HAND RESTAURANT", "address": "1616 2 AVENUE, MANHATTAN, 10028", "phone": "2127726660", "cuisine_type": "irish", "grade": "A"}, {"name": "KILLARNEY ROSE", "address": "80 BEAVER STREET, MANHATTAN, 10005", "phone": "2124221486", "cuisine_type": "irish", "grade": "A"}, {"name": "IRISH COTTAGE", "address": "10807 72 AVENUE, QUEENS, 11375", "phone": "7185208530", "cuisine_type": "irish", "grade": "A"}, {"name": "BLARNEY STONE", "address": "11 TRINITY PLACE, MANHATTAN, 10006", "phone": "2122694988", "cuisine_type": "irish", "grade": "A"}, {"name": "TWINS PUB", "address": "421 9 AVENUE, MANHATTAN, 10001", "phone": "2126431688", "cuisine_type": "irish", "grade": "A"}, {"name": "O'HANLON'S PUB", "address": "2257 31 STREET, QUEENS, 11105", "phone": "7187289619", "cuisine_type": "irish", "grade": "A"}, {"name": "THE LARK'S NEST", "address": "4280 KATONAH AVE, BRONX, 10470", "phone": "3472028233", "cuisine_type": "irish", "grade": "A"}, {"name": "JIM BRADY'S RESTAURANT", "address": "75 MAIDEN LANE, MANHATTAN, 10038", "phone": "2124251300", "cuisine_type": "irish", "grade": "U"}]})

  passed = True if resp_data == expected_data and resp_status == 200 else False

  print(f'Endpoint filters by cuisine (uppercase): {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'grade': 'B'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code

  expected_data = json.dumps({"data": [{"name": "MORRIS PARK BAKE SHOP", "address": "1007 MORRIS PARK AVE, BRONX, 10462", "phone": "7188924968", "cuisine_type": "bakery", "grade": "A"}, {"name": "WENDY'S", "address": "469 FLATBUSH AVENUE, BROOKLYN, 11225", "phone": "7182875005", "cuisine_type": "hamburgers", "grade": "A"}, {"name": "DJ REYNOLDS PUB AND RESTAURANT", "address": "351 WEST   57 STREET, MANHATTAN, 10019", "phone": "2122452912", "cuisine_type": "irish", "grade": "A"}, {"name": "RIVIERA CATERERS", "address": "2780 STILLWELL AVENUE, BROOKLYN, 11224", "phone": "7183723031", "cuisine_type": "american", "grade": "A"}, {"name": "WILKEN'S FINE FOOD", "address": "7114 AVENUE U, BROOKLYN, 11234", "phone": "7184443838", "cuisine_type": "delicatessen", "grade": "A"}, {"name": "TASTE THE TROPICS ICE CREAM", "address": "1839 NOSTRAND AVENUE, BROOKLYN, 11226", "phone": "7188560821", "cuisine_type": "ice cream, gelato, yogurt, ices", "grade": "A"}, {"name": "WILD ASIA", "address": "2300 SOUTHERN BOULEVARD, BRONX, 10460", "phone": "7182207846", "cuisine_type": "american", "grade": "A"}, {"name": "1 EAST 66TH STREET KITCHEN", "address": "1 EAST   66 STREET, MANHATTAN, 10065", "phone": "2128793900", "cuisine_type": "american", "grade": "A"}, {"name": "NATHAN'S FAMOUS", "address": "1310 SURF AVENUE, BROOKLYN, 11224", "phone": "7183332202", "cuisine_type": "hotdogs", "grade": "A"}, {"name": "SEUDA FOODS", "address": "705 KINGS HIGHWAY, BROOKLYN, 11223", "phone": "7183751500", "cuisine_type": "jewish/kosher", "grade": "A"}]})

  passed = True if resp_data == expected_data and resp_status == 200 else False

  print(f'Endpoint filters by grade: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'Thai', 'grade': 'B'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code

  expected_data = json.dumps({"data": [{"name": "JAIYA THAI ORIENTAL RESTAURANT", "address": "396 THIRD AVENUE, MANHATTAN, 10016", "phone": "2128891330", "cuisine_type": "thai", "grade": "A"}, {"name": "BENNIE'S THAI CAFE", "address": "88 FULTON STREET, MANHATTAN, 10038", "phone": "2125878930", "cuisine_type": "thai", "grade": "A"}, {"name": "ERAWAN THAI CUISINE", "address": "4231 BELL BOULEVARD, QUEENS, 11361", "phone": "7184282112", "cuisine_type": "thai", "grade": "A"}, {"name": "LOVELY DAY", "address": "196 ELIZABETH STREET, MANHATTAN, 10012", "phone": "2129253310", "cuisine_type": "thai", "grade": "A"}, {"name": "KUMA INN", "address": "113 LUDLOW STREET, MANHATTAN, 10002", "phone": "2123538866", "cuisine_type": "thai", "grade": "A"}, {"name": "TEEDA THAI CUISINE", "address": "218 COLUMBIA STREET, BROOKLYN, 11231", "phone": "7186432737", "cuisine_type": "thai", "grade": "A"}, {"name": "GALANGA THAI COOKING", "address": "149 WEST 4 STREET, MANHATTAN, 10012", "phone": "2122284367", "cuisine_type": "thai", "grade": "A"}, {"name": "LAND THAI KITCHEN", "address": "450 AMSTERDAM AVENUE, MANHATTAN, 10024", "phone": "2125018121", "cuisine_type": "thai", "grade": "B"}, {"name": "LANTERN", "address": "101 MONTAGUE STREET, BROOKLYN, 11201", "phone": "7182372594", "cuisine_type": "thai", "grade": "A"}, {"name": "THAI ELEPHANT RESTAURANT", "address": "2109 31 STREET, QUEENS, 11105", "phone": "7182048827", "cuisine_type": "thai", "grade": "A"}]})

  passed = True if resp_data == expected_data and resp_status == 200 else False

  print(f'Endpoint filters by cuisine and grade: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'invalid'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code

  expected_data = 'Error: grade param is invalid.'

  passed = True if resp_data == expected_data and resp_status == 422 else False

  print(f'Endpoint rejects invalid cuisine param: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'grade': 'invalid'}
  )

  resp_data   = response.content.decode('UTF-8')
  resp_status = response.status_code
  
  expected_data = 'Error: grade param is invalid.'

  passed = True if resp_data == expected_data and resp_status == 422 else False

  print(f'Endpoint rejects invalid grade param: {passed}')

  ###
