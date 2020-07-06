import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
from app_helpers import *
from graph import *
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
    
df = pd.read_csv('attachment_data.csv',dtype = formatting)

weapons = create_options(df.Weapon.unique())

empty = []


a = [1,2,3,4,5]

fig = make_graph()
fig2 = make_table()

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.title = 'The Gulag Gunsmith'
server = app.server
app.layout = html.Div([

    html.Br(),
    html.Div(
        style = {'textAlign': 'center',
                 'margin' : 'auto',
                 'width' : '60%'},
        children=[
            html.Img(src='https://raw.githubusercontent.com/mdhwang/Modern-Warfare-Weapon-Stats-Visualization/master/images/title.png',),
        ]
    ),
    html.Br(),
    html.Br(),
    html.Div(
        id = 'weapon-block',
        style = {'textAlign': 'center',
                 'margin' : 'auto',
                 'width' : '80%'},
        children = [
            html.Br(),
            html.H3('Pretty straight forward - enter your gamer info and build out your custom COD:MW weapons using the dropdowns.'),
            html.H3('Weapon stats were pulled from in game menus and use a python based computer vision script to determine the +/- of attachments'),
            html.H3('Data is compiled and charted out for you to min/max everything.'),
            html.Br(),
            html.H3('Good Hunting'),
            html.Br(),
            html.Hr(),
            html.Br(),
            html.H2("WHAT'S YOUR GAMERTAG?"),
            dcc.Input(id = "gamertag",
                      type = 'text',
                      value = 'John Wick',
                      style = {'textAlign': 'center'},
            ),
            html.Br(),
            html.Br(),

            html.H2("NAME YOUR BUILD"),
            dcc.Input(id = "guncode",
                      type = 'text',
                      value = 'YeetCannon5000',
                      style = {'textAlign': 'center'},
            ),
            html.Br(),
            html.Br(),
            html.Div(
                style = {'textAlign': 'center',
                        'margin' : 'auto',
                        'width' : '60%'},
                children = [
                    html.H2('CHOOSE YOUR WEAPON'),
                    dcc.Dropdown(
                        id = 'weapon-dropdown',
                        options = weapons,
                        value = 'M4A1'
                    ),
                ]
            ),
            
            html.Br(),
            html.H3('This is my rifle.  There are many like it, but this one is mine.')
        ]
    ),
    html.Hr(),

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
        style = {'textAlign': 'center',
                'display': 'inline-block',
                'width':'100%',},
        children = [
            dcc.Graph(
                id = 'radar',
                style={
                    'textAlign': 'center',
                    'display': 'inline-block',
                    'marginLeft': '0%', 
                    'marginRight': '0%',
                    'verticalAlign': 'top', 
                },
                figure = fig
            ),   
        ]
    ),
    
    html.Br(),

    html.Br(),

    html.Br(),

    html.Div(
        style = {'textAlign': 'center',
                'display': 'inline-block',
                'width':'100%',},
        children = [
            dcc.Graph(
                id = 'radar2',
                style={
                    'textAlign': 'center',
                    'display': 'inline-block',
                    'marginLeft': '0%', 
                    'marginRight': '0%',
                    'verticalAlign': 'top', 
                },
                figure = fig2
            ),   
        ]
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(),

    html.Div(
        style = {'textAlign': 'center',
                 'width' : '50%',
                 'margin' : 'auto', },
        children = [
            # html.H1("Stats Chart:"),
            html.Button(
                    style = {'margin':'2%'},
                    id="generate",
                    className="btn btn-primary btn-lg",
                    children="Add Build to Gulag"),
            html.Br(),
        ]
    ),


    html.Div(
        style = {'textAlign': 'center',
                'display': 'inline-block',
                'width':'100%',},
        children = [
            dcc.Graph(
                id = 'gulag1',
                style={
                    'textAlign': 'center',
                    'display': 'inline-block',
                    'marginLeft': '0%', 
                    'marginRight': '0%',
                    'verticalAlign': 'top', 
                },
                figure = fig2
            ),   
        ]
    ),


    html.Div(
        style = {'textAlign': 'center',
                'display': 'inline-block',
                'width':'100%',},
        children = [
            dcc.Graph(
                id = 'gulag2',
                style={
                    'textAlign': 'center',
                    'display': 'inline-block',
                    'marginLeft': '0%', 
                    'marginRight': '0%',
                    'verticalAlign': 'top', 
                },
                figure = fig2
            ),   
        ]
    ),

    # html.H2(
    #     style = {'textAlign': 'center'},
    #     children = [html.H1('Save your customized weapon',
    #                         style = {"text-decoration": "underline"}),
    #                 'Step 1: Hit the "Generate Image" button',html.Br(),
    #                 'Step 2: Hit the "Download Image" button',html.Br(),
    #                 'Step 3: Share your creation!',html.Br(),
    #     ]

    # ),

    # html.Br(),
    # html.Hr(),

    # html.Div(
    #     style = {'textAlign': 'center',
    #                      'width' : '50%',
    #                      'display': 'inline-block', },
    #     children = [
    #         html.H1("Stats Chart:"),
    #         html.Button(
    #                 style = {'margin':'2%'},
    #                 id="generate",
    #                 className="btn btn-primary btn-lg",
    #                 children="GENERATE CHART"),
    #         html.Br(),
    #         html.A(
    #             'DOWNLOAD CHART',
    #             style = {'margin':'2%'},    
    #             className = "btn btn-primary btn-lg",
    #             id='download-link',
    #             download="",
    #             href="",
    #             target="_blank"
    #         )
    #     ]
    # ),



    # html.Div(
    #     style = {'textAlign': 'center',
    #                      'width' : '50%',
    #                      'display': 'inline-block',},
    #     children = [
    #         html.H1("Stats Table:"),
    #         html.Button(
    #                 style = {'margin':'2%'},
    #                 id="generate2",
    #                 className="btn btn-primary btn-lg",
    #                 children="GENERATE TABLE"),
    #         html.Br(),
    #         html.A(
    #             'DOWNLOAD TABLE',
    #             style = {'margin':'2%'},    
    #             className = "btn btn-primary btn-lg",
    #             id='download-link2',
    #             download="",
    #             href="",
    #             target="_blank"
    #         )
    #     ]
    # ),

    html.Br(),
    html.Br(),
    html.H5(
        style = {'textAlign': 'center'},
        children = ['Check out ',
                    html.A('@The_Gulag_Gunsmith',href = 'https://www.instagram.com/the_gulag_gunsmith/',target="_blank"),
                    ' on IG',
                    html.Br(),
                    'to see the stats for the COD:MW Blueprint Guns',
                    html.Br(),
                    html.Br(),
                    'If you enjoy this kind of content please consider donating to my ',
                    html.A('Patreon Link',href = 'https://www.patreon.com/the_gulag_gunsmith',target="_blank"),
                    html.Br(),
                    'to keep the server up and so I can keep making more content',
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Img(src='https://raw.githubusercontent.com/mdhwang/Modern-Warfare-Weapon-Stats-Visualization/master/images/MostInterestingCaptain.png'),
                    html.Br(),
                    html.Br(),
                    'Stay frosty my friends.',
                    html.Br(),
                    html.Br(),
        ]

    ),
])


