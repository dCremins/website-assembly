# General imports from the old file
#need to be cleaned up
import MySQLdb
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#import dash_colorscales
import pandas as pd
import numpy as np
import base64
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
import dash_auth
import flask




# Our Imports
# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# Dash Layout
from dash_html_template import Template
# Loading Data and Custom Modules
import python_database
import components/select as select
import json
from textwrap import dedent


# Get JSON Data
f = open('data.json')
data = json.load(f)
f.close()

# Get HTML Layout
f = open("./rm/vanilla/build/index.html")
html_layout = f.read()
f.close()

# If this tool needs a database, send the options from data to our SQL function
if data.database:
    database_data = python_database.connect(data.database_options)
else:
    database_data = {}

# Load images
if data.images:
    images = os.listdir( './assets' )
    for image in images:
        image_data[image] = base64.b64encode(open(image, 'rb').read())
else:
    image_data = []

# Load Components
injection_dict = {}
for component in data.components:
    if component.type == 'select':
        if database_data[component.options]:
            options = database_data[component.options]
        else:
            options.component.options
        injection_dict[component.id] = select(component, options)

# Callback generator for Graphs
def create_callback(output):
     def callback(input):
        # ....
        return {
            'data': [],
            'layout': [],
            'legend': []
        }
    return callback

# Load Graphs
for graph in data.graph:
    outputs = Output(graph.output.id, graph.output.property)
    inputs = []
    for input in graph.input:
        input.append(Input(input.id, input.property))

    @app.callback(outputs, inputs)(create_callback(outputs))

# Run the app
app = dash.Dash()
app.layout = Template.from_string(html_layout, injection_dict)
