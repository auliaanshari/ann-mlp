import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output


data = pd.read_csv("/home/systemcommand/anggy/app/data/result.csv")

app = dash.Dash(__name__)

x = data['Time']
y = data['Truth']
y2 = data['Prediction']

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y,
                    mode='lines+markers',
                    name='Truth', line=dict(color='royalblue')))
fig.add_trace(go.Scatter(x=x, y=y2,
                    mode='lines+markers', 
                    name='Prediction', line=dict(color='firebrick')))
fig.update_layout(title='Perbandingan Data Aktual dan Prediksi Penjualan air PDAM di Kota Padang',
                   xaxis_title='Period',
                   yaxis_title='Amount')
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
        )
)

app.layout = html.Div([
                html.Div([
                    html.H1("Prediksi Penjualan Air PDAM di Kota Padang"),
                    html.P("menggunakan metode artificial neural network - multilayer perceptron")
                ],
                    style = {'padding' : '50px' , 'backgroundColor' : '#3aaab2'}),
                
                dcc.Graph(
                    id = 'plot', figure= fig ),

                ])

if __name__ == "__main__":
    app.run_server(debug=True)