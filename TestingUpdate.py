import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import plotly


def ReadData():
    f = open("testing_communication.txt")
    resultData = {
        'interval':[],
        'data':[]
    }
    for line in f:
        lineSplit = line.split(",")
        resultData['interval'].append(int(lineSplit[0]))
        resultData['data'].append(int(lineSplit[1]))
    f.close()
    return resultData


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

startTime = time.process_time()
interval = [startTime]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H4('Testing Live Update'),
    dcc.Graph(id='live_update_graph'),
    dcc.Interval(
        id='interval',
        interval=1*1000,
        n_intervals=0
    )
])

@app.callback(Output('live_update_graph', 'figure'),
              [Input('interval', 'n_intervals')])
def update_graph_live(n):

    data = ReadData()

    trace = go.Scatter(
        x = data['interval'],
        y = data['data'],
        marker = {'color':'blue', 'size':10},
        mode = 'markers+lines'
    )

    data = [trace]
    figure = go.Figure(data=data)

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
