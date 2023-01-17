import requests
import json
import pandas as pd

def get_sci(nom_association:str, fermée:bool=False):
    """
    Récupérer les informations d'une SCI à partir de son SIREN
    """
    nom_asso_url = nom_association.replace(" ", "+")
    url = f"https://api.pappers.fr/v2/recherche-dirigeants?q={nom_asso_url}&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&precision=standard&page=1&par_page=20"
    req = requests.get(url)
    data = req.json()
    # return data
    save_sci(data, fermée)

def save_sci(data:str, fermée:bool=False):
    """
    Enregistrer les informations d'une SCI dans un dataframe
    """

    global df_sci

    df_sci = pd.DataFrame(columns=["nom_societe", "siren_societe", "actuel", "forme_juridique", "statut_rcs", "capital", "date_creation", "adresse_siege", "ville_siege", "nom_association", "siren_association"])

    for entry in data:
        for resultat in data["resultats"]:
            if resultat["actuel"] == False and fermée == False:
                pass
            else:
                nom_association = resultat["denomination"]
                siren_association = resultat["siren"]
                actuel = resultat["actuel"]

                for entreprise in resultat["entreprises"]:
                # Create a dictionary
                    dict = {"nom_societe": entreprise["nom_entreprise"], 
                            "siren_societe": entreprise["siren"],
                            "actuel": actuel, 
                            "forme_juridique": entreprise["forme_juridique"], 
                            "statut_rcs": entreprise["statut_rcs"], 
                            "capital": entreprise["capital"], 
                            "date_creation": entreprise["date_creation"], 
                            "adresse_siege": entreprise["siege"]["adresse_ligne_1"], 
                            "ville_siege": entreprise["siege"]["ville"],
                            "nom_association": nom_association, 
                            "siren_association": siren_association,}
                    # Append the dictionary as a row in the dataframe
                    df_sci = df_sci.append(dict, ignore_index=True)
    
    return df_sci
