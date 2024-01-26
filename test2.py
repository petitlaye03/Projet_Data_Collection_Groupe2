# Importation des packages
import pandas as pd
import streamlit as st

# Chargement des données depuis les fichiers CSV pour BeautifulSoup4
villas_bs4 = pd.read_csv("Vente_Locations_Villas.csv")
appartements_bs4 = pd.read_csv("Appartements.csv")
terrains_bs4 = pd.read_csv("Terrains.csv")

# Chargement des données depuis les fichiers CSV pour Web Scraper
villas_ws = pd.read_csv("villas_ws.csv")
appartements_ws = pd.read_csv("appartements_ws.csv")
terrains_ws = pd.read_csv("terrains_ws.csv")

# Titre de l'application Streamlit
st.title("Projet Data Collection Groupe 2")

# Liste des tâches disponibles
taches = ["BeautifulSoup4", "Web Scraper","Dashboard"]

# Options pour la sélection des données
options = ["Villas", "Appartements", "Terrains"]

# Sélection de la tâche depuis la barre latérale
choix = st.sidebar.selectbox("Selectionner la methode de scraping", taches)

# Sélection des données à afficher depuis la barre latérale
selection = st.sidebar.selectbox("Sélectionner les données à afficher :", options)

# Gestion de l'affichage en fonction de la tâche choisie
if choix == taches[0]:  # Si l'utilisateur choisit BeautifulSoup4
    if selection == "Villas":
        st.subheader("Voici les données des villas extraites et nettoyées avec BeautifulSoup4 :")
        st.write(villas_bs4)
        st.write("Nombre de lignes et de colonnes pour les données des villas : ", villas_bs4.shape)
    elif selection == "Appartements":
        st.subheader("Voici les données des appartements extraites et nettoyées avec BeautifulSoup4 :")
        st.write(appartements_bs4)
        st.write("Nombre de lignes et de colonnes pour les données des appartements : ", appartements_bs4.shape)
    elif selection == "Terrains":
        st.subheader("Voici les données des terrains extraites et nettoyées avec BeautifulSoup4 :")
        st.write(terrains_bs4)
        st.write("Nombre de lignes et de colonnes pour les données des terrains : ", terrains_bs4.shape)
elif choix == taches[1]:  # Si l'utilisateur choisit Web Scraper
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
