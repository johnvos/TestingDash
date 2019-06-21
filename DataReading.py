import ast

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go


f = open("testing_communication.log")

def ReadData():

    resultData = {
        'time':[],
        'quality':[],
        'noiseratio':[],
        'signallevel':[],
        'bitrate':[]
    }
    for line in f:
        lineSplit = line.split("=")
        resultData['time'].append(lineSplit[0])
        dataReceived = ast.literal_eval(lineSplit[1])
        resultData['quality'].append(dataReceived['quality'])
        resultData['noiseratio'].append(dataReceived['Noiseratio'])
        resultData['signallevel'].append(dataReceived['signallevel'])
        resultData['bitrate'].append(dataReceived['bitrate'])
    f.seek(0)
    return resultData


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H4('Testing Live Update'),
    html.H4('Quality VS Time elapsed'),
    dcc.Graph(id='quality_graph'),
    html.H4('Noise ratio VS Time elapsed'),
    dcc.Graph(id='noiseratio_graph'),
    html.H4('Signal level VS Time elapsed'),
    dcc.Graph(id='signallevel_graph'),
    html.H4('Bitrate VS Time elapsed'),
    dcc.Graph(id='bitrate_graph'),
    dcc.Interval(
        id='interval',
        interval=1*1000,
        n_intervals=0
    )
])


@app.callback([Output('quality_graph', 'figure'),
               Output('noiseratio_graph', 'figure'),
               Output('signallevel_graph', 'figure'),
               Output('bitrate_graph', 'figure')],
              [Input('interval', 'n_intervals')])
def update_graph_live(n):

    data = ReadData()

    quality_trace = go.Scatter(
        x = data['time'],
        y = data['quality'],
        marker = {'color':'blue', 'size':10},
        mode = 'markers+lines'
    )

    quality_data = [quality_trace]
    quality_figure = go.Figure(quality_data)

    noiseratio_trace = go.Scatter(
        x=data['time'],
        y=data['noiseratio'],
        marker={'color': 'blue', 'size': 10},
        mode='markers+lines'
    )

    noiseratio_data = [noiseratio_trace]
    noiseratio_figure = go.Figure(noiseratio_data)

    signallevel_trace = go.Scatter(
        x = data['time'],
        y = data['signallevel'],
        marker = {'color':'blue', 'size':10},
        mode = 'markers+lines'
    )

    signallevel_data = [signallevel_trace]
    signallevel_figure = go.Figure(signallevel_data)

    bitrate_trace = go.Scatter(
        x = data['time'],
        y = data['bitrate'],
        marker = {'color':'blue', 'size':10},
        mode = 'markers+lines'
    )

    bitrate_data = [bitrate_trace]
    bitrate_figure = go.Figure(bitrate_data)

    return quality_figure, noiseratio_figure, signallevel_figure, bitrate_figure


if __name__ == '__main__':
    app.run_server(debug=True)