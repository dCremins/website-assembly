from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def date(info):
    return dcc.DatePickerRange(
        id=info["id"],
        calendar_orientation=info["orientation"],
        start_date=dt.now() - relativedelta(months=+info["start"]),
        end_date=dt.now() - relativedelta(months=+info["end"])
    )

def graph(info):
    return dcc.Graph(
        id=info["id"],
    )

def select(info, options, value_split):
    if value_split == 'first':
        return dcc.Dropdown(
            id=info["id"],
            options=[{'label': label, 'value': label[:1]} for i, label in enumerate(options)],
            value=info["value"],
        )
    else:
        return dcc.Dropdown(
            id=info["id"],
            options=[{'label': label, 'value': label} for i, label in enumerate(options)],
            value=info["value"],
        )

def image(info):
    return html.Img(
        id=info["id"],
        src=info["src"]
    )
