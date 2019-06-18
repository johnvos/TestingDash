import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

# Just testing out how the plotly graphs work, and how the drop down menu callback could be useful

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Select a graph to see how they look like."),
    dcc.Dropdown(
        id='graphType',
        options=[
            {'label':'Line Graph', 'value':'line'},
            {'label':'Pie Chart', 'value':'pie'},
            {'label':'Bar Graph', 'value':'bar'}
        ],
        value='line',
        searchable = False,
        clearable = False
    ),
    dcc.Graph(
        id='graph'
    ),
    html.H1("TESTING")
])

lineGraphData = [
    go.Scatter(
        x=[1,2,3,4,5],
        y=[1,2,1,2,3]
    ),
    go.Scatter(
        x=[1,2,3,4,5],
        y=[3,4,3,2,4]
    )
]

lineGraphFigure = go.Figure(lineGraphData)


pieGraphData = [go.Pie(
    labels=['blueberry','strawberry','apple','pumpkin','chocolate'],
    values=[90,85,80,10,50]
)]

pieGraphFigure = go.Figure(pieGraphData)


barGraphData = [go.Bar(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 1, 2, 3]
)]

barGraphFigure = go.Figure(barGraphData)

@app.callback(Output('graph','figure'),
              [Input('graphType','value')])
def update_graph(graphType):
    if graphType == 'line':
        return lineGraphFigure
    elif graphType == 'pie':
        return pieGraphFigure
    elif graphType == 'bar':
        return barGraphFigure
    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)
