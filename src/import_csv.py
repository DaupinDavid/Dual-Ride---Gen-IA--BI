import csv
import random

# Nombre de clients à simuler
NUM_CLIENTS = 15400

# Les options réalistes (basées sur notre analyse de marché)
STYLES = [
    "Néo-Rétro 90s (Youngtimer)", "Néo-Rétro 90s (Youngtimer)", "Néo-Rétro 90s (Youngtimer)", # Plus fréquent (Tendance)
    "Sportive Vintage", "Sportive Vintage",
    "Café Racer Sportif",
    "Cyber-Punk 90s",
    "Scrambler 80s",
    "Replica Bol d'Or"
]

MOTOS_ACTUELLES = ["Yamaha MT-07", "Kawasaki Z650", "Honda Hornet", "Suzuki SV 650", "Yamaha XSR 700", "Kawasaki Z900", "BMW NineT", "Honda CB500F"]

DOULEURS = [
    "Je déteste le phare avant insecte.",
    "Trop de plastique, pas assez de carénage.",
    "Je veux des couleurs flashy (Violet/Rose).",
    "Les motos neuves manquent d'âme.",
    "Je veux le look d'avant mais la fiabilité de maintenant.",
    "Interdit de rouler en ville avec ma vieille moto (ZFE).",
    "Les designs 'Manga' vieillissent mal."
]

MOTS_CLES = ["REJET_MANGA", "DESIR_90S", "BUDGET_SERRE", "NOSTALGIE", "LOOK_CARRE", "COULEUR_VINTAGE", "FIABILITE_MODERNE"]

# Création du fichier CSV
with open('DATA_CLIENTS_FULL_15K.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    
    # En-tête
    writer.writerow(["ID_CLIENT", "AGE", "BUDGET_MAX", "MOTO_ACTUELLE", "STYLE_DESIRE", "DOULEUR_CLIENT", "MOTS_CLES_IA"])
    
    # Génération des lignes
    for i in range(1, NUM_CLIENTS + 1):
        age = random.randint(20, 55)
        # Budget réaliste autour de 7800€
        budget = random.randint(60, 110) * 100 
        
        row = [
            f"C-{i:05d}", # ID format C-00001
            age,
            f"{budget} €",
            random.choice(MOTOS_ACTUELLES),
            random.choice(STYLES),
            random.choice(DOULEURS),
            random.choice(MOTS_CLES)
        ]
        writer.writerow(row)

print(f"✅ Fichier 'DATA_CLIENTS_FULL_15K.csv' généré avec {NUM_CLIENTS} lignes !")