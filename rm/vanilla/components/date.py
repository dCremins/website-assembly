import dash
import dash_core_components as dcc
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def date(info):
    return dcc.DatePickerRange(
        id=info["id"],
        calendar_orientation=info["orientation"],
        start_date=dt.now() - relativedelta(info["start"]),
        end_date=dt.now() - relativedelta(info["end"])
    )
