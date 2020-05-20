import plotly.graph_objects as go
import plotly.express as px


m4base = [71.13, 71.83, 63.03, 67.96, 63.03, 71.83]

upgrade = [81.13, 69, 73.03, 50, 73.03, 81.83]

categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']

def make_graph(original = m4base, updated = upgrade, gun = "M4A1"):

    fig = px.line_polar(r = updated, 
                        theta = categories, 
                        line_close = True,
                        range_r = [0,100],
                        render_mode = 'svg',
                        template = "plotly_dark",
                        width=500,
                        height=500,
                    )
    
    fig.update_traces(fill='toself',line_color='green')
    
    fig.update_layout(
        title={
            'text': "{} STATS".format(gun),
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(
                family="Courier New, monospace",
                size=32,
                color="green"
                ),
            },
        
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
                            tickfont = dict(size = 16)),
            )
        )

    fig.add_trace(go.Scatterpolar(
            mode = "lines",
            fillcolor = 'gray',
            line = dict(color='gray',width=3),
            opacity = 0.5,
            r = original,
            theta = categories,
            fill = "toself",
            showlegend=False,
            name = "BASE"))

    return fig