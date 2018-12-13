import dash
import dash_core_components as dcc

def select(info, options):
    return dcc.Dropdown(
        id=info.id,
        options=[{'label': i, 'value': i[:1]} for i in options],
        value=info.value,
    )
