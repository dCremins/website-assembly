# -*- coding: utf-8 -*-
import dash
import dash_auth
from dash.dependencies import Input, Output
from dash_html_template import Template
from credentials import rm_dash_server
from credentials import rm_dash_database

import pandas
import mysql.connector as MySQLdb

from textwrap import dedent
import json
import python_database
import components as components

VALID_USERNAME_PASSWORD_PAIRS = [
    [rm_dash_server.username, rm_dash_server.password]
]

# Open the HTML file
file = open("index.html", "r")
html_layout = file.read()

# Get JSON Data
file = open('data.json', 'r')
data = json.load(file)

# define global variables
connection = 'none'
input_components = []
output_components = []
input_holder = {}

# Load input options from the database
try:
    assert rm_dash_database
except:
    print('No database connection was made for this tool.')
    database_data = {}
else:
    connection, database_data = python_database.query(connection, data["queries"], rm_dash_database)

# Load Dash Components
injection_dict = {}
for component in data["components"]:
    if component["type"] == 'date':
        injector = components.date(component)
        injection_dict[component["id"]] = injector

    if component["type"] == 'select':
        hold = component["options"]
        try:
            assert database_data.has_key(hold)
        except:
            options = hold
        else:
            options = database_data[hold]
        injector = components.select(component, options, component["value_split"])
        injection_dict[component["id"]] = injector

for component in data["graph"]:
    injector = components.graph(component["output"])
    injection_dict[component["output"]["id"]] = injector

# Run the app
app = dash.Dash(__name__)
#app = dash.Dash('auth')
app.layout = Template.from_string(html_layout, injection_dict)
app.css.config.serve_locally = True
app.config.include_asset_files = True
app.title = data["title"]
#auth = dash_auth.BasicAuth(
#    app,
#    VALID_USERNAME_PASSWORD_PAIRS
#)

# Callback Generator Function
def create_callback(output, graph):
    # Load data from global variable and pass it to the graph figure function
    def rm_callback(*stuff):
        global input_holder
        try:
            assert input_holder[graph["output"]["id"]]
        except:
            print('No data available for callback.')
            database_data = {}
        else:
            database_data = python_database.callback_connect(input_holder[graph["output"]["id"]], graph["layout"])
        return database_data
    return rm_callback

# Load Graphs Controls and pass to callback generator
for graph in data["graph"]:
    output = Output(graph["output"]["id"], graph["output"]["property"])
    # use invisible connection div as input so that graph callbacks wait for query data to be stored
    app.callback(output, [Input(component_id="callback_open", component_property='children')])(create_callback(output, graph))
    # Store inputs to global variable to be used as inputs for the database query callback
    for input in graph["input"]:
        input_components.append(Input(input["id"], input["property"]))

# On Input change, load graph query data to global variable
# use invisible connector div as output
@app.callback(
    Output(component_id='callback_open', component_property='children'),
    input_components
)
def open_sql_connection(*input_value):
    global connection
    global input_holder
    print('Opening connection...')
    connection = python_database.connect(connection, rm_dash_database)
    if connection == 'none':
        print("There was an error with your connection")
        return
    for graph in data["graph"]:
        variables = {}
        i = 0
        for input in graph["input"]:
            variables[input["variable"].encode("utf-8")] = input_value[i]
            i += 1
        input_holder[graph["output"]["id"]] = {
            "data1": pandas.read_sql(graph["query"][0].format(**variables), con=connection),
            "data2": pandas.read_sql(graph["query"][1].format(**variables), con=connection)
        }
    print('Closing connection...')
    connection.close()
    return

# Server

if __name__ == '__main__':
    app.run_server(debug=True,port=80,host='0.0.0.0')
