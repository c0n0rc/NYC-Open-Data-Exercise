from flask import Flask

from routes.restaurants import restaurants

#
# Main entry point for the app. Get the server up and running.
#

# Initialize Flask and register routes.
app = Flask(__name__)
app.register_blueprint(restaurants)

if __name__ == '__main__':

  # Initiate the Flask server on localhost:3003
  app.run(debug=True, port=3003)

  # Listen!
