import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import random
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Button('Dark!', style={'backgroundColor':'black', 'color':'white', 'textAlign':'center'}, id='toggleButton', n_clicks=0)
], style={'backgroundColor':'white'}, id='mainDiv')


@app.callback([Output('toggleButton','children'),
               Output('toggleButton','style'),
               Output('mainDiv','style')],
              [Input('toggleButton','n_clicks')])
def BGColorToggle(clicks):
    if clicks%2 == 1:
        return 'Light!', {'backgroundColor':'white', 'color':'#b30000'}, {'backgroundColor':'black'}
    else:
        return 'Dark!', {'backgroundColor':'black', 'color':'#fdf7c2'}, {'backgroundColor':'white'}


if __name__ == '__main__':
    app.run_server(debug=True)