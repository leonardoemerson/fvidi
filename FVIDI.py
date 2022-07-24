import streamlit as st
import VizKG.visualize as vkg
import tkinter as tk
from requests import utils
DEFAULT_USER_AGENT = 'My Agent'
utils.default_user_agent = lambda: DEFAULT_USER_AGENT

st.subheader("Ferramenta de visualização interativa de dados interligados")
st.text("Digite as informações necessárias")


with st.form("form1", clear_on_submit=True): 
   endpoint = st.text_input("Digite o endpoint para consulta: ") 
   query = st.text_area("Digite a consulta: ") 
   type_graph = st.selectbox(
     'Escolha o tipo de plot: ',
     ('areachart','barchart','boxplot','bubblechart','dimensions',
     'densityplot','donutchart','graph','heatmap','histogram','imagegrid',
     'linechart','map','piechart','radar','scatterchart',
     'stackedareachart','sunburst','table','timeline','tree','treemap',
     'violinplot','wordcloud'))

   submit = st.form_submit_button("Gerar Visualização")
   
   if submit:
      sparql_query = query
      sparql_service_url = endpoint
      graph = vkg(sparql_query=sparql_query, sparql_service_url=sparql_service_url, chart=type_graph)
      graph.plot()
