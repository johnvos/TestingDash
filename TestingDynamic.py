import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([html.H1("This should be a RED banner, if css works.")], className='banner'),
    html.H1("Testing"),
    dcc.Dropdown(
        id='deviceNames',
        options=[
            {'label':'Device 1', 'value':'device1'},
            {'label':'Device 2', 'value':'device2'}
        ],
        placeholder="No device found",
        searchable=True
    ),
    html.Div([
        html.Div([
            html.Br(),
            html.H3("This will be data 1"),
            html.Br()
        ], id='dataBlock1', className='dataBlock'),

        html.Div([
            html.Br(),
            html.H3("This will be data 2"),
            html.Br()
        ], id='dataBlock2', style={'backgroundColor':'blue', 'float':'left', 'width':'33.33%', 'color':'white'}),

        html.Div([
            html.Br(),
            html.H3("This will be data 3"),
            html.Br()
        ], id='dataBlock3', style={'backgroundColor':'green', 'float':'left', 'width':'33.33%', 'color':'white'})
    ], id='dataDisplay', style={'display':'table', 'width':'100%'})
])

class Device:
    def __init__(self, name, information1, information2, information3):
        self.name = name
        self.information1 = information1
        self.information2 = information2
        self.information3 = information3

placeHolderData={
    'device1':Device("Device1","255.0.0.1","$300","DELL"),
    'device2':Device("Device2","123.1.2.3","$10000","APPLE")
}


@app.callback([Output('dataBlock1','children'),
               Output('dataBlock2','children'),
               Output('dataBlock3','children')],
              [Input('deviceNames','value')])
def update_data_blocks(name):
    if name is None:
        return html.H3("This will be data 1"), html.H3("This will be data 2"), html.H3("This will be data 3")
    elif placeHolderData[name] is None:
        return html.H3("This will be data 1"), html.H3("This will be data 2"), html.H3("This will be data 3")
    else:
        device = placeHolderData[name]
        return device.information1, device.information2, device.information3


if __name__ == '__main__':
    app.run_server(debug=True)