import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

print(dcc.__version__)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    html.H6("RAWR!"),
    dcc.Link('Navigate to "/button!"', href='/button!'),
    html.Div(id='page-content')
])


@app.callback(Output('page-content','children'),
              [Input('url','pathname')])
def display_page(pathname):
    return html.Div([
        html.H3("You clicked {}".format(pathname))
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
