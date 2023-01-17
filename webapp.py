import streamlit as st
import sci

st.title("Récupérer des sci")

nom_association = st.text_input("Nom de l'association", "Association diocèsaine de Rennes")
fermée = st.checkbox("Fermée", value=False)

def convert_df(df):
   return df.to_csv(index=False)

if st.button("Récupérer les informations"):
    sci.get_sci(nom_association, fermée)
    st.write(sci.df_sci)
    csv = convert_df(sci.df_sci)
    st.download_button(
    "Enregistrer le fichier",
    csv,
    f"scis_{nom_association.replace(' ','_')}.csv",
    "text/csv",
    key='download-csv'
    )


