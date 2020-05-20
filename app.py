import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from app_helpers import *
from graph import *
from get_stats import *

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
            html.H1('CALL OF DUTY : MODERN WARFARE WEAPON STATS VISUALIZATION'),
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
                style={'width':'46%',
                'display': 'inline-block',
                'marginLeft': '1%', 
                'marginRight': '0%',
                'verticalAlign': 'top', },
                figure=fig),   

            html.Div(
                className = 'card',
                style={'width':'46%', 
                'display': 'inline-block',
                'marginLeft': '0%', 
                'marginRight': '1%',
                'verticalAlign': 'top', },
                children = [
                    html.Div(
                        className = "card-header",
                        children = [
                            html.H2(
                                id = 'table-title', 
                                children = 'GUN NAME'
                            )
                        ]
                    ),
                    html.Div(
                        style = {'textAlign':'left'},
                        children = [
                            html.H4(
                                id = 'tablecat1',
                                children = 'Attachment 1'
                                ),
                            html.H5(
                                id = 'table-att1',
                                children = 'Attachment Name'
                            ),
                            html.Br(),

                            html.H4(
                                id = 'tablecat2',
                                children = 'Attachment 2'
                                ),
                            html.H5(
                                id = 'table-att2',
                                children = 'Attachment Name'
                            ),
                            html.Br(),

                            html.H4(
                                id = 'tablecat3',
                                children = 'Attachment 3'
                                ),
                            html.H5(
                                id = 'table-att3',
                                children = 'Attachment Name'
                            ),
                            html.Br(),

                            html.H4(
                                id = 'tablecat4',
                                children = 'Attachment 4'
                                ),
                            html.H5(
                                id = 'table-att4',
                                children = 'Attachment Name'
                            ),
                            html.Br(),

                            html.H4(
                                id = 'tablecat5',
                                children = 'Attachment 5'
                                ),
                            html.H5(
                                id = 'table-att5',
                                children = 'Attachment Name'
                            ),
                            html.Br(),
                        ]
                    )
                ]
            )
        ]
    ),

    
])


@app.callback([
    dash.dependencies.Output('cat1', 'options'),
    dash.dependencies.Output('cat2', 'options'),
    dash.dependencies.Output('cat3', 'options'),
    dash.dependencies.Output('cat4', 'options'),
    dash.dependencies.Output('cat5', 'options'),
    dash.dependencies.Output('table-title', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value')])
def update_dropdown(value):
    cat_mask = (df.Weapon == value)
    cat = create_options(df[cat_mask].Category.unique())
    return cat, cat, cat, cat, cat, 'Custom {} Build'.format(value)

@app.callback(
    [dash.dependencies.Output('att1', 'options'),
    dash.dependencies.Output('tablecat1', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat1', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att, "- Attachment 1: {}".format(cat_val)

@app.callback(
    [dash.dependencies.Output('att2', 'options'),
    dash.dependencies.Output('tablecat2', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat2', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att, "- Attachment 2: {}".format(cat_val)

@app.callback(
    [dash.dependencies.Output('att3', 'options'),
    dash.dependencies.Output('tablecat3', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat3', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att, "- Attachment 3: {}".format(cat_val)

@app.callback(
    [dash.dependencies.Output('att4', 'options'),
    dash.dependencies.Output('tablecat4', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat4', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att, "- Attachment 4: {}".format(cat_val)

@app.callback(
    [dash.dependencies.Output('att5', 'options'),
    dash.dependencies.Output('tablecat5', 'children'),],
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('cat5', 'value'),])
def update_dropdown(wep_val,cat_val):
    att_mask = (df.Weapon == wep_val) & (df.Category == cat_val)
    att = create_options(df[att_mask].Attachment.to_list())
    return att, "- Attachment 5: {}".format(cat_val)

@app.callback(
    dash.dependencies.Output('table-att1', 'children'),
    [dash.dependencies.Input('att1', 'value'),])
def update_dropdown(att_val):
    return att_val

@app.callback(
    dash.dependencies.Output('table-att2', 'children'),
    [dash.dependencies.Input('att2', 'value'),])
def update_dropdown(att_val):
    return att_val

@app.callback(
    dash.dependencies.Output('table-att3', 'children'),
    [dash.dependencies.Input('att3', 'value'),])
def update_dropdown(att_val):
    return att_val

@app.callback(
    dash.dependencies.Output('table-att4', 'children'),
    [dash.dependencies.Input('att4', 'value'),])
def update_dropdown(att_val):
    return att_val

@app.callback(
    dash.dependencies.Output('table-att5', 'children'),
    [dash.dependencies.Input('att5', 'value'),])
def update_dropdown(att_val):
    return att_val

@app.callback(
    dash.dependencies.Output('radar', 'figure'),
    [dash.dependencies.Input('weapon-dropdown', 'value'),
    dash.dependencies.Input('att1', 'value'),
    dash.dependencies.Input('att2', 'value'),
    dash.dependencies.Input('att3', 'value'),
    dash.dependencies.Input('att4', 'value'),
    dash.dependencies.Input('att5', 'value'),])
def update_dropdown(wep, att1, att2, att3, att4, att5):
    attachments = [att1, att2, att3, att4, att5]
    base = base_stats(df, wep)
    agg = aggregate(df, wep, attachments)
    return make_graph(base, agg, wep)




# @app.callback(
#     dash.dependencies.Output('radar', 'figure'),
#     [dash.dependencies.Input('weapon-dropdown', 'value')])
# def update_dropdown(wep_val):
#     return make_graph(gun = wep_val)



if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)