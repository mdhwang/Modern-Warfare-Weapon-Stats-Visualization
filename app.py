import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from app_helpers import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

types = ['MUZZLE','BARREL','UNDERBARREL','GRIP','STOCK','LASER','BASE']
categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    
formatting = {}
for each in categories:
    formatting[each] = float
    
df = pd.read_csv('attachment_data.csv',dtype=formatting)

stonks = df[df.Category == "STOCK"].Attachment.to_list()
options = create_options("STOCK",stonks)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=options,
        value='Select {}'.format("Stock")
    ),
    html.Div(id='dd-output-container')
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)