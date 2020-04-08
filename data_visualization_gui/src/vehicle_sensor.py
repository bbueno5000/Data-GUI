"""
Vehicle sensor data App Example - Data Visualization GUIs with Dash and Python p.5
"""
# standard
import collections
import time
# non-standard
import dash
import dash_core_components.Dropdown as Dropdown
import dash_core_components.Graph as Graph
import dash_core_components.Interval as Interval
import dash_html_components.Div as Div
import dash_html_components.H2 as H2
import plotly.graph_objs as graph_objs
import random

app = dash.Dash('vehicle-data')
max_length = 50
times = collections.deque(maxlen=max_length)
oil_temps = collections.deque(maxlen=max_length)
intake_temps = collections.deque(maxlen=max_length)
coolant_temps = collections.deque(maxlen=max_length)
rpms = collections.deque(maxlen=max_length)
speeds = collections.deque(maxlen=max_length)
throttle_pos = collections.deque(maxlen=max_length)
data_dict = {"Oil Temperature":oil_temps,
             "Intake Temperature": intake_temps,
             "Coolant Temperature": coolant_temps,
             "RPM":rpms,
             "Speed":speeds,
             "Throttle Position":throttle_pos}

def update_obd_values(times,
                      oil_temps,
                      intake_temps,
                      coolant_temps,
                      rpms,
                      speeds,
                      throttle_pos):
    """
    DOCSTRING
    """
    times.append(time.time())
    if len(times) == 1:
        oil_temps.append(random.randrange(180,230))
        intake_temps.append(random.randrange(95,115))
        coolant_temps.append(random.randrange(170,220))
        rpms.append(random.randrange(1000,9500))
        speeds.append(random.randrange(30,140))
        throttle_pos.append(random.randrange(10,90))
    else:
        for data_of_interest in [oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]:
            data_of_interest.append(data_of_interest[-1] \
                                    + data_of_interest[-1] \
                                    * random.uniform(-0.0001, 0.0001))
    return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos

times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = \
    update_obd_values(times,
                      oil_temps,
                      intake_temps,
                      coolant_temps,
                      rpms,
                      speeds,
                      throttle_pos)

app.layout = Div([Div([H2('Vehicle Data',
                          style={'float': 'left'})]),
                  Dropdown(id='vehicle-data-name',
                           options=[{'label': s, 'value': s} for s in data_dict.keys()],
                           value=['Coolant Temperature',
                                  'Oil Temperature',
                                  'Intake Temperature'],
                           multi=True),
                  Div(children=Div(id='graphs'), className='row'),
                  Interval(id='graph-update', interval=100)],
                 className="container", 
                 style={'width':'98%',
                        'margin-left':10,
                        'margin-right':10,
                        'max-width':50000})

@app.callback(dash.dependencies.Output('graphs', 'children'),
              [dash.dependencies.Input('vehicle-data-name', 'value')],
              state=[dash.dependencies.State('graph-update', 'interval')])
def update_graph(data_names, value):
    """
    DOCSTRING
    """
    graphs = []
    update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'
    for data_name in data_names:
        data = graph_objs.Scatter(x=list(times),
                                  y=list(data_dict[data_name]),
                                  name='Scatter',
                                  fill="tozeroy",
                                  fillcolor="#6897bb")
        graphs.append(Div(Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],
                    'layout' : graph_objs.Layout(xaxis=dict(range=[min(times), max(times)]),
                                                 yaxis=dict(range=[min(data_dict[data_name]), max(data_dict[data_name])]),
                                                 margin={'l':50, 'r':1, 't':45, 'b':1},
                                                 title='{}'.format(data_name))}), className=class_choice))
    return graphs

external_css = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css']
for css in external_css:
    app.css.append_css({'external_url': css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
    app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    app.run_server(debug=True)
