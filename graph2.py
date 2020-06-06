import plotly.graph_objects as go
import plotly.express as px

from plotly.subplots import make_subplots


from get_stats import *


m4base = [0,0,0,0,0,0]
upgrade = [0,0,0,0,0,0]


categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    
formatting = {}
for each in categories:
    formatting[each] = float
    
df = pd.read_csv('attachment_data.csv',dtype=formatting)

attachments = []
cat = []

values = table_agg(df, "M4A1", attachments, cat)

def make_graph(original = m4base, updated = upgrade, gun = "M4A1", gamertag = "Gamertag", guncode = "Guncode",values = values):

    fig = make_subplots(
        rows = 2, 
        cols = 1,
        specs = [
            [{"type": "scatterpolar"}],
            [{"type": "table"}]
        ]
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
                fillcolor = '#ffa07a ',
                line = dict(color='red',width=2),
                opacity = 0.25,
                r = original,
                theta = categories,
                fill = "toself",
                showlegend=False),
            row=1, col=1
    )

    fig.add_trace(
        go.Table(        
            columnwidth = [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            header = dict(
                values = ["Category","Attachment",'Accuracy','Damage','Range','Fire Rate','Mobility','Control'],
                font = dict(size = 20,
                color = "black"),
                height = 36,
                align="left"
            ),
            cells = dict(
                values = [values.Category, 
                          values.Attachment, 
                          values.Accuracy, 
                          values.Damage, 
                          values.Range, 
                          values['Fire Rate'], 
                          values.Mobility,
                          values.Control],
                height = 36,
                align = "left",
                font = dict(size = 16,
                color = "black"),
            )
        ),
        row=2, col=1,
    )
    
    fig.update_layout(
        height = 1000,
        width = 1000,
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
        margin = {'t':200},
        polar = dict(
            radialaxis = dict(showticklabels = True, 
                            color = 'gray',
                            tickangle = 0,
                            tickfont = dict(size = 12),
                            range = [0,100],)
            )
        )


    return fig

def make_table(original = m4base, updated = upgrade, gun = "M4A1", gamertag = "Gamertag", guncode = "Guncode",values = values):
    pass