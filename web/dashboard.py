import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
filepath = '/home/systemcommand/anggy/app/data/result.csv'
st = pd.read_csv(filepath)

# dropdown options
# features = st[1:-1]
opts = [{'label' : 'Truth', 'value' : 'Truth'},
        {'label' : 'Prediction', 'value' : 'Prediction'}]

# range slider options
# st['Time'] = pd.to_datetime(st.Time)
dates = ['2016-12-17', '2017-06-17', '2017-12-17', '2018-06-17', '2018-12-17',
         '2019-06-17', '2019-12-17', '2020-06-17', '2020-12-17']


# Step 3. Create a plotly figure
trace_1 = go.Scatter(x = st.Time, y = st['Truth'],
                    name = 'Truth', mode='lines+markers',
                    line = dict(color = 'royalblue'))
layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1], layout = layout)


# Step 4. Create a Dash layout
app.layout = html.Div([
                # a header and a paragraph
                html.Div([
                    html.H1("This is my first dashboard"),
                    html.P("Dash is so interesting!!")
                         ],
                     style = {'padding' : '50px' ,
                              'backgroundColor' : '#3aaab2'}),
                # adding a plot
                dcc.Graph(id = 'plot', figure = fig),
                # dropdown
                html.P([
                    html.Label("Choose a feature"),
                    dcc.Dropdown(id = 'opt', options=[
                                {'label' : 'Truth', 'value' : 'Truth'},
                                {'label' : 'Prediction', 'value' : 'Prediction'}
                                ],
                                value = 'Truth')
                        ], style = {'width': '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
                # range slider
                html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'slider',
                                    marks = {i : dates[i] for i in range(0, 9)},
                                    min = 0,
                                    max = 8,
                                    value = [1, 7])
                        ], style = {'width' : '80%',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'})
                      ])


# Step 5. Add callback functions
@app.callback(Output('plot', 'figure'),
             [Input('opt', 'value'),
             Input('slider', 'value')])
def update_figure(input1, input2):
    # filtering the data
    st2 = st[(st.Time > dates[input2[0]]) & (st.Time < dates[input2[1]])]
    # updating the plot
    trace_1 = go.Scatter(x = st2.Time, y = st2['Truth'],
                        name = 'Truth', mode='lines+markers',
                        line = dict(color = 'royalblue'))
    trace_2 = go.Scatter(x = st2.Time, y = st2[input1],
                        name = input1, mode='lines+markers',
                        line = dict(color = 'firebrick'))
    fig = go.Figure(data = [trace_1, trace_2], layout = layout)
    return fig
  
# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)