import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go


app = dash.Dash(__name__)

data = [go.Bar(
    x=[1,2,3],
    y=[1,2,3]
)]

layout = go.Layout(
    xaxis=dict(range=[-1,12]),
    yaxis=dict(range=[-1,12])
)

figure = go.Figure(data,layout)

app.layout = html.Div([
    html.H1("Play with the slider and the graph!"),
    dcc.RangeSlider(id='horizontal', min=0,max=10,step=1,updatemode='drag',value=[0,11]),
    dcc.Graph(id='graph',figure=figure),
    dcc.Slider(id='vertical', min=0, max=10, step=1, updatemode='drag', value=5, vertical=True)
], style={'width':'100%','height':'100%'})




@app.callback(Output('graph','figure'),
              [Input('vertical','value'),
               Input('horizontal','value')])
def update_graph(height,width):
    yVal = []
    i=0
    while i < width[-1]-width[0]:
        yVal.append(height)
        i+=1
    return go.Figure([go.Bar(x=list(range(width[0],width[-1])),y=yVal)],layout)







if __name__ == '__main__':
    app.run_server(debug=True)