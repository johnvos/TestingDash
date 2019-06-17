import dash_html_components as html
import dash_core_components as dcc
import dash
import plotly.graph_objs as go
import datetime as dt
from TestingDataReceiving import getData

testing = getData()
print("Received: {}\n".format(testing))
