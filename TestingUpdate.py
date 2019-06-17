import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

startTime = time.process_time()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H4('Testing Live Update'),
    html.Div(id='live_update_text'),
    dcc.Graph(id='live_update_graph'),
    dcc.Interval(
        id='interval',
        interval=1*1000,
        n_intervals=0
    )
])

@app.callback(Output('live_update_text', 'children'),
              [Input('interval', 'n_intervals')])
def update_metrics(n):
    timeTaken = time.process_time() - startTime
    return html.Span('Time taken: {}'.format(timeTaken))


@app.callback(Output('live_update_graph', 'figure'),
              [Input('interval', 'n_intervals')])
def update_graph_live(n):
    timeTaken = time.process_time() - startTime
    #testing
    return{
        'data':[{
            'type': 'scatter',
            'y': timeTaken
        }]
    }
    

if __name__ == '__main__':
    app.run_server(debug=True)
