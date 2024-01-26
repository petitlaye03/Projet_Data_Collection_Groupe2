# Importation des packages
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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
choix = st.sidebar.selectbox("Selectionner", taches)

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
else:
        st.title("Données Web Scrapping")
        st.write("Voici les differents graphiques  ")
    # Simuler des données pour le tableau de bord
    # Créer un DataFrame
        df = pd.read_csv("Vente_Locations_Villas.csv")
        da = pd.read_csv("Appartements.csv")
        dt = pd.read_csv("Terrains.csv")
    # Créer le diagramme camembert pour la variable "villa"
        st.subheader("Taux Vente/Location ")
        villa_counts = df['Type_annonce'].value_counts()
    # Diagramme camembert directement dans la page
        fig, ax = plt.subplots()
        ax.pie(villa_counts.head(2), labels=villa_counts.head(2).index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'), wedgeprops=dict(width=0.4))
        ax.axis('equal')
        st.pyplot(fig)
        st.subheader("Courbe de Régression")
        fi, ax = plt.subplots()
    # Utiliser l'axe pour créer un nuage de points
        sns.regplot(data=da, x='Nombre_pieces', y='Prix', color='blue', scatter_kws={'s': 100})
    # Personnaliser l'axe et le graphique
        ax.set_xlabel('Nombre de Pièces')
        ax.set_ylabel('Prix')
        ax.set_title('Courbe de Régression Nombre de Pièces/Prix')
    # Afficher le graphique avec Streamlit
        st.pyplot(fi)
        st.subheader("Courbe de Régression")
    # Créer un objet de figure et un axe avec Matplotlib
        fid, ax = plt.subplots()
    # Utiliser l'axe pour créer un nuage de points
        ax.scatter(dt['Superficie'], dt['Prix'], c='blue', label='Biens immobiliers')
    # Personnaliser l'axe et le graphique
        ax.set_xlabel('Superficie (m²)')
        ax.set_ylabel('Prix (EUR)')
        ax.set_title('Nuage de Points Prix/Superficie')
    # Ajouter une légende
        ax.legend()
    # Afficher le graphique avec Streamlit
        st.pyplot(fid)












