
import mysql.connector
from mysql.connector import errorcode
import pandas
import plotly.graph_objs as go

# Assumed appearance of options:
#
# options = {
#   host: 123.45.67.890
#   user: usrnm
#   password: pswrd
#   database: someSQL
#   queries: [
#       { name: variableName
#         search: SELECT stuff FROM palce
#         column: index
#       }
#   ]
# }
#

def connect(conn, options):
    #check for an open connection before opening another
    if not conn == 'none':
        if conn.is_connected():
            print('connection already open')
            return conn
    # connect to the database
    try:
        conn = mysql.connector.connect(
            host=options.host,
            user=options.username,
            passwd=options.password,
            db=options.database
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password. Recieved:")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        print({"host":options.host, "user":options["user"], "passwd":options.password, "db":options.database})
        return 'none'

    return conn

def query(connection, queries, options):
    print('opening query connection...')
    con = connect(connection, options)
    # define our dictionary to return
    data = {}
    # read our querys into DataFrames
    for query in queries:
        result = pandas.read_sql(query["search"], con)
        try:
            assert query["modifier"]
        except:
            data[query["name"]] = result[query["column"]]
        else:
            data[query["name"]] = result[query["column"]].map(str) + query["modifier"] + result[query["column2"]]
    print("closing query connection...")
    con.close()
    return con, data


def test(conn, options, query, variables, layout):
    print('opening callback connection...')
    db = connect(conn, options)
    if db == 'none':
        print("There was an error with your connection")
        return

    dataframe = pandas.read_sql(query[0].format(**variables), con=db)
    print("closing callback connection...")
    db.close()
    return db, {}









def callback_connect(data, layout):

    return {
        'data' : [
            go.Scatter (
                x=data["data1"][layout["x"]].str[:5]+"am",
                y=data["data1"][layout["y"]],
                name=layout["data1"]
            ),
            go.Scatter (
                x=data["data2"][layout["x"]].str[:5]+"am",
                y=data["data2"][layout["y"]],
                name=layout["data2"]
            )
        ],
        'layout': go.Layout(
            title=layout["title"],
            yaxis={
                'title': layout["axis"]
            },
            showlegend=True,
            margin={'l': 50, 'b': 100, 't': 120, 'r': 0},
        ),
        'legend' : dict (orientation = "h"),
    }
