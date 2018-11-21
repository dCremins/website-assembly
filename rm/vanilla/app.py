# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_template import Template

from textwrap import dedent

f = open("test.html")
string = f.read()

graph = dcc.Graph(
    id='example-graph',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
)
html_layout = string

injection_dict = {'date_picker': graph}

app = dash.Dash()
app.layout = Template.from_string(html_layout, injection_dict)

if __name__ == '__main__':
    app.run_server(debug=True)
