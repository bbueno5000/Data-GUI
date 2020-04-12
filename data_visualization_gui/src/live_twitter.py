"""
Live Twitter Sentiment Graph - Data Visualization GUIs with Dash and Python
"""
# standard
import collections
import input
import random
# non-standard
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.graph_objects as graph_objs
import sqlite3

app = dash.Dash(__name__)

app.layout = html.Div([html.H2('Live Twitter Sentiment'),
                       dcc.Input(id='sentiment_term', value='olympic', type='text'),
                       dcc.Graph(id='live-graph', animate=True),
                       dcc.Interval(id='graph-update', interval=1000)])

@app.callback(dash.dependencies.Output('live-graph', 'figure'),
              [dash.dependencies.Input(component_id='sentiment_term', component_property='value')],
              state=[dash.dependencies.State('graph-update', 'interval')])
def update_graph_scatter():
    """
    DOCSTRING
    """
    try:
        conn = sqlite3.connect('twitter.db')
        c = conn.cursor()
        df = pandas.read_sql(
            "SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000",
            conn)
        df.sort_values('unix', inplace=True)
        df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
        df['date'] = pd.to_datetime(df['unix'], unit='ms')
        df.set_index('date', inplace=True)
        df = df.resample('1min').mean()
        df.dropna(inplace=True)
        X = df.index
        Y = df.sentiment_smoothed.values[-100:]
        data = graph_objs.Scatter(x=X, y=Y, name='Scatter', mode= 'lines+markers')
        return {'data': [data],
                'layout': graph_objs.Layout(xaxis=dict(range=[min(X), max(X)]),
                                            yaxis=dict(range=[min(Y), max(Y)]),
                                            title='Term: {}'.format(sentiment_term))}
    except Exception as e:
        with open('errors.txt','a') as f:
            f.write(str(e))
            f.write('\n')

if __name__ == '__main__':
    app.run_server(debug=True)
