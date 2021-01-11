import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

app.layout = html.Div(
    children=[
        html.H1(children="Prediksi Penjualan Air PDAM di Kota Padang",),
        html.P(
            children="menggunakan metode artificial neural network - multilayer perceptron" 
        ),
        dcc.Graph(
            figure= fig,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)