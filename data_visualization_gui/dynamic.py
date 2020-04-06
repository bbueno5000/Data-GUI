"""
DOCSTRING
"""
# standard
import datetime
# non-standard
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web

if __name__ == '__main__':
    app = dash.Dash()
    stock = 'GOOGL'
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2018, 2, 8)
    df = web.DataReader(stock, 'morningstar', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)
    app.layout = html.Div(children=[html.Div(children='ticker symbol'),
                                    dcc.Input(id='input', value='', type='text'),
                                    html.Div(id='output-graph')])
    @app.callback(dash.dependencies.Output(component_id='output-graph', 
                                           component_property='children'),
                  [dash.dependencies.Input(component_id='input', component_property='value')])
    def update_value(input_data):
        """
        DOCSTRING
        """
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(input_data, 'morningstar', start, end)
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df = df.drop("Symbol", axis=1)
        return dcc.Graph(id='example-graph',
                         figure={'data':[{'x':df.index,
                                          'y':df.Close,
                                          'type':'line',
                                          'name':input_data}],
                                 'layout':{'title':input_data}})
    app.run_server(debug=True)
