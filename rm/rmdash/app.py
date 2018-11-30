import MySQLdb
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_colorscales
import pandas as pd
import numpy as np
import base64
from datetime import datetime as dt
import plotly.graph_objs as go
import dash_auth


# Passwords list- move to separate file not on github
VALID_USERNAME_PASSWORD_PAIRS = [
    ['ncdot', 'rm']
]


#app = dash.Dash(__name__)
#server = app.server

app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)



conn = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
cursor = conn.cursor()
cursor.execute('SELECT distinct rt_number  FROM `tb_routes` ')
rows=cursor.fetchall()
df=pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0: 'new_rt'}, inplace=True);
#df = pd.read_csv('http://itredatalab.org/rm.test.csv')
#cursor.execute('SELECT distinct `Date_1` from rt_test')
#rows1=cursor.fetchall()
#df1=pd.DataFrame([rows1])
df2=pd.read_sql('SELECT distinct `Date_1` from rt_test', con=conn)
#df1.rename(columes={0: 'disc_date'}, inplace=True);
conn.close()
conn55 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
df55=pd.read_sql('select * from rt_desc;', con=conn55)
df55['trr']=df55['rt_no'].map(str)+ " - ("+df55['rt_name']+")"
conn55.close()

aval_rt=df['new_rt']
aval_rt2=df55['trr']
aval_date=df2['Date_1']
aval_baseline=df2['Date_1']


# Devin --> This section you may need to load your pictures....

image_filename = 'static/itredatalab-logo2.JPG'  # replace with your own image
encoded_ITRE = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/ncdot-logo.png'  # replace with your own image
encoded_NCDOT = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/flow_rates.png'  # replace with your own image
encoded_flow = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/route_map.png'  # replace with your own image
encoded_route_map = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/savings_table.png'  # replace with your own image
encoded_savings = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/tt_route.png'  # replace with your own image
encoded_route_tt = base64.b64encode(open(image_filename, 'rb').read())
image_filename = 'static/redsection.png'  # replace with your own image
encoded_redsection = base64.b64encode(open(image_filename, 'rb').read())


'''
~~~~~~~~~~~~~~
~ APP LAYOUT ~~
~~~~~~~~~~~~~~
'''
# Devin --> This is the section that we define HTML codes


app.layout = html.Div([
	html.Div([
		html.Img(src='data:image/png;base64,{}'.format(encoded_ITRE.decode()), height='130px', style={'text-align':'center'})] , className='three columns', style={'text-align':'right'}),
	html.Div([
	    html.H2(children='I-540WB On-Ramp Signals Evaluation Dashboard'),
	    html.P("This dashboard is design to assist NCDOT to evaluate the impact of On-Ramp signals on I-540WB. For questions or bugs related to this dashboard, please contact support@itredatalab.org. The travel times data used in this dashboard are collected from HERE.COM."),], className = 'nine columns'),
	html.Div([
	html.P(". 	")] , className='twelve columns'),



    html.Div([
        html.P(".	 ")] , className='twelve columns'),
html.Div([html.H4("Travel Time Analysis:")],className="nine columns"),
  html.Div([
        html.P("This section provide a summary report of Travel Times on nine defined routes within I-540WB facility. The user should select a route as well as a reporting or baseline period for travel time analysis. For volume analysis, the user only needs to select a reporting or a baseline periods.")] , className='nine columns'),

	html.Div([
html.Div([
			html.H6(["Route #:"]),
			dcc.Dropdown(
			    id='rt-select',
			    options=[
			        {'label': i, 'value': i[:1]} for i in dummyRoutes

			    ],
			    value='1',
			),

			html.H6(["Reporting Period:"]),




dcc.DatePickerRange(
    id='date_select',
    calendar_orientation='horizontal',
    start_date=dt(2018,2,1),
    end_date=dt(2018,2,28)
),


                        html.H6(["Baseline Period:"]),


dcc.DatePickerRange(
    id='date_baseline',
    calendar_orientation="horizontal",
    start_date=dt(2018,1,1),
    end_date=dt(2018,1,31),
)



	] , className='four columns' ),

 html.Div([
                html.Img(src='data:image/png;base64,{}'.format(encoded_route_map.decode()),height='550px' , width='1000px')],  className='seven columns' , style={'horizontal-align': 'middle'}),


html.Div([
                        dcc.Graph(
                        id='example-graph-Total',
                )], className="twelve columns"),


], className="ten columns"),

      html.Div([





                html.Div([
                        dcc.Graph(
                        id='example-graph-Mon',
                )], className="three columns"),

                html.Div([
                        dcc.Graph(
                        id='example-graph-Tue',
                )], className="three columns"),


                html.Div([
                        dcc.Graph(
                        id='example-graph-Wed',
                )], className="three columns"),


                html.Div([
                        dcc.Graph(
                        id='example-graph-Thu',
                )], className="three columns"),


                html.Div([
                        dcc.Graph(
                        id='example-graph-Fri',
                )], className="three columns"),






                ], className = "twelve columns"),
	    html.Div([
        html.P("         ")] , className='twelve columns'),
html.Div([html.H4("Volume Analysis:")],className="nine columns"),


html.Div([html.P(["This section provides a summary report of observed/measured flow rates at two locations on I-540WB facility."])], className="nine columns"),




     html.Div([





                html.Div([
                        dcc.Graph(
                        id='example-graph-UPsen',
                )], className="six columns"),

                html.Div([
                        dcc.Graph(
                        id='example-graph-DNsen',
                )], className="six columns"),




                ], className = "ten columns"),












#    html.Div([
#        html.Img(src='data:image/png;base64,{}'.format(encoded_route_map.decode())),
#        html.Img(src='data:image/png;base64,{}'.format(encoded_savings.decode())),
#        html.Img(src='data:image/png;base64,{}'.format(encoded_route_tt.decode())),
#        html.Img(src='data:image/png;base64,{}'.format(encoded_flow.decode())),
#    ], id='GraphDiv', className='ten columns')

], className='twelve columns' )

