import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from app_helpers import *
from graph2 import *
from get_stats import *
import flask
import os 
import uuid

from dash.dependencies import Input, Output, State


external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/slate/bootstrap.min.css']

categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    
formatting = {}
for each in categories:
    formatting[each] = float
    
df = pd.read_csv('attachment_data.csv',dtype=formatting)

weapons = create_options(df.Weapon.unique())

empty=[]

fig = make_graph()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.Br(),

    html.Div(
        id = 'weapon-block',
        style = {'textAlign': 'center',
                 'margin' : 'auto',
                 'width' : '60%'},
        children = [
            html.H1('CALL OF DUTY : MODERN WARFARE WEAPON STATS VISUALIZATION',
                    style = {"text-decoration": "underline"}),
            html.Br(),

            html.H2("WHAT'S YOUR GAMERTAG?"),
            dcc.Input(id = "gamertag",
                      type = 'text',
                      value = 'Enter Gamertag',
                      style = {'textAlign': 'center'},
            ),
            html.Br(),
            html.Br(),

            html.H2('CHOOSE YOUR WEAPON'),
            dcc.Dropdown(
                id = 'weapon-dropdown',
                options = weapons,
                value = 'M4A1'
            ),
            html.Br(),
            html.H3('This is my rifle.  There are many like it, but this one is mine.')
        ]
    ),

    html.Br(),
    html.Br(),

    html.Div(id = 'attachment-block',
        style = {'textAlign': 'center'},
        children = [
            html.Div(
                className = 'card',
                style = {'width' : '18%',
                         'display': 'inline-block',
                         'marginLeft': '1%', 
                         'marginRight': '1%',
                         },
                children = [
                    html.Div(
                        className = 'card-header',
                        children=[
                            html.H3('Attachment 1')
                        ]
                    ),
                    html.Br(),
                    html.H4('Category:'),
                    dcc.Dropdown(
                        id='cat1',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.H4('Attachment:'),
                    dcc.Dropdown(
                        id='att1',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),

            html.Div(
                className = 'card',
                style = {'width' : '18%',
                         'display': 'inline-block',
                         'marginLeft': '1%', 
                         'marginRight': '1%',
                         },
                children = [
                    html.Div(
                        className = 'card-header',
                        children=[
                            html.H3('Attachment 2')
                        ]
                    ),
                    html.Br(),
                    html.H4('Category:'),
                    dcc.Dropdown(
                        id='cat2',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.H4('Attachment:'),
                    dcc.Dropdown(
                        id='att2',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),

            html.Div(
                className = 'card',
                style = {'width' : '18%',
                         'display': 'inline-block',
                         'marginLeft': '1%', 
                         'marginRight': '1%',
                         },
                children = [
                    html.Div(
                        className = 'card-header',
                        children=[
                            html.H3('Attachment 3')
                        ]
                    ),
                    html.Br(),
                    html.H4('Category:'),
                    dcc.Dropdown(
                        id='cat3',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.H4('Attachment:'),
                    dcc.Dropdown(
                        id='att3',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),

            html.Div(
                className = 'card',
                style = {'width' : '18%',
                         'display': 'inline-block',
                         'marginLeft': '1%', 
                         'marginRight': '1%',
                         },
                children = [
                    html.Div(
                        className = 'card-header',
                        children=[
                            html.H3('Attachment 4')
                        ]
                    ),
                    html.Br(),
                    html.H4('Category:'),
                    dcc.Dropdown(
                        id='cat4',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.H4('Attachment:'),
                    dcc.Dropdown(
                        id='att4',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),

            html.Div(
                className = 'card',
                style = {'width' : '18%',
                         'display': 'inline-block',
                         'marginLeft': '1%', 
                         'marginRight': '1%',
                         },
                children = [
                    html.Div(
                        className = 'card-header',
                        children=[
                            html.H3('Attachment 5')
                        ]
                    ),
                    html.Br(),
                    html.H4('Category:'),
                    dcc.Dropdown(
                        id='cat5',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.H4('Attachment:'),
                    dcc.Dropdown(
                        id='att5',
                        options=empty,
                        value='None'
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),
        ]
    ),
    
    html.Br(),
    html.Br(),

    html.Div(
        style = {'textAlign': 'center'},
        children = [
            dcc.Graph(
                id = 'radar',
                style={'width':'80%',
                'display': 'inline-block',
                'marginLeft': '1%', 
                'marginRight': '0%',
                'verticalAlign': 'top', },
                figure=fig),   

            # html.Div(
            #     className = 'card',
            #     style={'width':'46%', 
            #     'display': 'inline-block',
            #     'marginLeft': '0%', 
            #     'marginRight': '1%',
            #     'verticalAlign': 'top', },
            #     children = [
            #         html.Div(
            #             className = "card-header",
            #             children = [
            #                 html.H2(
            #                     id = 'table-title', 
            #                     children = 'GUN NAME'
            #                 )
            #             ]
            #         ),
            #         html.Div(
            #             style = {'textAlign':'left'},
            #             children = [
            #                 html.H4(
            #                     id = 'tablecat1',
            #                     children = 'Attachment 1'
            #                     ),
            #                 html.H5(
            #                     id = 'table-att1',
            #                     children = 'Attachment Name'
            #                 ),
            #                 html.Br(),

            #                 html.H4(
            #                     id = 'tablecat2',
            #                     children = 'Attachment 2'
            #                     ),
            #                 html.H5(
            #                     id = 'table-att2',
            #                     children = 'Attachment Name'
            #                 ),
            #                 html.Br(),

            #                 html.H4(
            #                     id = 'tablecat3',
            #                     children = 'Attachment 3'
            #                     ),
            #                 html.H5(
            #                     id = 'table-att3',
            #                     children = 'Attachment Name'
            #                 ),
            #                 html.Br(),

            #                 html.H4(
            #                     id = 'tablecat4',
            #                     children = 'Attachment 4'
            #                     ),
            #                 html.H5(
            #                     id = 'table-att4',
            #                     children = 'Attachment Name'
            #                 ),
            #                 html.Br(),

            #                 html.H4(
            #                     id = 'tablecat5',
            #                     children = 'Attachment 5'
            #                     ),
            #                 html.H5(
            #                     id = 'table-att5',
            #                     children = 'Attachment Name'
            #                 ),
            #                 html.Br(),
            #             ]
            #         )
            #     ]
            # ),
        ]
    ),
    html.Br(),
    html.Br(),
    html.H2(
        style = {'textAlign': 'center'},
        children = [html.H1('Save your customized weapon',
                            style = {"text-decoration": "underline"}),
                    'Step 1: Hit the "Generate Image" button',html.Br(),
                    'Step 2: Hit the "Download Image" button',html.Br(),
                    'Step 3: Share your creation!',html.Br(),
        ]

    ),
    html.Div(
        style = {'textAlign': 'center'},
        children = [
            html.Button(
                    style = {'margin':'2%'},
                    id="generate",
                    className="btn btn-primary btn-lg",
                    children="GENERATE IMAGE"),
            html.A(
                'DOWNLOAD IMAGE',
                style = {'margin':'2%'},    
                className = "btn btn-primary btn-lg",
                id='download-link',
                download="",
                href="",
                target="_blank"
            )
        ]
    ),
])


@app.callback([
    dash.dependencies.Output('download-link', 'href'),
    dash.dependencies.Output('download-link', 'download')],
    [dash.dependencies.Input("generate", "n_clicks")],
    [dash.dependencies.State("radar", "figure"),
    dash.dependencies.State('gamertag', 'value'),
    dash.dependencies.State('weapon-dropdown', 'value')])
def update_download_link(n_clicks,fig1,gamer,wep):
    chart = go.Figure(fig1)
    filename = "{} - {}.png".format(gamer,wep)
    path = 'static/' + filename
    chart.write_image(path)
    return path, path
    

# @app.callback([
#     dash.dependencies.Output('download-link', 'href'),
#     dash.dependencies.Output('download-link', 'download')],
#     [dash.dependencies.Input("download-link", "n_clicks")],
#     [dash.dependencies.State("radar", "figure"),
#     dash.dependencies.State('gamertag', 'value'),
#     dash.dependencies.State('weapon-dropdown', 'value')])
# def update_download_link(n_clicks,fig1,gamer,wep):
#     chart = go.Figure(fig1)
#     filename = "{} - {}.png".format(gamer,wep)
#     path = 'static/' + filename
#     chart.write_image(path)
#     return path, path

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

# @app.callback(
#     dash.dependencies.Output('table-att1', 'children'),
#     [dash.dependencies.Input('att1', 'value'),])
# def update_dropdown(att_val):
#     return att_val

# @app.callback(
#     dash.dependencies.Output('table-att2', 'children'),
#     [dash.dependencies.Input('att2', 'value'),])
# def update_dropdown(att_val):
#     return att_val

# @app.callback(
#     dash.dependencies.Output('table-att3', 'children'),
#     [dash.dependencies.Input('att3', 'value'),])
# def update_dropdown(att_val):
#     return att_val

# @app.callback(
#     dash.dependencies.Output('table-att4', 'children'),
#     [dash.dependencies.Input('att4', 'value'),])
# def update_dropdown(att_val):
#     return att_val

# @app.callback(
#     dash.dependencies.Output('table-att5', 'children'),
#     [dash.dependencies.Input('att5', 'value'),])
# def update_dropdown(att_val):
#     return att_val

@app.callback(
    dash.dependencies.Output('radar', 'figure'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('gamertag', 'value'),
    dash.dependencies.Input('att1', 'value'),
    dash.dependencies.Input('att2', 'value'),
    dash.dependencies.Input('att3', 'value'),
    dash.dependencies.Input('att4', 'value'),
    dash.dependencies.Input('att5', 'value'),])
def update_dropdown(wep, gamertag, att1, att2, att3, att4, att5):
    attachments = [att1, att2, att3, att4, att5]
    base = base_stats(df, wep)
    agg = aggregate(df, wep, attachments)
    return make_graph(base, agg, wep, gamertag)




# ----


if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)