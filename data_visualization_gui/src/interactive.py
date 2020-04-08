"""
DOCSTRING
"""
import dash
import dash.dependencies as dependencies
import dash_core_components.Graph as Graph
import dash_core_components.Input as Input
import dash_html_components.Div as Div
import dash_html_components.H1 as H1

app = dash.Dash()
app.layout = Div(children=[Input(id='input', value='blank', type='text'), Div(id='output')])
@app.callback(Output(component_id='output', component_property='children'),
                [Input(component_id='input', component_property='value')])
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)
app.run_server(debug=True)