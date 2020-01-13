"""
- purpose: download data from Quandl and display it in Dash
- source: <https://pythonprogramming.net/using-quandl-data/>

"""
from dash import Dash
from dash import dependencies
from dash_core_components import Graph    # pylint: disable=E0611
from dash_core_components import Input    # pylint: disable=E0611
from dash_html_components import Div      # pylint: disable=E0611
from datetime import datetime
from quandl import ApiConfig
from quandl import get

app = Dash()

app.layout = Div([Div(children='Symbol to graph:'),
                  Input(id='input', value='', type='text'),
                  Div(id='output-graph')])

@app.callback(dependencies.Output(component_id='output-graph', component_property='children'),
             [dependencies.Input(component_id='input', component_property='value')])

def update_value(input_data):
    ApiConfig.api_key = "ypzBJYSBk3vDxmUSxAsi"
    df = get("EIA/PET_RWTC_D", start_date="2010-12-31", end_date="2015-12-31")
    print(df.head())
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    return Graph(
        id='example-graph',
        figure={'data': [{'x': df.index, 'y': df.Value, 'type': 'line', 'name': "EIA/PET_RWTC_D"}],
                'layout': {'title': "EIA/PET_RWTC_D"}})

if __name__ == '__main__':
    app.run_server(debug=True)