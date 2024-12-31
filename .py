import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

# Dados de exemplo
data = {
    'Cidade': ['Belo Horizonte', 'Juiz de Fora', 'Salvador', 'Palmeiras', 'Vale do Capão'],
    'Latitude': [-19.9167, -21.761, -12.9714, -12.505, -12.5284],
    'Longitude': [-43.9345, -43.350, -38.5014, -41.575, -41.4186]
}
df = pd.DataFrame(data)

# Figura do mapa
fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', text='Cidade',
                        center={'lat': -13, 'lon': -41}, zoom=5)
fig.update_layout(mapbox_style='open-street-map')

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Itinerário para o Vale do Capão'),

    html.Div(children='''
        Selecione a cidade de origem:
    '''),

    dcc.Dropdown(
        id='cidade-origem',
        options=[
            {'label': 'Belo Horizonte', 'value': 'Belo Horizonte'},
            {'label': 'Juiz de Fora', 'value': 'Juiz de Fora'}
        ],
        value='Belo Horizonte'
    ),

    dcc.Graph(
        id='mapa-itinerario',
        figure=fig
    )
])

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
