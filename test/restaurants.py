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

  passed = True if response.status_code == 200 else False

  print(f'Endpoint is available: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'Thai'}
  )

  passed = True if response.status_code == 200 else False

  print(f'Endpoint filters by cuisine: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'grade': 'A'}
  )

  passed = True if response.status_code == 200 else False

  print(f'Endpoint filters by grade: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'Thai', 'grade': 'A'}
  )

  passed = True if response.status_code == 200 else False

  print(f'Endpoint filters by cuisine and grade: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'cuisine': 'invalid'}
  )

  passed = True if response.status_code == 422 else False

  print(f'Endpoint rejects invalid cuisine param: {passed}')

  ###

  response = requests.get(
      hostname + port + API_VERSION + '/restaurants',
      params={'grade': 'invalid'}
  )

  passed = True if response.status_code == 422 else False

  print(f'Endpoint rejects invalid grade param: {passed}')

  ###
