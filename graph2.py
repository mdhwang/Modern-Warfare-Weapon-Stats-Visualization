import plotly.graph_objects as go
import plotly.express as px

from plotly.subplots import make_subplots


m4base = [0,0,0,0,0,0]
upgrade = [0,0,0,0,0,0]

values = [['MUZZLE','BARREL','UNDERBARREL','GRIP','STOCK'],
         ['A','B','C','D','E']]

categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']

def make_graph(original = m4base, updated = upgrade, gun = "M4A1", gamertag = "Gamertag", guncode = "Guncode",values = values):

    fig = make_subplots(
        rows = 1, 
        cols = 2,
        column_widths=[0.4, 0.6],
        specs = [[{"type": "scatterpolar"},{"type": "table"}],]
    )
    
    fig.add_trace(
            go.Scatterpolar(
                mode = "lines",
                fillcolor = 'green',
                line = dict(color='green',width=3),
                opacity = 0.5,
                r = updated,
                theta = categories,
                fill = "toself",
                showlegend=False,
            ),
            row=1, col=1
    )
        
    fig.add_trace(
            go.Scatterpolar(
                mode = "lines",
                fillcolor = 'gray',
                line = dict(color='gray',width=3),
                opacity = 0.5,
                r = original,
                theta = categories,
                fill = "toself",
                showlegend=False),
            row=1, col=1
    )
    
    fig.add_trace(
        go.Table(        
            columnwidth = [0.3, 0.7],
            header = dict(
                values = ["CATEGORY","ATTACHMENT"],
                font = dict(size = 20,
                color = "black"),
                height = 36,
                align="left"
            ),
            cells = dict(
                values = values,
                height = 36,
                align = "left",
                font = dict(size = 16,
                color = "black"),
            )
        ),
        row=1, col=2,
    )
    
    fig.update_layout(
        title={
            'text': "{}'s {} BUILD <br> THE '{}'".format(gamertag, gun, guncode),
            'y':0.93,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(
                family="Courier New, monospace",
                size=32,
                color="green"
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
        margin = {'t':130},
        polar = dict(
            radialaxis = dict(showticklabels = True, 
                            color = 'gray',
                            tickangle = 0,
                            tickfont = dict(size = 12),
                            range = [0,100],)
            )
        )


    return fig