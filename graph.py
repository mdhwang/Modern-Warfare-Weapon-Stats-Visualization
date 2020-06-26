import plotly.graph_objects as go
import plotly.express as px

from plotly.subplots import make_subplots


from get_stats import *


m4base = [0,0,0,0,0,0]
upgrade = [0,0,0,0,0,0]


categories = ['   Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    
formatting = {}
for each in categories:
    formatting[each] = float
    
df = pd.read_csv('attachment_data.csv',dtype=formatting)

attachments = [0,0,0,0,0]
cat = [0,0,0,0,0]

values = table_agg(df, "M4A1", attachments, cat)

def make_graph(original = m4base, updated = upgrade, gun = "M4A1", gamertag = "Gamertag", guncode = "Guncode",values = values):

    fig = make_subplots(
        rows = 1, 
        cols = 1,
        specs = [
            [{"type": "scatterpolar"}],
        ]
    )
    
    fig.add_trace(
            go.Scatterpolar(
                mode = "lines",
                fillcolor = 'green',
                line = dict(color = 'green',
                            width = 3
                    ),
                opacity = 0.5,
                r = updated,
                theta = categories,
                fill = "toself",
                showlegend = False,
                hoverinfo="none",
            ),
            row = 1, col = 1
    )
        
    fig.add_trace(
            go.Scatterpolar(
                mode = "lines",
                fillcolor = '#ffa07a ',
                opacity = 0.25,
                r = original,
                theta = categories,
                fill = "toself",
                showlegend = False,
                hoverinfo="none",
            ),
            row = 1, col = 1
    )

    fig.update_layout(
        height = 1000,
        width = 1000,
        dragmode = False,
        title={
            'text': guncode,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(
                family = "Courier New, monospace",
                size = 50,
                color = "green"
                ),
            },
        template = "plotly_dark",
        transition =  {
                'duration': 1000,
                'easing': 'cubic-in-out'},
        font = dict(
            family = "Helvetica",
            size = 18,
            color = "gray"
            ),
        margin = {'t':150,
                  'b':150
                },
        polar = dict(
            radialaxis = dict(showticklabels = True, 
                            color = 'gray',
                            tickangle = 0,
                            tickfont = dict(size = 12),
                            range = [0,100],
                            )
            ),
        annotations=[
            go.layout.Annotation(
                showarrow = False,
                text = 'Custom {} Build Created By {}'.format(gun, gamertag),
                xanchor = 'center',
                x = 0.5,
                yanchor = 'top',
                y = 0,
                font = dict(
                    family = "Courier New, monospace",
                    size = 24,
                    color = "green",
                ),
                yshift = -50,
            ),

            go.layout.Annotation(
                showarrow = False,
                text = 'Make Yours On IG At:<br>@The_Gulag_Gunsmith',
                xanchor = 'center',
                x = 0.95,
                yanchor = 'top',
                y = 0,
                font = dict(
                    family = "Courier New, monospace",
                    size = 14,
                    color = "gray",
                ),
                yshift = -100,
                align = "center",
            )
        ]
    )


    return fig

def make_table(original = m4base, updated = upgrade, gun = "M4A1", gamertag = "Gamertag", guncode = "Guncode",values = values):

    fig = make_subplots(
        rows = 1, 
        cols = 1,
        specs = [
            [{"type": "table"}]
        ]
    )
    
    fig.add_trace(
        go.Table(        
            columnwidth = [0.125, 0.275, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            header = dict(
                values = ["Category","Attachment",'Accuracy','Damage','Range','Fire Rate','Mobility','Control'],
                font = dict(size = 14,
                            color = "black"),
                height = 30,
                align = "center",
                fill_color = [
                    ["rgba(100, 149, 237, 0.85)"] * 8,
                ]
            ),
            cells = dict(
                values = [
                    values.Category, 
                    values.Attachment, 
                    values.Accuracy, 
                    values.Damage, 
                    values.Range, 
                    values['Fire Rate'], 
                    values.Mobility,
                    values.Control
                ],
                
                fill_color=[
                    ["rgb(200, 200, 200)"]*len(values),
                    ["rgb(200, 200, 200)"]*len(values),
                    values.Accuracy_color,
                    values.Damage_color,
                    values.Range_color,
                    values['Fire Rate_color'],
                    values.Mobility_color,
                    values.Control_color,
                ],
                height = 24,
                align = "center",
                font = dict(size = 12,
                            color = "black"),
            )
        ),
        row=1, col=1,
    )
    
    fig.update_layout(
        height = 600,
        width = 1000,
        title={
            'text': guncode,
            'y':0.93,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(
                family = "Courier New, monospace",
                size = 50,
                color = "green"
                ),
            },
        template = "plotly_dark",
        transition =  {
                'duration': 1000,
                'easing': 'cubic-in-out'},
        font = dict(
            family = "Helvetica",
            size = 18,
            color = "gray"
            ),
        margin = {'t':150,
                  'b':150
        },
        annotations=[
            go.layout.Annotation(
                showarrow = False,
                text = 'Custom {} Build Created By {}'.format(gun, gamertag),
                xanchor = 'center',
                x = 0.5,
                yanchor = 'top',
                y = 0,
                font = dict(
                    family = "Courier New, monospace",
                    size = 24,
                    color = "green",
                ),
                yshift = -50,
            ),

            go.layout.Annotation(
                showarrow = False,
                text = 'Make Yours On IG At:<br>@The_Gulag_Gunsmith',
                xanchor = 'center',
                x = 0.95,
                yanchor = 'top',
                y = 0,
                font = dict(
                    family = "Courier New, monospace",
                    size = 14,
                    color = "gray",
                ),
                yshift = -100,
                align = "center",
            )
        ]
        )


    return fig