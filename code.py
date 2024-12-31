import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

# Dados de exemplo para o dashboard
data = {
    'Cidade': ['Belo Horizonte', 'Juiz de Fora', 'Salvador', 'Palmeiras', 'Vale do Capão'],
    'Latitude': [-19.9167, -21.761, -12.9714, -12.505, -12.5284],
    'Longitude': [-43.9345, -43.350, -38.5014, -41.575, -41.4186],
    'Descrição': [
        'Ponto de partida com conexões para Salvador',
        'Ponto de partida com conexões para Salvador',
        'Principal hub de conexões para o Vale do Capão',
        'Cidade intermediária antes do transporte local',
        'Destino final: Vale do Capão'
    ]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Figura inicial do mapa
fig = px.scatter_mapbox(
    df, lat='Latitude', lon='Longitude', text='Cidade',
    hover_data=['Descrição'],
    center={'lat': -13, 'lon': -41}, zoom=5
)
fig.update_layout(mapbox_style='open-street-map', height=600)

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Itinerário para o Vale do Capão', style={'textAlign': 'center'}),

    html.Div(children='''
        Escolha a cidade de origem para visualizar as rotas.
    ''', style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='cidade-origem',
        options=[
            {'label': 'Belo Horizonte', 'value': 'Belo Horizonte'},
            {'label': 'Juiz de Fora', 'value': 'Juiz de Fora'}
        ],
        value='Belo Horizonte',
        style={'width': '50%', 'margin': '0 auto'}
    ),

    dcc.Graph(
        id='mapa-itinerario',
        figure=fig
    ),

    html.Div(id='descricao-itinerario', style={'textAlign': 'center', 'marginTop': '20px'})
])

# Callback para atualizar descrição com base na cidade de origem
@app.callback(
    Output('descricao-itinerario', 'children'),
    Input('cidade-origem', 'value')
)
def atualizar_descricao(cidade):
    if cidade == 'Belo Horizonte':
        return 'Itinerário sugerido: Ônibus para Salvador > Ônibus para Palmeiras > Van/Transporte Local para o Vale do Capão.'
    elif cidade == 'Juiz de Fora':
        return 'Itinerário sugerido: Ônibus para Salvador > Ônibus para Palmeiras > Van/Transporte Local para o Vale do Capão.'

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
