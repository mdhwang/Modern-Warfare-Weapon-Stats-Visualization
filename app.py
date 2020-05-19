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

empty=[]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H2('CHOOSE YOUR WEAPON'),
    dcc.Dropdown(
        id='weapon-dropdown',
        options=weapons,
        value='None'
    ),
    html.Br(),

    html.H5('Attachment 1'),
    html.P('Category:'),
    dcc.Dropdown(
        id='cat1',
        options=empty,
        value='None'
    ),
    html.Br(),
    html.P('Attachment:'),
    dcc.Dropdown(
        id='att1',
        options=empty,
        value='None'
    ),

    html.Br(),
    html.H5('Attachment 2'),
    html.P('Category:'),
    dcc.Dropdown(
        id='cat2',
        options=empty,
        value='None'
    ),
    html.Br(),
    html.P('Attachment:'),
    dcc.Dropdown(
        id='att2',
        options=empty,
        value='None'
    ),

    html.Br(),
    html.H5('Attachment 3'),
    html.P('Category:'),
    dcc.Dropdown(
        id='cat3',
        options=empty,
        value='None'
    ),
    html.Br(),
    html.P('Attachment:'),
    dcc.Dropdown(
        id='att3',
        options=empty,
        value='None'
    ),

    html.Br(),
    html.H5('Attachment 4'),
    html.P('Category:'),
    dcc.Dropdown(
        id='cat4',
        options=empty,
        value='None'
    ),
    html.Br(),
    html.P('Attachment:'),
    dcc.Dropdown(
        id='att4',
        options=empty,
        value='None'
    ),

    html.Br(),
    html.H5('Attachment 5'),
    html.P('Category:'),
    dcc.Dropdown(
        id='cat5',
        options=empty,
        value='None'
    ),
    html.Br(),
    html.P('Attachment:'),
    dcc.Dropdown(
        id='att5',
        options=empty,
        value='None'
    ),


    
])


@app.callback([
    dash.dependencies.Output('cat1', 'options'),
    dash.dependencies.Output('cat2', 'options'),
    dash.dependencies.Output('cat3', 'options'),
    dash.dependencies.Output('cat4', 'options'),
    dash.dependencies.Output('cat5', 'options'),],
    [dash.dependencies.Input('weapon-dropdown', 'value')])
def update_dropdown(value):
    cat_mask = (df.Weapon == value)
    cat = create_options(df[cat_mask].Category.unique())
    return cat, cat, cat, cat, cat

@app.callback(
    dash.dependencies.Output('att1', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat1', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att2', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat2', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att3', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat3', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att4', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat4', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att5', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat5', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att




if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)