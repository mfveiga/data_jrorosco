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

df['PERC_%']=(round(df[['PERC']]*100,1)).astype(str)+"%"
# df2 = df[['NM_LOCALIDADE','PERC_%']].reset_index(drop=True)
# st.dataframe(df2)
st.dataframe(df)

df_filter = df.select_dtypes(include=np.number).columns.to_list()
df_filter.remove('LAT')
df_filter.remove('LONG')


select_item = st.radio(
    "Select one",
    df_filter
)

geo=r"geojs-35-mun.json"
file = open(geo, encoding="utf8")
text = file.read()

m3 = folium.Map(location=[-23.638686523492638, -46.4], tiles="Cartodb Positron", zoom_start=11)

folium.Choropleth(
    geo_data=text,
    data=df, 
    columns=['NM_LOCALIDADE', 'VOTOS'],
    legend_name='Quantidade de votos',
    key_on='feature.properties.name',
    fill_color="PuBu"
    ).add_to(m3)

for loc, p, n in zip(zip(df['LAT'],df['LONG']),df[select_item],df['NM_LOCALIDADE']):

    if select_item == 'PERC':
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
