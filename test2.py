import pandas as pd
import streamlit as st

villas_bs4 = pd.read_csv("Vente_Locations_Villas.csv")
appartements_bs4 = pd.read_csv("Appartements.csv")
terrains_bs4 = pd.read_csv("Terrains.csv")

villas_ws = pd.read_csv("villas_ws.csv")
appartements_ws = pd.read_csv("appartements_ws.csv")
terrains_ws = pd.read_csv("terrains_ws.csv")

st.title("Projet Data Collection Groupe 2")

taches = ["BeautifulSoup4", "Web Scraper","Dashboard"]
choix = st.sidebar.selectbox("Selectionner", taches)

options = ["Villas", "Appartements", "Terrains"]
selection = st.sidebar.selectbox("Sélectionner les données à afficher :", options)

if choix == taches[0]:
    if selection == "Villas":
        st.subheader("Voici les données des villas extraites et netoyees avec BeautifulSoup4 :")
        st.write(villas_bs4)
        st.write("Nombre de lignes et de colonnes pour les données des villas : ", villas_bs4.shape)
    elif selection == "Appartements":
        st.subheader("Voici les données des appartements extraites et netoyees avec BeautifulSoup4 :")
        st.write(appartements_ws)
        st.write("Nombre de lignes et de colonnes pour les données des appartements : ", appartements_ws.shape)
    elif selection == "Terrains":
        st.subheader("Voici les données des terrains extraites et netoyees avec BeautifulSoup4 :")
        st.write(terrains_bs4)
        st.write("Nombre de lignes et de colonnes pour les données des terrains : ", terrains_bs4.shape)
elif choix == taches[1]:
    if selection == "Villas":
        st.subheader("Voici les données des villas extraites avec Web scraper :")
        st.write(villas_ws)
        st.write("Nombre de lignes et de colonnes pour les données des villas : ", villas_ws.shape)
    elif selection == "Appartements":
        st.subheader("Voici les données des appartements extraites avec Web scraper :")
        st.write(appartements_ws)
        st.write("Nombre de lignes et de colonnes pour les données des appartements : ", appartements_ws.shape)
    elif selection == "Terrains":
        st.subheader("Voici les données des terrains extraites avec Web scraper :")
        st.write(terrains_ws)
        st.write("Nombre de lignes et de colonnes pour les données des terrains : ", terrains_ws.shape)