@app.callback([
    dash.dependencies.Output('download-link2', 'href'),
    dash.dependencies.Output('download-link2', 'download')],
    [dash.dependencies.Input("generate2", "n_clicks")],
    [dash.dependencies.State("radar2", "figure"),
    dash.dependencies.State('gamertag', 'value'),
    dash.dependencies.State('weapon-dropdown', 'value')])
def update_download_link(n_clicks,fig1,gamer,wep):
    chart = go.Figure(fig1)
    filename = "Stats Table {} - {}.png".format(gamer,wep)
    path = 'static/' + filename
    chart.write_image(path, width = 1000, height = 600)
    return path, path
    
@app.callback([
    dash.dependencies.Output('download-link', 'href'),
    dash.dependencies.Output('download-link', 'download')],
    [dash.dependencies.Input("generate", "n_clicks")],
    [dash.dependencies.State("radar", "figure"),
    dash.dependencies.State('gamertag', 'value'),
    dash.dependencies.State('weapon-dropdown', 'value')])
def update_download_link(n_clicks,fig1,gamer,wep):
    chart = go.Figure(fig1)
    filename = "Stats Chart {} - {}.png".format(gamer,wep)
    path = 'static/' + filename
    chart.write_image(path, width = 1000, height = 1000)
    return path, path
    

