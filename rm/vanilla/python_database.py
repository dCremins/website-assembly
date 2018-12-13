import MySQLdb
import pandas

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

def connect(options):
    # connect to the database
    conn = MySQLdb.connect(host=options.host, user=options.user, passwd=options.password, db=options.database)
    # define our dictionary to return
    data = {}
    # read our querys into DataFrames
    for query in options.queries:
        result = pandas.read_sql(query.search, con=conn)
        data[query.name] = result[query.column]

    conn.close()

    return data