app.css.append_css({"external_url": "http://itredatalab.org/css_for_other_tools/rm.css"})


#app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


# Devin --> this section does the compitations and update graphs.....

@app.callback(
        dash.dependencies.Output('example-graph-Total', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTotal(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
	conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
	conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
	df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt from TP_def left join rt_test on rt_test.time_1=TP_def.time_2 where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays)  group by TP_def.time_2;', con=conn1)
	df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+'  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays)  group by TP_def.time_2;', con=conn2)
	conn1.close()
	conn2.close()
	print(type(df3['time_2']))
	return {
'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],

'layout': go.Layout(
        title="Average Travel Time (min) Across Selected Periods",
	xaxis={
	'type': 'time',
	'tickformat':'%H:%M'
	},
       yaxis={
                'title': 'Travel Time (Minutes)'
            },
        showlegend=True,
        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        ),
'legend' : dict (orientation = "h"),

}



@app.callback(
        dash.dependencies.Output('example-graph-Mon', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphMon(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#	dff=df[df['new_rt'] == rtselect ]
	conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
	conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
	df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=0  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn1)
	df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=0  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn2)
	conn1.close()
	conn2.close()
	return {

'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],

'layout': go.Layout(
        title="Monday(s) TT",
              xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
	 yaxis={
                'title': 'Travel Time (min)'
            },
        showlegend=False,
        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        ),
'legend' : dict (orientation = "h"),

}



@app.callback(
        dash.dependencies.Output('example-graph-Tue', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTue(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=1  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn1)
        df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=1  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn2)
        conn1.close()
        conn2.close()
        return {

'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],

'layout': go.Layout(
        title="Tuesday(s) TT",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Travel Time (min)'
            },
        showlegend=False,

        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        )

}


@app.callback(
        dash.dependencies.Output('example-graph-Wed', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTue(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=2  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn1)
        df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=2  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn2)
        conn1.close()
        conn2.close()
        return {

'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],

'layout': go.Layout(
        title="Wednesday(s) TT",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Travel Time (min)'
            },
        showlegend=False,

        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        )

}




@app.callback(
        dash.dependencies.Output('example-graph-Thu', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTue(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2 where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=3  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn1)
        df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2 where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=3  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn2)
        conn1.close()
        conn2.close()
        return {

'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],


'layout': go.Layout(
        title="Thursday(s) TT",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Travel Time (min)'
            },
        showlegend=False,

        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        )

}




@app.callback(
        dash.dependencies.Output('example-graph-Fri', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTue(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2  where rt_test.date_1 >= "' + dateselectSTR  + '" and rt_test.Date_1 <= "'+ dateselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=4  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn1)
        df4=pd.read_sql('select TP_def.time_2, avg(rt_test.tt) as avgtt  from TP_def left join rt_test on rt_test.time_1=TP_def.time_2 where rt_test.date_1 >= "' + baselineselectSTR  + '" and rt_test.Date_1 <= "'+ baselineselectEND +'"  and rt_test.rt_number='+str(rtselect)+' and weekday(rt_test.date_1)=4  AND rt_test.Date_1 NOT IN (SELECT holiday_date from holidays) group by TP_def.time_2;', con=conn2)
        conn1.close()
        conn2.close()
        return {



'data' : [go.Scatter ( x= df3['time_2'].str[:5]+"am" , y=df3['avgtt'], name='Selected Date'),go.Scatter ( x=df4['time_2'].str[:5]+"am" , y=df4['avgtt'], name='Baseline')],

'layout': go.Layout(
        title="Friday(s) TT",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Travel Time (min)'
            },
        showlegend=False,

        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        )

}

# CALL BACKS for VOLUME Graphs ...


@app.callback(
        dash.dependencies.Output('example-graph-UPsen', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTotal(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select time, avg(volume) as avgvol from vol_tb where vol_tb.sensor_ID ="East"  and vol_tb.date >= "' + dateselectSTR  + '" and vol_tb.Date <= "'+ dateselectEND +'"  AND vol_tb.Date NOT IN (SELECT holiday_date from holidays)   group by vol_tb.time;', con=conn1)
        df4=pd.read_sql('select time, avg(volume) as avgvol from vol_tb where  vol_tb.sensor_ID ="East"  and vol_tb.date >= "' + baselineselectSTR  + '" and vol_tb.Date <= "'+ baselineselectEND +'"  AND vol_tb.Date NOT IN (SELECT holiday_date from holidays)   group by vol_tb.time;', con=conn2)
        conn1.close()
        conn2.close()
        return {
'data' : [go.Scatter ( x= df3['time'].str[:5]+"am" , y=df3['avgvol'], name='Selected Date'),go.Scatter ( x=df4['time'].str[:5]+"am" , y=df4['avgvol'], name='Baseline')],

'layout': go.Layout(
        title="I-540WB UpStream Fixed Sensor Volume (vphpl)",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Flow Rate Per Lane (vphpl)'
            },
        showlegend=True,
        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        ),
'legend' : dict (orientation = "h"),

}



@app.callback(
        dash.dependencies.Output('example-graph-DNsen', 'figure'),
        [dash.dependencies.Input('rt-select','value'),
       dash.dependencies.Input('date_select','start_date'),
       dash.dependencies.Input('date_select','end_date'),
       dash.dependencies.Input('date_baseline','start_date'),
       dash.dependencies.Input('date_baseline','end_date')])

def update_graphTotal(rtselect, dateselectSTR, dateselectEND, baselineselectSTR, baselineselectEND):
#       dff=df[df['new_rt'] == rtselect ]
        conn1 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        conn2 = MySQLdb.connect(host="152.14.29.12", user="rmdash", passwd="dashdash", db="rmdash")
        df3=pd.read_sql('select time, avg(volume) as avgvol from vol_tb where  vol_tb.sensor_ID ="West"  and vol_tb.date >= "' + dateselectSTR  + '" and vol_tb.Date <= "'+ dateselectEND +'"  AND vol_tb.Date NOT IN (SELECT holiday_date from holidays)   group by vol_tb.time;', con=conn1)
        df4=pd.read_sql('select time, avg(volume) as avgvol from vol_tb where  vol_tb.sensor_ID ="West"  and vol_tb.date >= "' + baselineselectSTR  + '" and vol_tb.Date <= "'+ baselineselectEND +'"  AND vol_tb.Date NOT IN (SELECT holiday_date from holidays)   group by vol_tb.time;', con=conn2)
        conn1.close()
        conn2.close()
        return {
'data' : [go.Scatter ( x= df3['time'].str[:5]+"am" , y=df3['avgvol'], name='Selected Date'),go.Scatter ( x=df4['time'].str[:5]+"am" , y=df4['avgvol'], name='Baseline')],

'layout': go.Layout(
        title="I-540WB DownStream Fixed Sensor Volume (vphpl)",
        xaxis={
        'type': 'time',
        'tickformat':'%H:%M'
        },
       yaxis={
                'title': 'Flow Rate Per Lane (vphpl)'
            },
        showlegend=True,
        margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        ),
'legend' : dict (orientation = "h"),

}



# load app
#app = dash.Dash('auth')
#auth = dash_auth.BasicAuth(
#    app,
#    VALID_USERNAME_PASSWORD_PAIRS
#)
#server = app.server
app.title = 'I-540WB OnRamp Signal Evaluation Dashboard'



if __name__ == '__main__':
    app.run_server(debug=True,port=5081,host='0.0.0.0')
