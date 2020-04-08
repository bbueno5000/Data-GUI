"""
Live Graphs with Events - Data Visualization GUIs with Dash and Python p.4
"""
# standard
import collections
# non-standard
import dash
import dash_core_components.Graph as Graph
import dash_core_components.Interval as Interval
import dash_html_components.Div as Div
import plotly.graph_objs as graph_objs
import random

if __name__ == '__main__':
    variable_X = collections.deque(maxlen=20)
    variable_Y = collections.deque(maxlen=20)

    variable_X.append(1)
    variable_Y.append(1)

    app = dash.Dash(__name__)
    app.layout = Div([Graph(id='live-graph', animate=True),
                      Interval(id='graph-update', interval=1000)])

    @app.callback(dash.dependencies.Output('live-graph', 'figure'), 
                  state=[dash.dependencies.State('graph-update', 'interval')])
    def update_graph_scatter():
        """
        DOCSTRING
        """
        variable_X.append(variable_X[-1]+1)
        variable_Y.append(variable_Y[-1] + variable_Y[-1]*random.uniform(-0.1, 0.1))
        data = graph_objs.Scatter(x=list(variable_X),
                                         y=list(variable_Y),
                                         name='Scatter',
                                         mode= 'lines+markers')
        return {'data':[data],
                'layout':graph_objs.Layout(xaxis=dict(range=[min(variable_X), max(variable_X)]),
                                           yaxis=dict(range=[min(variable_Y), max(variable_Y)]))}

    app.run_server(debug=True)
