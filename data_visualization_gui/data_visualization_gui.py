
"""
- purpose: download data from Quandl and display it in Dash
- source: <https://pythonprogramming.net/using-quandl-data/>

"""
# standard
import datetime
# non-standard
import dash
import dash.dependencies as dependencies
import dash_core_components.Graph as Graph
import dash_core_components.Input as Input
import dash_html_components.Div as Div
import dash_html_components.H1 as H1

app = dash.Dash()

app.layout = Div(children=[H1('Dash Tutorials'),
                           Graph(id='example',
                                 figure={'data': [{'x': [1, 2, 3, 4, 5],
                                                   'y': [9, 6, 2, 1, 5],
                                                   'type': 'line',
                                                   'name': 'Boats'},
                                                  {'x': [1, 2, 3, 4, 5],
                                                   'y': [8, 7, 2, 7, 3],
                                                   'type': 'bar',
                                                   'name': 'Cars'}]})])

#app.layout = Div([Div(children='Symbol to graph:'),
#                  Input(id='input', value='', type='text'),
#                  Div(id='output-graph')])

#@app.callback(dependencies.Output(component_id='output-graph', component_property='children'),
#             [dependencies.Input(component_id='input', component_property='value')])

#def update_value(input_data):
#    quandl.ApiConfig.api_key = "ypzBJYSBk3vDxmUSxAsi"
#    df = quandl.get("EIA/PET_RWTC_D", start_date="2010-12-31", end_date="2015-12-31")
#    print(df.head())
#    df.reset_index(inplace=True)
#    df.set_index("Date", inplace=True)
#    return Graph(id='example-graph',
#                 figure={'data': [{'x': df.index,
#                                   'y': df.Value,
#                                   'type': 'line',
#                                   'name': "EIA/PET_RWTC_D"}],
#                         'layout': {'title': "EIA/PET_RWTC_D"}})

if __name__ == '__main__':
    app.run_server(debug=True)