@app.callback([
        dash.dependencies.Output('cat1', 'options'),
        dash.dependencies.Output('cat2', 'options'),
        dash.dependencies.Output('cat3', 'options'),
        dash.dependencies.Output('cat4', 'options'),
        dash.dependencies.Output('cat5', 'options'),
        dash.dependencies.Output('cat1', 'value'),
        dash.dependencies.Output('cat2', 'value'),
        dash.dependencies.Output('cat3', 'value'),
        dash.dependencies.Output('cat4', 'value'),
        dash.dependencies.Output('cat5', 'value'),
        dash.dependencies.Output('att1', 'value'),
        dash.dependencies.Output('att2', 'value'),
        dash.dependencies.Output('att3', 'value'),
        dash.dependencies.Output('att4', 'value'),
        dash.dependencies.Output('att5', 'value'),
    ],
    [
        dash.dependencies.Input('weapon-dropdown', 'value')
    ],
    [
        dash.dependencies.State('cat1', 'options'),
        dash.dependencies.State('cat2', 'options'),
        dash.dependencies.State('cat3', 'options'),
        dash.dependencies.State('cat4', 'options'),
        dash.dependencies.State('cat5', 'options'),
    ],
    )
def set_categories_from_weapon(weapon,c1,c2,c3,c4,c5):
    cat_mask = (df.Weapon == weapon) & (df.Category != "BASE")
    cats = df[cat_mask].Category.unique()
    cats = list(cats)
    cats.remove('Base')
    cat = create_options(cats)
    return cat, cat, cat, cat, cat, '', '', '', '', '', '', '', '', '', ''

@app.callback(
    dash.dependencies.Output('att1', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat1', 'value'),])
def set_attachments_from_categories(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att2', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat2', 'value'),])
def set_attachments_from_categories(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att3', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat3', 'value'),])
def set_attachments_from_categories(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att4', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat4', 'value'),])
def set_attachments_from_categories(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att

@app.callback(
    dash.dependencies.Output('att5', 'options'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat5', 'value'),])
def set_attachments_from_categories(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att


@app.callback(
    [dash.dependencies.Output('radar', 'figure'),
    dash.dependencies.Output('radar2', 'figure'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('gamertag', 'value'),
    dash.dependencies.Input('guncode', 'value'),
    dash.dependencies.Input('cat1', 'value'),
    dash.dependencies.Input('cat2', 'value'),
    dash.dependencies.Input('cat3', 'value'),
    dash.dependencies.Input('cat4', 'value'),
    dash.dependencies.Input('cat5', 'value'),
    dash.dependencies.Input('att1', 'value'),
    dash.dependencies.Input('att2', 'value'),
    dash.dependencies.Input('att3', 'value'),
    dash.dependencies.Input('att4', 'value'),
    dash.dependencies.Input('att5', 'value'),])
def generate_figures(wep, gamertag, guncode, cat1, cat2, cat3, cat4, cat5, att1, att2, att3, att4, att5):
    categories = [cat1, cat2, cat3, cat4, cat5]
    attachments = [att1, att2, att3, att4, att5]
    base = base_stats(df, wep)
    agg = aggregate(df, wep, attachments)
    table_values = table_agg(df, wep, attachments, categories)
    f1 = make_graph(base, agg, wep, gamertag, guncode, table_values)
    f2 = make_table(base, agg, wep, gamertag, guncode, table_values)
    return f1, f2 




# ----


if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)