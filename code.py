import streamlit as st
import pandas as pd
import plotly.express as px

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

# Layout do Dashboard
st.title("Dashboard de Itinerário para o Vale do Capão")

cidade = st.selectbox(
    'Escolha sua cidade de origem:',
    ['Belo Horizonte', 'Juiz de Fora']
)

if cidade == 'Belo Horizonte':
    st.write("Itinerário sugerido: Ônibus para Salvador > Ônibus para Palmeiras > Van/Transporte Local para o Vale do Capão.")
elif cidade == 'Juiz de Fora':
    st.write("Itinerário sugerido: Ônibus para Salvador > Ônibus para Palmeiras > Van/Transporte Local para o Vale do Capão.")

# Mapa interativo
fig = px.scatter_mapbox(
    df, lat='Latitude', lon='Longitude', text='Cidade',
    hover_data=['Descrição'], center={'lat': -13, 'lon': -41}, zoom=5
)
fig.update_layout(mapbox_style='open-street-map', height=600)
st.plotly_chart(fig)
