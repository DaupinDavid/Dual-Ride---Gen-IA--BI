import csv
import random
from datetime import datetime, timedelta

# Configuration
NUM_CLIENTS = 15400
FILENAME = 'DATA_CLIENTS_FULL_15K_AVEC_DATE.csv'

# DONNÉES EXACTES DU DASHBOARD (Pour matcher à 100%)
# 2020: Faible / 2024: Explosion
# Ces poids forcent Excel à suivre la courbe du site web
YEARS = [2020, 2021, 2022, 2023, 2024]
WEIGHTS = [0.04, 0.06, 0.12, 0.24, 0.54] 
# Explication: 54% des lignes seront en 2024, comme sur ton graphique.

# Listes de données
STYLES = ["Néo-Rétro 90s (Youngtimer)", "Néo-Rétro 90s (Youngtimer)", "Sportive Vintage", "Café Racer Sportif", "Cyber-Punk 90s", "Scrambler 80s", "Replica Bol d'Or", "Muscle Bike 80s", "Rétro Performance", "Street Rétro", "Racer Caréné"]
MOTOS = ["Yamaha MT-07", "Kawasaki Z650", "Honda Hornet", "Suzuki SV 650", "Yamaha XSR 700", "Kawasaki Z900", "BMW NineT", "Honda CB500F"]
DOULEURS = ["Je déteste le phare avant.", "Trop de plastique.", "Couleurs trop tristes.", "Manque d'âme.", "Fiabilité douteuse.", "ZFE bloquante.", "Design manga moche."]
MOTS_CLES = {"Je déteste le phare avant.": "DESIR_CARRE", "Trop de plastique.": "MATERIAUX_NOBLES", "Couleurs trop tristes.": "COULEUR_VINTAGE", "Manque d'âme.": "NOSTALGIE", "Fiabilité douteuse.": "FIABILITE_MODERNE", "ZFE bloquante.": "EURO5_OK", "Design manga moche.": "REJET_MANGA"}

def generate_random_date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    delta = end - start
    random_days = random.randrange(delta.days)
    return (start + timedelta(days=random_days)).strftime("%d/%m/%Y")

with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    # En-tête
    writer.writerow(["ID_CLIENT", "DATE", "AGE", "BUDGET", "MOTO_ACTUELLE", "STYLE_DESIRE", "DOULEUR", "TAG_IA"])
    
    for i in range(1, NUM_CLIENTS + 1):
        # On choisit l'année selon la courbe du Dashboard
        year = random.choices(YEARS, weights=WEIGHTS, k=1)[0]
        date = generate_random_date(year)
        
        douleur = random.choice(DOULEURS)
        tag = MOTS_CLES.get(douleur, "STYLE")
        budget = random.randint(60, 110) * 100
        
        writer.writerow([
            f"C-{i:05d}", 
            date, 
            random.randint(20, 55), 
            budget, 
            random.choice(MOTOS), 
            random.choice(STYLES), 
            douleur, 
            tag
        ])

print(f"✅ Fichier Excel généré ! La distribution des dates correspond maintenant à 100% à la courbe du Dashboard.")