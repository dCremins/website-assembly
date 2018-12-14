# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_template import Template

from textwrap import dedent
import json
import python_database
import components.date as date_component

# Open the HTML file
f = open("./rm/vanilla/build/index.html")
html_layout = f.read()

# Get JSON Data
f = open('./rm/vanilla/data.json', 'r')
data = json.load(f)
#data = f.read()
f.close()

try:
    assert data["database"]
except:
    print('No database connection was made for this tool.')
    database_data = {}
else:
    print('Database information found.')
    database_data = python_database.connect(data["database_options"])

# Load Components
injection_dict = {}
for component in data["components"]:
    if component["type"] == 'date':
        injector = date_component.date(component)
        injection_dict[component["id"]] = injector

    if component["type"] == 'select':
        hold = component["options"]
        try:
            assert database_data[hold]
        except:
            options = hold
        else:
            options = database_data[hold]


# Run the app
app = dash.Dash()
app.layout = Template.from_string(html_layout, injection_dict)

# Logic


# Server
if __name__ == '__main__':
    app.run_server(debug=True)
