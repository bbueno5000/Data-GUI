"""
DOCSTRING
"""
import dash
import dash_core_components.Graph as Graph
import dash_html_components.Div as Div
import dash_html_components.H1 as H1

if __name__ == '__main__':
    APP = dash.Dash()
    APP.layout = Div(children=[H1('Dash Tutorials'),
                               Graph(id='example',
                                     figure={'data': [{'x': [1, 2, 3, 4, 5],
                                                       'y': [9, 6, 2, 1, 5],
                                                       'type': 'line',
                                                       'name': 'Boats'},
                                                      {'x': [1, 2, 3, 4, 5],
                                                       'y': [8, 7, 2, 7, 3],
                                                       'type': 'bar',
                                                       'name': 'Cars'}]})])
    APP.run_server(debug=True)
