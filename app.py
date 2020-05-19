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

weapons = create_options(df.Weapon.unique())

stocks_mask = (df.Weapon == "M4A1") & (df.Category == "STOCK")
stocks = create_options(df[stocks_mask].Attachment.to_list())

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='weapon-dropdown',
        options=weapons,
        value='M4A1'
    ),
    html.Div(id='dd-output-container'),
    html.Br(),
    dcc.Dropdown(
        id='stocks',
        options=stocks,
        value='Choose Stock Attachment'
    ),
    html.Div(id='stock-output-container'),
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('weapon-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('stock-output-container', 'children'),
    [dash.dependencies.Input('stocks', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)




if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)