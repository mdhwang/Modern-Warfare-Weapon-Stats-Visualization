import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
server = app.server

app.layout = html.Div([

    dcc.Dropdown(
        id='model-selector',
        options=[{'label': i, 'value': i} for i in ["OLS", "Lasso"]],
        value="OLS"
    ),

    dcc.Input(id="polynomial-order", type="number", value=0),
    dcc.Input(id="alpha", type="number", value=0),

    html.Div(id='display-selected-values')
])

# HIDE THE ALPHA SELECTOR (YOU COULD HIDE AN ENTIRE DIV IF YOU WANTED)
@app.callback(Output('alpha', 'style'), [Input('model-selector', 'value')])
def toggle_container(toggle_value):
    if toggle_value == 'OLS':
        return {'display': 'none'}
    else:
        return {'display': 'block'}


@app.callback(
    Output('display-selected-values', 'children'),
    [Input('model-selector', 'value'),
     Input('polynomial-order', 'value'),
     Input('alpha', 'value')])
def set_display_children(model, order, alpha):
    if model == "OLS":
        return f"Model: {model},  Order: {order}."
    else:
        return f"Model: {model},  Order: {order}, Alpha: {alpha}."

if __name__ == "__main__":
    app.server.run(port=8000, host='127.0.0.1')
    app.run_server(debug=True)