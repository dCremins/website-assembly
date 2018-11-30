# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_template import Template

from textwrap import dedent

# Open the HTML file
f = open("./rm/vanilla/build/index.html")
html_layout = f.read()

# Define the components
dummyRoutes = [
    "1 - (I-540 WB @ US-401)",
    "2 - (Falls of Neuse @ New Falls)",
    "3 - (Falls of Neuse @ Spring Forest)",
    "4 - (Six Forks @ Norwood)",
    "5 - (Six Forks @ Spring Forest)",
    "6 - (Creedmoor @ Norwood)"
]

route = dcc.Dropdown(
    id='rt-select',
    options=[
        {'label': i, 'value': i[:1]} for i in dummyRoutes
    ],
    value='1',
)

test = html.H2(
    id='test'
)

#source =

#after =

#before =


# Insert components into HTML using key-value pairs
injection_dict = {
    'route': route,
    'test': test
}

# Run the app
app = dash.Dash()
app.layout = Template.from_string(html_layout, injection_dict)

# Logic
@app.callback(
    Output(component_id='test2', component_property='children'),
    [Input(component_id='rt-select', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

# Server
if __name__ == '__main__':
    app.run_server(debug=True)
