''' Example of a simple flask API with multiple routes '''

from flask import Flask, request

''' The application is defined here '''

app = Flask(__name__)

''' To access the api, you may go to 127.0.0.1:5000/ OR
localhost:5000/
Routes are like paths. They may redirect to different pages
that have different functions. In this case, our api has
multiple routes with multiple different functions. To access
a route, you may go to 127.0.0.1:5000/<route_name> OR
localhost:5000/<route_name>'''

@app.route("/")
def main_route():
	''' This is the main route. To get to this route,
	you must run the script and type "127.0.0.1:5000/" in the url bar
	of any browser'''

	return '<p style="font-size:2em" >Hello World!</p>'

@app.route("/add")
def add_numbers():
	''' This route takes arguments, similar to how
	functions in other programming languages take arguments.
	To pass arguments called num1 and num2 to this route, you may go to
	127.0.0.1:5000/add?num1=4&num2=6 '''
	num1 = request.args.get("num1")
	num2 = request.args.get("num2")
	result = int(num1) + int(num2)
	return str(result)

names = ["Alice", "Bob", "Charlie", "Diana", "Elise", "Francis"]

@app.route("/search_name")
def search_name():
	''' In the list above titled "names", we have a series of pre-defined names.
	The purpose of this route is to accept an argument "name" and return
	whether or not "name" is in the list. You may edit the list above if you like.
	To use this route, go to 127.0.0.1:5000/search_name?name=Alice
	You may replace the value of "name" in the url to any other name you would like to test'''
	name = request.args.get("name")
	if name in names:
		return "True"
	else:
		return "False"

data = []

@app.route("/add_data")
def add_data():
	''' The list "data" defined above is empty. The purpose of this route
	is to allow us to add strings to "data". You may access this route by
	going to 127.0.0.1:5000/add_data?new_data=Hello and changing the value
	of "new_data" in the url to anything that you would like to add to the list.
	Go ahead and add new data to the list'''
	new_data = request.args.get("new_data")
	if new_data != None:
		data.append(new_data)
		return new_data + " added"
	else:
		return "No data found"

@app.route("/view_data")
def view_data():
	'''In the above route, we added new data to a list. This route
	will allow us to look at all of the data in the list.
	To access the route, go to 127.0.0.1:5000/view_data'''
	return "<br />".join(data)

if __name__ == "__main__":
	app.run(debug=True)
