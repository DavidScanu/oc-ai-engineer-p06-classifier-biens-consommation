import requests
import pandas as pd
import json

def collecter_produits_champagne(nombre_produits=10):
    """
    Collecte des produits à base de champagne via l'API Open Food Facts.
    
    Args:
        nombre_produits (int): Nombre de produits à collecter
        
    Returns:
        DataFrame: DataFrame contenant les produits collectés
    """
    # URL de base de l'API Open Food Facts
    base_url = "https://world.openfoodfacts.org/cgi/search.pl"
    
    # Paramètres de la requête
    params = {
        "search_terms": "champagne",
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 10,
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": "champagnes"  # Filtrer par la catégorie "champagnes"
    }
    
    # Effectuer la requête à l'API
    print("Envoi de la requête à l'API Open Food Facts...")
    response = requests.get(base_url, params=params)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        data = response.json()
        produits = data.get('products', [])
        print(f"{len(produits)} produits trouvés.")
        
        # Extraire les données demandées
        resultats = []
        for produit in produits:
            # Extraction des données requises
            food_id = produit.get('code', '')
            label = produit.get('product_name', '')
            categories = produit.get('categories', '')
            food_contents_label = produit.get('ingredients_text', '')
            image_url = produit.get('image_url', '')
            
            resultats.append({
                'foodId': food_id,
                'label': label,
                'category': categories,
                'foodContentsLabel': food_contents_label,
                'image': image_url
            })
        
        # Créer un DataFrame pandas
        df = pd.DataFrame(resultats)
        return df
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        return None

def sauvegarder_csv(df, nom_fichier="produits_champagne.csv"):
    """
    Sauvegarde les données dans un fichier CSV.
    
    Args:
        df (DataFrame): DataFrame contenant les produits
        nom_fichier (str): Nom du fichier CSV à créer
    """
    if df is not None and not df.empty:
        df.to_csv(nom_fichier, index=False, encoding='utf-8')
        print(f"Les données ont été sauvegardées dans {nom_fichier}")
    else:
        print("Aucune donnée à sauvegarder.")

# Exécution principale
if __name__ == "__main__":

    # Configurer pandas pour afficher toutes les colonnes et lignes
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)

    # Collecter les 10 premiers produits contenant "champagne"
    df_produits = collecter_produits_champagne(10)
    
    # Afficher un aperçu des produits collectés
    if df_produits is not None and not df_produits.empty:
        print("\nDonnées complètes des produits collectés :")
        print(df_produits)
        
        # Sauvegarder dans un fichier CSV
        sauvegarder_csv(df_produits)
    else:
        print("Impossible de collecter les produits.")