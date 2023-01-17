import streamlit as st
import sci

st.title("Récupérer des sci")

nom_association = st.text_input("Nom de l'association", "Association diocèsaine de Rennes")
fermée = st.checkbox("Fermée", value=False)

if st.button("Récupérer les informations"):
    sci.get_sci(nom_association, fermée)
    st.write(sci.df_sci)

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(sci.df_sci)

st.download_button(
   "Enregistrer le fichier",
   csv,
   "scis.csv",
   "text/csv",
   key='download-csv'
)