# from turtle import pd
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap
import pandas as pd
# import folium.plugins
# from folium import GeoJson
import numpy as np
from folium.features import DivIcon
from folium import Popup

import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('JROROSCO_VOTOS.xlsx')

st.header("Informações pesquisa Junior Orosoco")

df['%']=(round(df[['Percentual']]*100,1)).astype(str)+"%"
# df2 = df[['NM_LOCALIDADE','PERC_%']].reset_index(drop=True)
# st.dataframe(df2)


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)


st.table(df[['Nome da Localidade','%','Total pesquisa','Votos']])

df_filter = df.select_dtypes(include=np.number).columns.to_list()
df_filter.remove('LAT')
df_filter.remove('LONG')


select_item = st.radio(
    "Select one",
    df_filter
)

visualize1 = st.checkbox("Visualizar mapa")

if visualize1:
    geo=r"geojs-35-mun.json"
    file = open(geo, encoding="utf8")
    text = file.read()

    m3 = folium.Map(location=[-23.638686523492638, -46.4], tiles="Cartodb Positron", zoom_start=11)

    folium.Choropleth(
        geo_data=text,
        data=df, 
        columns=['Nome da Localidade', 'Votos'],
        legend_name='Quantidade de votos',
        key_on='feature.properties.name',
        fill_color="PuBu"
        ).add_to(m3)

    for loc, p, n in zip(zip(df['LAT'],df['LONG']),df[select_item],df['Nome da Localidade']):

        if select_item == 'Percentual':
            html='<div style="font-size: 10pt; color : black">'+"{:.1%}".format(p)+'</div>'
        else:
            html='<div style="font-size: 10pt; color : black">'+"{:.0f}".format(p)+'</div>'

        folium.Marker(loc, icon=DivIcon(
            icon_size=(0,0),
            icon_anchor=(10,0),
            html=html,)).add_to(m3)
        folium.Marker(loc,
            popup=Popup(n)).add_to(m3)

    mst_data = st_folium(m3)