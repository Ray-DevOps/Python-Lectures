
#                                 OVERVIEW
                       ------------------------------


# Application Programming Interfaces (APIs), are a set of commands, functions, protocols, and objects that programmers
# can use to create software or interact with an external system.
# APIs allow us to interact with external systems/websites and pull live data from the sites.
# The API acts as an interface between your software and the external system.
# You use the rules that the external system's API has prescribed to make a request to the external system for some piece of data, and if
# you have structured your request according to all of the requirements that this external system has set out in their API, then they
# will respond to you with the data that you requested.

# The specific location where the requested data is stored (the location that accepts such requests and sends back responses) is known 
# as an API endpoint. So the different systems send and receive data constructively through the endpoint.
# API endpoints are basically URLs. e.g. api.coinbase.com is the API endpoint for Coinbase Inc., a global cryptocurrency exchange platform.

# The request made to the API endpoint is called an API request.
# API request can receive the following response codes

# 1XX: Hold on (request is being processed)
# 2XX: Success
# 3XX: Redirection
# 4XX: Unauthorized, not available, etc
# 5XX: Server problem (problem from their end)



#                        USING API ENDPOINTS TO GET DATA
                  ---------------------------------------------
# In this example, we use the API endpoint of ISS now, to get the current location (longitude and latitude) of NASA's space station.


import requests                                                           # The "requests" module allows you to send HTTP requests using Python.

response = requests.get(url="http://api.open-notify.org/iss-now.json")    # We make a request to the ISS api endpoint, and store the response in a variable called "response"

print(response)                   --------------->   <Response [200]>
print(response.status_code)       --------------->    200

response.raise_for_status()                                               # when making API requests through our Python code, we can as well raise for status code  as follows:

data = response.json()                                                    # to get our response data in JSON format. The dictionary below can work as any Python dictionary
print(data)                       --------------->      {'timestamp': 1698875485, 'message': 'success', 'iss_position': {'latitude': '0.1287', 'longitude': '-2.3129'}}

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)              --------------->   ('6.7350', '12.6012')


